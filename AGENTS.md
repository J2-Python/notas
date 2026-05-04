# AGENTS.md

This repository is a small Django + Django REST Framework project.
Use this file as the default operating guide for coding agents in this repo.

## Scope
- Applies to the full repo rooted at `/Users/jota/Sites/python/curso-drf/notas`.
- Main Django entry point: `drfNotas/manage.py`.
- Django apps live under `drfNotas/applications/`.
- Project settings live under `drfNotas/drfNotas/settings/`.

## Repo Instruction Files
- No prior `AGENTS.md` existed when this file was created.
- No `.cursor/rules/` directory was present.
- No `.cursorrules` file was present.
- No `.github/copilot-instructions.md` file was present.

## Environment Notes
- A local virtualenv exists at `.venv/`.
- Local dependencies are pinned in `requirements/local.txt`.
- `manage.py` defaults to `drfNotas.settings.local`.
- `drfNotas/drfNotas/settings/base.py` reads `secrets.json` via a relative path.
- Because of that, run Django management commands with working directory `drfNotas/`.
- Local settings expect Postgres credentials from `drfNotas/secrets.json`.
- Do not print, copy, or commit secrets from `drfNotas/secrets.json`.

## Project Layout
- `drfNotas/applications/notas/`: notes app.
- `drfNotas/applications/users/`: user app.
- `drfNotas/drfNotas/settings/base.py`: shared settings.
- `drfNotas/drfNotas/settings/local.py`: local Postgres settings.
- `drfNotas/drfNotas/settings/prod.py`: present but currently empty.
- `COMANDOS.md`: basic setup notes for Django, DRF, and Postgres.

## Setup And Validation Commands
- Create venv: `python3 -m venv .venv`
- Activate venv: `. .venv/bin/activate`
- Install deps: `pip install -r requirements/local.txt`
- Start dev server: `.venv/bin/python manage.py runserver`
- Django system check: `.venv/bin/python manage.py check`
- Create migrations: `.venv/bin/python manage.py makemigrations`
- Verify no missing migrations: `.venv/bin/python manage.py makemigrations --check --dry-run`
- Apply migrations: `.venv/bin/python manage.py migrate`
- Open shell: `.venv/bin/python manage.py shell`
- Create superuser: `.venv/bin/python manage.py createsuperuser`

## Test Commands
- Test runner: Django built-in `manage.py test`.
- No `pytest`, `tox`, or coverage config was found.
- Run all tests: `.venv/bin/python manage.py test`
- Run one app: `.venv/bin/python manage.py test applications.notas`
- Run one module: `.venv/bin/python manage.py test applications.notas.tests`
- Run one `TestCase`: `.venv/bin/python manage.py test applications.notas.tests.NotaTests`
- Run one test method: `.venv/bin/python manage.py test applications.notas.tests.NotaTests.test_example`
- Filter by substring: `.venv/bin/python manage.py test -k nota`
- Stop on first failure: `.venv/bin/python manage.py test --failfast`
- Reuse test DB: `.venv/bin/python manage.py test --keepdb`
- Verbose output: `.venv/bin/python manage.py test -v 2`

## Lint And Format Commands
- No Ruff, Black, isort, Flake8, or mypy config was found.
- Do not introduce repo-wide tooling unless the user asks for it.
- Use `manage.py check` as the baseline validation command.
- Use `manage.py makemigrations --check --dry-run` after model changes.
- Optional syntax sweep: `.venv/bin/python -m compileall applications drfNotas`

## Working Agreements
- Keep changes tightly scoped to the request.
- Prefer small, reviewable diffs over broad cleanup.
- Preserve the current app and package layout.
- Do not rename settings modules or package roots without explicit instruction.
- Do not commit secrets, credentials, or local-only config.
- Do not assume `prod.py` is ready for deployment.

## Code Style
This codebase mixes generated Django scaffolding with early manual edits.
When touching code, improve local consistency without performing unrelated rewrites.

### Imports
- Group imports as standard library, third-party/Django, then local imports.
- Separate import groups with one blank line.
- Prefer one import per line.
- Avoid duplicate imports.
- Prefer absolute imports across apps.
- Use wildcard imports only for the existing settings split pattern like `from .base import *`.

### Formatting
- Use 4 spaces for indentation.
- Keep lines readable; target about 88 characters when practical.
- Leave blank lines between top-level classes and functions.
- Use trailing commas in multiline literals and call sites.
- Prefer single quotes unless double quotes read better.
- Remove dead commented-out code when editing nearby code.
- Keep inline comments rare and useful.

### Naming
- Use `snake_case` for functions, methods, variables, and module names.
- Use `PascalCase` for classes, models, serializers, forms, and test classes.
- Use `UPPER_SNAKE_CASE` for constants and setting names.
- Keep model class names singular, for example `Nota`.
- Name booleans with explicit prefixes like `is_`, `has_`, or `can_`.
- Prefer English names unless a Spanish domain term is already established.

### Types
- The current codebase is largely untyped.
- Add type hints for new non-trivial helper functions when they help clarity.
- Do not do annotation-only refactors across untouched files.
- Annotate service-style functions and utilities before annotating simple Django boilerplate.
- Keep ORM and model code idiomatic rather than forcing awkward typing patterns.

### Django Conventions
- Keep each app under `drfNotas/applications/<app_name>/`.
- Register new apps in `LOCAL_APPS` in `drfNotas/drfNotas/settings/base.py`.
- Put schema changes in migrations created in the same change as the model edits.
- Keep routing in URL modules, not embedded string constants in views.
- Keep reusable business logic in models, managers, or services, not in thin wrappers.
- If adding DRF endpoints, keep serializers, views, and URLs explicit and predictable.
- Prefer class-based abstractions only when they clearly reduce repetition.

### Models
- Be explicit with field options such as `blank`, `null`, `default`, `unique`, and `db_index`.
- Add `Meta` only when it provides real behavior.
- Keep `__str__()` short and stable.
- Prefer model constraints and validation over scattered ad hoc checks.
- Always update migrations with schema changes.

### Views And API Code
- Keep views thin and boundary-focused.
- Validate request data close to the entry point.
- Return standard Django or DRF response types.
- Avoid hidden side effects in GET handlers.
- Keep auth and permission behavior explicit.

### Error Handling
- Raise specific exceptions; do not use bare `except`.
- If touching `get_secret`, catch `KeyError` instead of swallowing every exception.
- Use Django exceptions like `ImproperlyConfigured` and `ValidationError` when appropriate.
- Fail fast for missing configuration.
- Make error messages actionable and name the missing setting or invalid field.
- Do not silence ORM or validation errors unless replacing them with a clearer domain error.

### Tests
- Add or update tests for non-trivial behavior changes.
- Keep tests near the app they cover.
- Use descriptive test names that state the expected behavior.
- Prefer one main behavior per test.
- Use Django `TestCase` for database-backed tests unless a lighter option is enough.

### Security And Config
- Never hardcode secrets in source files.
- Never commit `secrets.json` changes unless explicitly requested.
- Assume local development uses Postgres from `local.py`.
- Be careful with auth work: a custom `User` model exists, but `AUTH_USER_MODEL` is not configured yet.
- Verify auth assumptions before building features on top of the custom user model.

## Practical Repo Notes
- `views.py` and `tests.py` in both apps are still starter placeholders.
- `applications/users/manager.py` exists but is empty.
- `applications/notas/admin.py` currently has a duplicate import; do not copy that pattern.
- `asgi.py` and `wsgi.py` still point to `drfNotas.settings`; verify them before relying on those entry points.

## Minimal Pre-Handoff Checklist
- Run `manage.py check` after meaningful Django changes.
- Run `manage.py makemigrations --check --dry-run` after model changes.
- Run the smallest relevant test scope first.
- Call out any commands you could not run because local Postgres or secrets were unavailable.
