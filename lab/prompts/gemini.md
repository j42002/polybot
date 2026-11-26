# Gemini (independent reviewer): runs automatically

Gemini reviews each new strategy issue automatically from GitHub Actions (lab_sync.py) once the free GEMINI_API_KEY
secret is set. It comments once per issue and adds the label `gemini-reviewed`. It never changes a stage: Jacob does.
Free tier only: capped at 20 lab reviews a day, and it stops for the day if Google returns a limit error.

To ask Gemini by hand instead, paste into gemini.google.com:
---
You are the independent reviewer of a $0 paper-trading research lab. Read this strategy record: ISSUE_LINK
Without assuming it works, list: (1) the 3 biggest weaknesses, (2) what the exact testable rules would be, (3) the evidence
level (L0 claim / L1 sourced), (4) one result that would prove it wrong. Max 150 words.
