---
name: git-safe-push
description: Safely commit and push selected files to GitHub without accidentally committing unrelated or sensitive files.
---

# Git Safe Push

Use this skill when the user wants to commit and push only selected files.

## Workflow

1. Check repository status:

   git status

2. Never use:

   git add .

   unless the user explicitly wants every changed file.

3. Stage only requested files:

   git add path/to/file.py

4. Verify staged files:

   git diff --cached --name-only

5. Commit:

   git commit -m "descriptive commit message"

6. Check current branch:

   git branch --show-current

7. Push:

   git push origin <branch>

## Safety checks

- Do not commit .env files.
- Do not commit passwords or API keys.
- Do not commit unrelated files.
- Always inspect staged files before commit.