"""Merge this run's data/ into the latest data/ on main, so no run can lose another run's rows.

Run #7 (2026-11-25) lost an hour of data: it started from an older commit, its
data clashed with what another run had pushed, and the git rebase failed.
Now the commit step does: copy our data aside -> reset to origin/main ->
merge our rows in here -> commit -> push (retry from the top if main moved).

Second bug (found 2026-11-25 by ChatGPT): a run that started before someone edited
team_board.md pushed its OLD copy back over main ("ours wins"), erasing Claude's reply.
Now a file this run did not change is never written back (compared to the copy taken at
checkout), and the team board is merged entry by entry so nobody's note is lost.

Usage: python sync_data.py <our_data_dir> <repo_data_dir> [<base_data_dir_at_checkout>]
"""
import csv
import os
import shutil
import sys

# append-only logs: union of rows, de-duplicated by key
KEYS = {
    "checkpoints.csv": ("slug", "secs_left", "logged_utc"),
    "results.csv": ("slug",),
    "tickets.csv": ("t_start",),
    "loop_stats.csv": ("run_utc",),
}
# fingerprint lists: union of lines
UNION_LINES = {"account_seen.txt"}
# conversation logs: merge entries ("### <time> · <who>") from both sides
BOARDS = {"team_board.md"}
# written only by people (pasted ChatGPT replies): main always wins
HUMAN = {"chatgpt_notes.md"}
# everything else (report.md, *_stats.json, model_tune.json) is regenerated: ours wins


def read(path):
    if not os.path.exists(path):
        return [], []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def merge_csv(name, ours, theirs, out):
    f_o, r_o = read(ours)
    f_t, r_t = read(theirs)
    fields = f_o + [f for f in f_t if f not in f_o]          # newest code's column order first
    key = KEYS[name]
    merged = {}
    for r in r_t + r_o:                                      # ours last: our version of a row wins (e.g. a settled result)
        k = tuple(r.get(c, "") for c in key)
        if k in merged:
            merged[k].update({c: v for c, v in r.items() if v not in (None, "")})
        else:
            merged[k] = dict(r)
    rows = list(merged.values())
    if "logged_utc" in fields:
        rows.sort(key=lambda r: r.get("logged_utc") or "")
    elif "t_start" in fields:
        rows.sort(key=lambda r: int(r.get("t_start") or 0))
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return len(r_o), len(r_t), len(rows)


def _text(p):
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return f.read()


def merge_board(ours, theirs):
    """Union of '### ' entries, ordered by their timestamp; header from main."""
    def split(t):
        parts = (t or "").split("\n### ")
        return parts[0], ["### " + x.strip() + "\n" for x in parts[1:]]
    head_t, ent_t = split(theirs)
    head_o, ent_o = split(ours)
    seen, merged = set(), []
    for e in ent_t + ent_o:
        k = e.strip()
        if k not in seen:
            seen.add(k)
            merged.append(e)
    merged.sort(key=lambda e: e.split("\n", 1)[0][4:21])      # "YYYY-MM-DD HH:MMZ"
    head = (head_t if theirs is not None else head_o).rstrip() + "\n"
    return head + "".join("\n" + e for e in merged)


def main(ours_dir, repo_dir, base_dir=None):
    os.makedirs(repo_dir, exist_ok=True)
    for name in sorted(os.listdir(ours_dir)):
        src, dst = os.path.join(ours_dir, name), os.path.join(repo_dir, name)
        if os.path.isdir(src):
            continue
        if base_dir is not None and _text(src) == _text(os.path.join(base_dir, name)):
            continue                                            # we didn't touch it: keep main's version
        if name in HUMAN:
            continue                                            # Jacob edits these by hand; a run never overwrites them
        if name in BOARDS:
            merged = merge_board(_text(src), _text(dst))       # read main's copy BEFORE opening it for writing
            with open(dst, "w", encoding="utf-8") as f:
                f.write(merged)
            print(f"merged {name} entries")
        elif name in KEYS:
            o, t, m = merge_csv(name, src, dst, dst + ".tmp")
            os.replace(dst + ".tmp", dst)
            print(f"merged {name}: ours {o} + main {t} -> {m}")
        elif name in UNION_LINES:
            lines = set()
            for p in (src, dst):
                if os.path.exists(p):
                    with open(p, encoding="utf-8") as f:
                        lines |= {x.strip() for x in f if x.strip()}
            with open(dst, "w", encoding="utf-8") as f:
                f.write("\n".join(sorted(lines)) + "\n")
            print(f"merged {name}: {len(lines)} lines")
        else:
            shutil.copyfile(src, dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
