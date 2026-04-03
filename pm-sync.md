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
- Status: done
- Commits: daa7f7d

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
- Status: done

1. Запустить `mkdocs build --strict` — 0 ошибок, 0 warnings
2. Запустить `mkdocs serve` и пройтись по всем страницам
3. Написать статус в pm-sync

---

# Round 3 — API Reference без Swagger UI

Ревьюер обновил данные на Home и Rate Limits (коммит 1d33a12 — 10M+ req/day, $0.0006/req).

## Task 16: Заменить Swagger UI на neoteroi-mkdocs OpenAPI renderer

**Проблема:** Swagger UI на страницах API Reference выглядит как врезанная чужая страница — кнопка Authorize, Servers dropdown, Models/Schemas секция. Ни один крупный API-продукт (Stripe, Twilio, OpenAI) так не делает. Нужен чистый нативный рендер эндпоинтов в стиле Material theme.

**Решение:** Плагин `neoteroi-mkdocs` (`mkdocsoad`) — читает OpenAPI JSON и рендерит нативный Markdown с бейджами методов, таблицами параметров, collapsible секциями request/response.

**Что сделать:**

1. Установить зависимость:
```bash
uv pip install neoteroi-mkdocs
```

2. Добавить в `docs/requirements.txt`:
```
mkdocs-material>=9.5
mkdocs-swagger-ui-tag>=0.6
neoteroi-mkdocs>=1.2.0
```

3. В `mkdocs.yml` добавить plugin:
```yaml
plugins:
  - search
  - neoteroi.mkdocsoad
```

4. В `mkdocs.yml` добавить CSS для neoteroi (в `extra_css`):
```yaml
extra_css:
  - overrides/extra.css
  - css/neoteroi-mkdocs.css
```

5. Скопировать CSS neoteroi для кастомизации:
```bash
# Найти файл:
python3 -c "import neoteroi.mkdocsoad; import os; print(os.path.dirname(neoteroi.mkdocsoad.__file__))"
# Скопировать mkdocsoad.css в docs/css/neoteroi-mkdocs.css
# Или создать docs/css/neoteroi-mkdocs.css с нужными стилями
```

Если CSS файл не находится автоматически — создать `docs/css/neoteroi-mkdocs.css` и подключить. Документация: https://www.neoteroi.dev/mkdocs-plugins/web/oad/

6. Обновить `docs/api-reference/rest-v1.md`:
```markdown
# REST API v1

Mobile API endpoints for anonymous Instagram data retrieval. v1 endpoints return raw Instagram data structures with minimal transformation.

All endpoints use `GET` method and require the `x-access-key` header. See [Authentication](../getting-started/authentication.md).

## Endpoint groups

| Group | Description | Example |
|-------|-------------|---------|
| **User** | Profiles, followers, following, search | `/v1/user/by/username` |
| **Media** | Posts, reels, likes, comments | `/v1/media/by/code` |
| **Stories** | User stories and story items | `/v1/user/stories` |
| **Highlights** | Story highlights and covers | `/v1/user/highlights` |
| **Hashtags** | Hashtag info and recent media | `/v1/hashtag/by/name` |
| **Locations** | Location info and media | `/v1/location/by/id` |
| **Search** | Global search across users, hashtags, locations | `/v1/search` |

## All v1 endpoints (72)

[OAD(../openapi-v1.json)]

---

**Ready to integrate?** [Get your API key →](https://hikerapi.com/p/hybef5jn){ target=_blank }
```

7. Аналогично обновить `docs/api-reference/rest-v2.md` — заменить `<swagger-ui .../>` на `[OAD(../openapi-v2.json)]`

8. Аналогично обновить `docs/api-reference/graphql.md` — заменить `<swagger-ui .../>` на `[OAD(../openapi-gql.json)]`. Оставить пример с табами curl/Python выше OAD.

9. После замены всех Swagger UI — можно удалить `mkdocs-swagger-ui-tag` из зависимостей и плагинов в mkdocs.yml (но только после проверки что OAD работает!).

10. Запустить `mkdocs serve` и проверить:
    - Эндпоинты рендерятся нативно в стиле Material
    - Бейджи методов (GET зелёный)
    - Параметры в таблицах
    - Нет Swagger UI элементов (Authorize, Servers, Models)
    - Dark mode работает

11. Коммит: `feat: replace Swagger UI with neoteroi OpenAPI renderer`

**Важно:** Если `neoteroi-mkdocs` не устраивает визуально или есть проблемы — НЕ коммитить, написать в pm-sync что именно не так. Мы рассмотрим альтернативы.

- Status: done
- Commits: 73cdabc
- Notes: neoteroi.mkdocsoad рендерит эндпоинты нативно. swagger-ui-tag удалён из plugins и requirements. CSS инжектится автоматически (нет отдельного файла). Build strict — 0 warnings.

## Task 17: Final build verification Round 3
- Status: done

1. `mkdocs build --strict` — 0 ошибок
2. `mkdocs serve` — пройтись по v1, v2, gql страницам
3. Проверить dark/light mode
4. Написать статус в pm-sync

---

# Round 4 — API Reference по ресурсам (как Stripe/OpenAI)

**Контекст:** Ревьюер сравнил нашу доку с Stripe и OpenAI API Reference. У топов:
- Каждый ресурс (User, Media, Chat) — **отдельная страница** с 3-10 эндпоинтами
- Sidebar навигация по ресурсам
- Нет огромного списка всех эндпоинтов на одной странице
- Нет APIKeyHeader в параметрах (auth описана отдельно)
- Response — реальный пример JSON, не schema с null

## Task 18: Разбить API Reference на страницы по ресурсам

**Проблема:** 72 v1 эндпоинта на одной странице — юзер скроллит 5 минут. APIKeyHeader в каждом эндпоинте. Schema ответа с null бесполезна.

**Что сделать:**

### 18.1 Доработать `scripts/split_openapi.py`

Добавить возможность разбивать spec не только по версии (v1/v2/gql), но и по **тегу/ресурсу**. Скрипт должен создавать:

Для v1:
- `docs/openapi/v1-user.json` — пути `/v1/user/*` + `/v1/user*`
- `docs/openapi/v1-media.json` — пути `/v1/media/*`
- `docs/openapi/v1-story.json` — пути `/v1/story/*` + `/v1/user/stories*`
- `docs/openapi/v1-highlight.json` — пути `/v1/highlight/*` + `/v1/user/highlights*`
- `docs/openapi/v1-hashtag.json` — пути `/v1/hashtag/*`
- `docs/openapi/v1-location.json` — пути `/v1/location/*`
- `docs/openapi/v1-search.json` — пути `/v1/search/*` + `/v1/fbsearch/*` + `/v1/share/*`

Для v2 — аналогичная структура по тегам.
Для gql — можно оставить одной страницей (22 эндпоинта — нормально).

**Важно:** В каждом spec-файле:
1. **Убрать параметр APIKeyHeader** из всех эндпоинтов (это security scheme, а не query param). Фильтр: удалить из `parameters` любой параметр где `name == "APIKeyHeader"` и `in == "header"`.
2. **Убрать response schemas** (свойство `responses.200.content.application/json.schema`) — заменить на пустой объект `{}` или удалить. Мы добавим реальные примеры позже, отдельной задачей.
3. Убрать из `info` блока поля `termsOfService`, `license`, `x-logo` — они рендерятся как мусор на странице.
4. Убрать секцию `servers` — у нас один сервер, он уже описан в Authentication.
5. Убрать секцию `components` если она не нужна после удаления response schemas.

### 18.2 Создать страницы для v1 ресурсов

Создать директорию `docs/api-reference/v1/` с файлами:

**`docs/api-reference/v1/index.md`** — обзорная страница:
```markdown
# REST API v1

Mobile API endpoints for anonymous Instagram data retrieval.

All endpoints use `GET` method and require the `x-access-key` header. See [Authentication](../../getting-started/authentication.md).

| Resource | Description | Endpoints |
|----------|-------------|-----------|
| [User](user.md) | Profiles, followers, following | 16 |
| [Media](media.md) | Posts, reels, likes, comments | 8 |
| [Stories](stories.md) | User stories | 4 |
| [Highlights](highlights.md) | Story highlights | 4 |
| [Hashtags](hashtags.md) | Hashtag info and media | 6 |
| [Locations](locations.md) | Location info and media | 4 |
| [Search](search.md) | Search users, hashtags, places | 6 |
```

**`docs/api-reference/v1/user.md`:**
```markdown
# User Endpoints

Get user profiles, followers, following lists, and search within followers.

[OAD(../../openapi/v1-user.json)]

---

**Ready to integrate?** [Get your API key →](https://hikerapi.com/p/hybef5jn){ target=_blank }
```

Аналогично для media.md, stories.md, highlights.md, hashtags.md, locations.md, search.md.

### 18.3 Аналогично для v2

Создать `docs/api-reference/v2/` с тем же подходом. Файлы по ресурсам.

### 18.4 GraphQL — оставить одной страницей

22 эндпоинта — нормально. Но тоже убрать APIKeyHeader и response schemas.

### 18.5 Обновить nav в mkdocs.yml

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - Quick Start: getting-started/quick-start.md
    - Authentication: getting-started/authentication.md
  - API Reference:
    - v1 Overview: api-reference/v1/index.md
    - v1 User: api-reference/v1/user.md
    - v1 Media: api-reference/v1/media.md
    - v1 Stories: api-reference/v1/stories.md
    - v1 Highlights: api-reference/v1/highlights.md
    - v1 Hashtags: api-reference/v1/hashtags.md
    - v1 Locations: api-reference/v1/locations.md
    - v1 Search: api-reference/v1/search.md
    - v2 Overview: api-reference/v2/index.md
    - v2 User: api-reference/v2/user.md
    - v2 Media: api-reference/v2/media.md
    - v2 Search: api-reference/v2/search.md
    - GraphQL API: api-reference/graphql.md
    - Response Codes: api-reference/response-codes.md
  - SDKs:
    - Python: sdk/python.md
    - JavaScript: sdk/javascript.md
    - Go: sdk/go.md
    - PHP: sdk/php.md
  - Guides:
    - Rate Limits: guides/rate-limits.md
    - Request Costs: guides/request-costs.md
  - Support:
    - Contacts: support/contacts.md
```

### 18.6 Удалить старые файлы

```bash
rm -f docs/openapi-v1.json docs/openapi-v2.json docs/openapi-gql.json
rm -f docs/api-reference/rest-v1.md docs/api-reference/rest-v2.md
```
Оставить docs/openapi.json (исходник) и docs/api-reference/graphql.md (обновлённый) и docs/api-reference/response-codes.md.

### 18.7 Verify + Commit

```bash
mkdocs build --strict
mkdocs serve
```

Проверить:
- Sidebar: каждый ресурс отдельно (как у Stripe)
- На странице User — только user эндпоинты (не 72)
- Нет APIKeyHeader в параметрах
- Нет response schema с null
- Нет Servers / Terms of Service / License секций

Коммит: `feat: split API Reference into per-resource pages (Stripe-style)`

- Status: done
- Commits: d46a866
- Notes: v1: 7 ресурсных страниц (user/media/stories/highlights/hashtags/locations/search), v2: 8 страниц (+track). Cleaned specs: no APIKeyHeader, no response schemas, no servers/license. 28 pages total. Strict build 0 warnings. Обновлены ссылки в index/quick-start/sdk pages.

## Task 19: Final verification Round 4
- Status: done

1. `mkdocs build --strict`
2. `mkdocs serve` — пройтись по всем страницам ресурсов
3. Проверить навигацию sidebar
4. Написать статус в pm-sync

---

# Round 5 — Чистка рендера эндпоинтов

Ревьюер нашёл 4 проблемы после сравнения со Stripe/OpenAI:

## Task 20: Почистить OpenAPI spec-файлы и рендер

**Проблема 1: "HikerAPI REST 1.7.7 / Instagram API"** — мусор из info блока рендерится вверху каждой страницы ресурса.

**Проблема 2: Пустые response schema** — "Response 200 OK / Schema of the response body" с пустым серым блоком. Бесполезно и выглядит как баг.

**Проблема 3: Response 404, 422** — рендерятся с пустыми блоками. Шум.

**Проблема 4: Нет краткого описания ответа** — у Stripe/OpenAI каждый эндпоинт говорит что возвращает: "Returns a User object", "Returns a list of Media objects". У нас — ничего.

**Что сделать в `scripts/split_openapi.py`:**

1. **Минимизировать `info` блок** — поставить пустые значения:
```python
spec["info"] = {"title": "", "version": ""}
```

2. **Убрать `responses` полностью из каждого path** — это избавит от пустых schema блоков и 404/422:
```python
for path_data in spec["paths"].values():
    for method_data in path_data.values():
        if "responses" in method_data:
            del method_data["responses"]
```

3. **Добавить краткое описание ответа в `description`** каждого эндпоинта. Маппинг по паттерну пути:

| Path pattern | Append to description |
|---|---|
| `/user/by/username` | Returns a User object. |
| `/user/by/id` | Returns a User object. |
| `/user/followers*` | Returns a list of User objects and pagination cursor. |
| `/user/following*` | Returns a list of User objects and pagination cursor. |
| `/user/medias*` | Returns a list of Media objects and pagination cursor. |
| `/user/clips*` | Returns a list of Media objects (Reels) and pagination cursor. |
| `/user/stories*` | Returns a list of Story objects. |
| `/user/highlights*` | Returns a list of Highlight objects. |
| `/media/by/*` | Returns a Media object. |
| `/media/comments*` | Returns a list of Comment objects and pagination cursor. |
| `/media/likers*` | Returns a list of User objects. |
| `/hashtag/by/*` | Returns a Hashtag object. |
| `/hashtag/medias*` | Returns a list of Media objects and pagination cursor. |
| `/location/medias*` | Returns a list of Media objects and pagination cursor. |
| `/search/*`, `/fbsearch/*` | Returns a list of matching results. |
| `/share/*` | Returns shared content data. |
| `*chunk*` | Returns paginated results with end_cursor. |

Если у эндпоинта уже есть description — добавить в конец через ` `. Если нет — поставить.

4. **Убрать `components`** из каждого spec-файла (больше не нужен без response schemas):
```python
if "components" in spec:
    del spec["components"]
```

5. Перегенерировать все spec-файлы: `python3 scripts/split_openapi.py`

6. **Verify:**
- `mkdocs build --strict`
- `mkdocs serve` — проверить:
  - НЕТ "HikerAPI REST 1.7.7" заголовка
  - НЕТ пустых response блоков
  - НЕТ Response 404/422
  - ЕСТЬ краткое описание что возвращает эндпоинт
  - Sidebar ресурсов работает

7. Коммит: `fix: clean OpenAPI render — remove empty schemas, add response descriptions`

**Отпиши статус в pm-sync. Ревьюер проверит и если что-то не так — будет ещё итерация.**

- Status: done
- Commits: bd4233d
- Notes: info минимизирован (пустой title/version), responses удалены полностью (нет пустых schema/404/422), security убран, return descriptions добавлены по паттерну пути (16+ endpoints с "Returns a ..."). Strict build 0 warnings.
