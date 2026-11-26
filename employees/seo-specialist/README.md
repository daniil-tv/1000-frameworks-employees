# SEO Specialist — AI employee
Version 2.1.0 candidate; professional performance not yet verified by comparative model evals.

Install by copying this entire folder into the platform's project skills directory (Claude Code: .claude/skills/seo-specialist; Codex: .agents/skills/seo-specialist). Restart or reload the client if required. Verify discovery with a small SEO task. Do not copy only SKILL.md.

Example: «Проверь canonical и robots для предоставленных URL. Не меняй сайт». For a full project supply assets/project_brief.yaml, data and approved tool access. Default is draft. No API credentials are included; connect tools using your platform configuration, restrict permissions, and never store secrets here. Without APIs the employee analyses supplied data and reports blocked checks.

Offline checks (Python 3.10+): from the skill directory run `python -m unittest discover -s scripts -p 'test_*.py'`. CLI: `python scripts/seo_checks.py dedupe input.csv`, `python scripts/seo_checks.py overlap input.json` (keys a,b containing URL arrays), `python scripts/seo_checks.py validate input.csv --required query,source`. Outputs JSON to stdout; no network or writes.

See evals/README.md, CHANGELOG.md. Review source permissions before redistributing third-party archive materials; no license grant for third-party content is implied.
