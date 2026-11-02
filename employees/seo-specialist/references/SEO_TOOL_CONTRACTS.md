# Контракты инструментов и контроль доступа

| Инструмент | Для чего | Вход/выход | Контроль |
|---|---|---|---|
| Yandex Wordstat / API | фразы, регион, история частот | keyword_raw + frequency metadata | тип частоты, дата, гео, лимиты, дедуп |
| SERP API (XMLRiver и аналоги) | Google/Yandex snapshots | query geo device engine → raw SERP+parsed results | 429/капча/неполная выдача, дата и локаль |
| Crawler (Screaming Frog/Sitebulb/собственный) | URL, status, canonical, links | crawl.csv | robots, rate limits, JS parity |
| Firecrawl/Scrapfly | рендер/извлечение | HTML + extracted text | paywall, bot blocks, page content validation |
| GSC | queries / pages / index | date-range report | sampling/anonymization, timezone |
| Яндекс Вебмастер | search queries, indexing | segments | регион/устройство/индекс |
| GA4/Метрика/CRM | сделки, качество трафика | events/leads | privacy, attribution, dedup |
| Ahrefs/Semrush/Keys.so | ссылки, конкуренты, спрос | datasets | estimates ≠ observed reality |
| GitHub | изменять шаблоны, тексты, skills | commits/PR | only permitted repositories, branch protection |
| CMS/WordPress | публиковать утверждённые страницы | draft/publish response | approval, backup, rendering, rollback |

**Требования к хранению:** ключи только в секретах/`.env`, исключить из логов и git, не выкладывать в чат; перед работой проверить действительность и доступ. Если API недоступен — составь план и отметь `BLOCKED`, не симулируй данные.
