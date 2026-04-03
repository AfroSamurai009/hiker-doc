# PM Sync Log

Файл для синхронизации между агентом-исполнителем и ревьюером.

**Формат записи:**
```
## Task N: название
- Status: in_progress / done / blocked
- Commits: <hash>
- Notes: что сделано, проблемы, вопросы
```

---

## Task 1: MkDocs Material setup + base config
- Status: done
- Commits: c9624ce
- Notes: mkdocs.yml, requirements.txt, .readthedocs.yaml, docs/index.md, docs/overrides/ — build OK

## Task 2: Home page with CTA
- Status: done
- Commits: 6e8a77b
- Notes: Grid cards, trust signals table, CTA box with custom CSS, dark mode support

## Task 3: Announcement bar
- Status: done
- Commits: 6fc5348
- Notes: Dismissible banner with free trial CTA on all pages

## Task 4: Getting Started pages
- Status: done
- Commits: 1d84ab5
- Notes: Quick Start (5-step guide, 4 language tabs) + Authentication page

## Task 5: API Reference — OpenAPI render
- Status: done
- Commits: 6dcd1c9
- Notes: 147 paths from openapi.json, REST v1/v2, GraphQL, Response Codes pages with Swagger UI

## Task 6: Guides — Rate Limits and Request Costs
- Status: done
- Commits: e101573
- Notes: Rate limits with async example, request costs with force mode tabs

## Task 7: SDK guide pages
- Status: done
- Commits: 76895ce
- Notes: Python, JavaScript, Go, PHP — quick start + pagination examples

## Task 8: Support page
- Status: done
- Commits: 91d0c20
- Notes: Contacts with email + Telegram, feature requests, full nav complete

## Task 9: Cleanup — remove old Sphinx files
- Status: done (partial)
- Commits: 30778e5
- Notes: Added exclude_docs for superpowers/. Strict build passes. Old Sphinx files NOT removed — user denied rm permission. Need manual: `rm -rf docs/source/ docs/hikerapi/ docs/build/ docs/Makefile docs/make.bat Makefile Makefile.bak`

## Task 10: Final verification
- Status: done
- Commits: (no changes needed)
- Notes: `mkdocs build --strict` passes with 0 errors/warnings. 16 pages generated. Swagger UI on 3 API pages. Announcement bar + CTA box confirmed in HTML output.

---

# Round 2 — Полировка (после ревью)

Ревьюер починил иконки на Home (коммит 8dd46f1 — добавил `pymdownx.emoji` extension + `--unsafe` в pre-commit check-yaml).

Сервер: `.venv/bin/mkdocs serve -a localhost:8002`

## Task 11: API Reference — разделить openapi.json по версиям

**Проблема:** Сейчас на всех трёх API-страницах (v1, v2, gql) вставлен один и тот же полный Swagger UI со ВСЕМИ эндпоинтами. Выглядит как врезанная страничка, а не документация.

**Что сделать:**

1. Написать скрипт `scripts/split_openapi.py` — читает `docs/openapi.json`, создаёт отдельные файлы:
   - `docs/openapi-v1.json` — только пути `/v1/*` (72 эндпоинта)
   - `docs/openapi-v2.json` — только `/v2/*` + `/v3/*` + `/a2/*` (52 эндпоинта)
   - `docs/openapi-gql.json` — только `/gql/*` + `/g2/*` (22 эндпоинта)
   - Каждый файл — полноценный OpenAPI spec (с info, components, servers), но только свои paths

2. Обновить `docs/api-reference/rest-v1.md`:
   - Убрать текущий `<swagger-ui src="../openapi.json" .../>`
   - Добавить вступительное описание (какие данные, для чего)
   - Описать группы эндпоинтов: User, Media, Stories, Highlights, Hashtags, Locations, Search
   - В конце — `<swagger-ui src="../openapi-v1.json" docExpansion="list" filter="true"/>`
   - CTA внизу: "Ready to integrate? Get your API key →"

3. Обновить `docs/api-reference/rest-v2.md`:
   - Аналогично, но с описанием отличий v2 от v1 (пагинация через `next_page_id`, расширенные данные)
   - `<swagger-ui src="../openapi-v2.json" .../>`

4. Обновить `docs/api-reference/graphql.md`:
   - Описать cursor-based pagination, формат ответов
   - Оставить пример с комментариями (с табами)
   - `<swagger-ui src="../openapi-gql.json" .../>`

5. Коммит: `fix: split OpenAPI spec per API version for cleaner reference pages`

- Status: done
- Commits: e871aa9
- Notes: scripts/split_openapi.py создан. 3 spec-файла: v1(72), v2(52), gql(22). Все 3 страницы обновлены с описаниями групп.

## Task 12: Home — stat-карточки вместо таблицы "Why HikerAPI?"
- Status: done
- Commits: 97f3666

**Проблема:** Таблица "Why HikerAPI?" — обычная markdown-таблица на ~40% ширины. Данные мощные (10K+ devs, 4-5M req/day), но выглядит скромно.

**Что сделать:**

1. В `docs/index.md` заменить секцию "Why HikerAPI?" — вместо таблицы сделать grid с stat-карточками:
```markdown
<div class="grid cards" markdown>

-   **10,000+**{ .stat-number }

    developers worldwide

-   **147**{ .stat-number }

    API endpoints

-   **4-5M**{ .stat-number }

    requests per day

-   **$0.001**{ .stat-number }

    per request

</div>
```

2. В `docs/overrides/extra.css` добавить стили для `.stat-number`:
```css
.stat-number {
  display: block;
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--md-primary-fg-color);
  line-height: 1.2;
}
```

3. Убрать карточку Pricing из верхнего grid (перенесена в stat-числа) — оставить 3 карточки в один ряд: Quick Start, API Reference, SDKs

4. Коммит: `feat: replace Why HikerAPI table with stat cards`

## Task 13: Home — layout polish
- Status: done
- Commits: 741ffab

**Что сделать:**

1. Между stat-карточками и CTA-блоком добавить code snippet preview:
```markdown
## See it in action

\`\`\`bash
curl -H "x-access-key: YOUR_TOKEN" \
  "https://api.hikerapi.com/v1/user/by/username?username=ronaldo"
\`\`\`

\`\`\`json
{"pk": "173560420", "username": "ronaldo", "full_name": "Cristiano Ronaldo",
 "is_verified": true, "follower_count": 612000000, ...}
\`\`\`
```

2. Коммит: `feat: add code snippet preview on home page`

## Task 14: Navigation polish — breadcrumbs + footer

**Что сделать:**

1. В `mkdocs.yml` в `theme.features` добавить:
   - `navigation.path` (включает breadcrumbs)

2. В `mkdocs.yml` в `extra` добавить footer ссылки:
```yaml
extra:
  social:
    - icon: fontawesome/brands/telegram
      link: https://t.me/hikerapi
    - icon: fontawesome/brands/python
      link: https://pypi.org/project/hikerapi/
    - icon: material/web
      link: https://hikerapi.com
  generator: false
```

3. В `docs/overrides/main.html` добавить блок footer с ссылками (Terms, Privacy, Status):
```html
{% block content %}
  {{ super() }}
{% endblock %}
```
Нет — лучше просто через `extra` в mkdocs.yml, footer links Material поддерживает.

4. Коммит: `feat: add breadcrumbs and footer links`

## Task 15: Final build verification

1. Запустить `mkdocs build --strict` — 0 ошибок, 0 warnings
2. Запустить `mkdocs serve` и пройтись по всем страницам
3. Написать статус в pm-sync
