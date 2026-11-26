# Контракты артефактов
CSV UTF-8, первая строка — заголовки; UNKNOWN для отсутствующих значений, не ноль. ISO 8601 для дат. Сырые данные не перезаписывать.
- keywords_raw/clean.csv: query, engine, region, device, frequency, frequency_type, source, measured_at
- clusters.csv: cluster_id, query, intent, evidence, confidence
- url_map.csv: cluster_id, url, action, reason, evidence
- baseline.csv: url, engine, period_start, period_end, impressions, clicks, leads, source
- technical_issues.csv: url, issue, observed, severity, action, verification, status
- serp_quality.csv: query, source, measured_at, status, reason
- changes.csv: url, change, approved_by, date, rollback, status
- experiments.csv: test_id, hypothesis, primary_metric, treatment, holdout, stopping_rule, status
- serp_snapshots.jsonl: query, engine, region, device, timestamp, provider, top_urls, parse_status
- qa_report.md: scope, observed evidence, checks PASS/FAIL/BLOCKED, remaining risks, approval
- kpi_report.md: baseline, period, segmentation, changes, confounders, observed result, next step
- decisions.md: observed, alternatives, decision, confidence, evidence, owner
For page specifications and experiments use the corresponding assets. Store working artifacts in the user-approved workspace, not the installed skill folder.
