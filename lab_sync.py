"""Research lab sync ($0): GitHub Issues are the strategy database.

Runs in GitHub Actions with the free built-in GITHUB_TOKEN:
1. makes sure the lab labels exist
2. seeds the starting strategies from lab/seed.json (once each, matched by title)
3. Gemini (free tier, optional) reviews each new strategy issue once and comments
4. rebuilds lab/DATABASE.md and lab/strategies.csv from the issues
It never touches data/ or the live experiments, never changes a stage label on its own
(people decide stages), and never places a trade.
"""
import csv
import json
import os
import re
import sys
from datetime import datetime, timezone

import requests

API = "https://api.github.com"
REPO = os.getenv("GITHUB_REPOSITORY", "j42002/polybot")
TOKEN = os.getenv("GITHUB_TOKEN", "")
LAB = "lab"
GEMINI_DAILY = int(os.getenv("LAB_GEMINI_DAILY", "20"))

LABELS = {
    "strategy": ("0e8a16", "A trading idea in the lab"),
    "stage:1-submitted": ("c5def5", "Claim recorded"),
    "stage:2-evidence": ("bfdadc", "Sources and counter-evidence checked"),
    "stage:3-review": ("fef2c0", "Challenged by reviewers"),
    "stage:4-preregistered": ("f9d0c4", "Rules frozen before any result"),
    "stage:5-testing": ("d4c5f9", "Paper test running"),
    "stage:6-verdict": ("5319e7", "Finished"),
    "evidence:L0-claim": ("eeeeee", "Someone says it works"),
    "evidence:L1-sourced": ("c2e0c6", "Original source + exact rules"),
    "evidence:L2-historical": ("7fd3a5", "Survived an exploratory historical test"),
    "evidence:L3-forward": ("0e8a16", "Survived a pre-registered forward paper test"),
    "verdict:supported": ("0e8a16", "Forward test supports it"),
    "verdict:refuted": ("b60205", "Evidence says it does not work"),
    "verdict:inconclusive": ("fbca04", "Not enough evidence either way"),
    "verdict:untestable": ("cccccc", "Cannot be paper-tested honestly at $0"),
    "gemini-reviewed": ("1d76db", "Gemini posted its independent review"),
}
STAGE_ORDER = ["stage:1-submitted", "stage:2-evidence", "stage:3-review", "stage:4-preregistered",
               "stage:5-testing", "stage:6-verdict"]


class GH:
    def __init__(self, token, repo, session=None):
        self.s = session or requests.Session()
        self.s.headers.update({"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json",
                               "X-GitHub-Api-Version": "2022-11-28"})
        self.repo = repo

    def req(self, method, path, **kw):
        r = self.s.request(method, f"{API}/repos/{self.repo}{path}", timeout=20, **kw)
        if r.status_code >= 400 and not (method == "POST" and path == "/labels" and r.status_code == 422):
            raise RuntimeError(f"GitHub {method} {path} -> {r.status_code}")
        return r

    def all_issues(self):
        out, page = [], 1
        while True:
            r = self.req("GET", "/issues", params={"state": "all", "per_page": 100, "page": page})
            items = [i for i in r.json() if "pull_request" not in i]
            out += items
            if len(r.json()) < 100:
                return out
            page += 1


def ensure_labels(gh):
    have = {l["name"] for l in gh.req("GET", "/labels", params={"per_page": 100}).json()}
    made = 0
    for name, (color, desc) in LABELS.items():
        if name not in have:
            gh.req("POST", "/labels", json={"name": name, "color": color, "description": desc})
            made += 1
    return made


def body_from_fields(fields):
    return "\n\n".join(f"### {k}\n\n{v}" for k, v in fields.items()) + "\n\n_Seeded by the lab from existing work._"


def seed(gh, issues, path=os.path.join(LAB, "seed.json")):
    if not os.path.exists(path):
        return 0
    titles = {i["title"] for i in issues}
    made = 0
    for s in json.load(open(path, encoding="utf-8")):
        if s["title"] in titles:
            continue
        gh.req("POST", "/issues", json={"title": s["title"], "body": body_from_fields(s["fields"]), "labels": s["labels"]})
        made += 1
    return made


def parse_fields(body):
    """Issue-form bodies are '### Heading\\n\\nvalue' blocks."""
    out = {}
    for block in re.split(r"\n?### ", "\n" + (body or "")):
        if not block.strip():
            continue
        head, _, val = block.partition("\n")
        out[head.strip()] = val.strip()
    return out


def label_names(issue):
    return [l["name"] if isinstance(l, dict) else l for l in issue.get("labels", [])]


def first(labels, prefix):
    for l in labels:
        if l.startswith(prefix):
            return l.split(":", 1)[1]
    return ""


# ---------- Gemini independent review (free tier, optional) ----------

def gemini_review(gh, issues, ask=None):
    if ask is None:
        if not os.getenv("GEMINI_API_KEY"):
            print("lab: no GEMINI_API_KEY - Gemini reviews off")
            return 0
        import team                                   # reuse the free-tier client
        team.USAGE = os.path.join(LAB, "gemini_usage.json")
        team.DAILY_CAP = GEMINI_DAILY
        ask = team.ask_gemini
    done = 0
    for i in issues:
        labels = label_names(i)
        if (i.get("state") != "open" or "strategy" not in labels or "gemini-reviewed" in labels
                or "stage:6-verdict" in labels):
            continue
        prompt = ("You are the independent reviewer of a $0 paper-trading research lab. No strategy is trusted because "
                  "a trader claims it works. Review this strategy record without assuming it works.\n\n"
                  f"TITLE: {i['title']}\n\n{(i.get('body') or '')[:6000]}\n\n"
                  "Answer in under 160 words with these headings: Biggest weaknesses (3 bullets) / Exact testable rules / "
                  "Evidence level (L0 claim or L1 sourced, one line why) / What result would prove it wrong.")
        try:
            text = ask(prompt)
        except Exception as e:
            print(f"lab: Gemini skipped #{i['number']} ({e})")
            break                                     # cap or limit reached: try again next run
        gh.req("POST", f"/issues/{i['number']}/comments",
               json={"body": f"**Gemini (independent reviewer, automatic)**\n\n{text}\n\n_Free-tier review. Does not change the stage; Jacob does._"})
        gh.req("POST", f"/issues/{i['number']}/labels", json={"labels": ["gemini-reviewed"]})
        done += 1
    return done


# ---------- database files ----------

def build_db(issues):
    rows = []
    for i in issues:
        labels = label_names(i)
        if "strategy" not in labels:
            continue
        f = {k: v.replace("|", "/").replace("\n", " ") for k, v in parse_fields(i.get("body")).items()}
        rows.append({"id": i["number"], "title": re.sub(r"^\[Strategy\]\s*", "", i["title"]).replace("|", "/"),
                     "stage": first(labels, "stage:") or "1-submitted", "evidence": first(labels, "evidence:") or "L0-claim",
                     "verdict": first(labels, "verdict:"), "submitted_by": f.get("Submitted by", ""),
                     "market": f.get("Market", ""), "gemini": "yes" if "gemini-reviewed" in labels else "",
                     "comments": i.get("comments", 0), "state": i.get("state", ""),
                     "created": (i.get("created_at") or "")[:10], "updated": (i.get("updated_at") or "")[:10],
                     "url": i.get("html_url", "")})
    rows.sort(key=lambda r: r["id"])
    os.makedirs(LAB, exist_ok=True)
    with open(os.path.join(LAB, "strategies.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["id"])
        w.writeheader()
        w.writerows(rows)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    L = ["# Strategy database", "",
         f"Rebuilt from GitHub Issues {now}. {len(rows)} strategies. Lab rules: [lab/README.md](README.md).",
         "", "**No strategy is trusted because a trader claims it works. Only evidence level L3 (forward paper test) counts.**", ""]
    by_stage = {s.split(":", 1)[1]: [] for s in STAGE_ORDER}
    for r in rows:
        by_stage.setdefault(r["stage"], []).append(r)
    for stage, items in by_stage.items():
        L += [f"## {stage} ({len(items)})", ""]
        if not items:
            L += ["_none_", ""]
            continue
        L += ["| # | Strategy | Market | Evidence | Verdict | Submitted by | Gemini | Comments |", "|---|---|---|---|---|---|---|---|"]
        for r in items:
            L.append(f"| [#{r['id']}]({r['url']}) | {r['title']} | {r['market']} | {r['evidence']} | {r['verdict'] or '-'} | "
                     f"{r['submitted_by']} | {r['gemini'] or '-'} | {r['comments']} |")
        L.append("")
    with open(os.path.join(LAB, "DATABASE.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    return rows


def main():
    if not TOKEN:
        print("lab: no GITHUB_TOKEN - nothing to do")
        return
    gh = GH(TOKEN, REPO)
    print(f"lab: labels created {ensure_labels(gh)}")
    issues = gh.all_issues()
    n = seed(gh, issues)
    if n:
        print(f"lab: seeded {n} strategies")
        issues = gh.all_issues()
    r = gemini_review(gh, issues)
    if r:
        print(f"lab: Gemini reviewed {r}")
        issues = gh.all_issues()
    rows = build_db(issues)
    print(f"lab: database rebuilt ({len(rows)} strategies)")


if __name__ == "__main__":
    main()
