# Copilot / AI Agent Project Instructions

Concise, project-specific guidance so an AI can contribute effectively. Keep this file lean (~50 lines) and updated when conventions change.

## 1. Project Snapshot
Modern, minimal Python package + CLI (Click) managed by Poetry 2 (>=2.0.0). Strict quality gate: formatting (black+isort), lint (flake8), typing (mypy strict), tests (pytest+coverage). CI matrix (3.9–3.12) plus build/release/publish stages.

## 2. Code & Architecture
- Source lives in `src/super_octo_bassoon/`; tests mirror structure in `tests/`.
- Public API exported via `src/super_octo_bassoon/__init__.py` (`__all__`). Add new user-facing functions there.
- Core logic separated from CLI wrapper (`hello.py` vs `cli.py`). Follow this separation: put pure logic in its own module, keep Click wiring thin.
- Version source of truth: `__init__.__version__` AND `[tool.poetry] version` in `pyproject.toml` must stay in sync.
- Behavior nuance: `hello_world(None)` -> "Hello, World!" but `hello_world("")` -> "Hello, !" (empty retained). Preserve unless explicitly changed with matching test update.

## 3. CLI Pattern (Click)
- Entry point declared in `pyproject.toml` `[tool.poetry.scripts] hello = super_octo_bassoon.cli:main`.
- Add new CLI features by extending `cli.py` or introducing subcommands (consider refactor to `@click.group()` if >1 command). Keep options simple, validated, and pure logic delegated to non-CLI functions.

## 4. Testing & Quality
- Pytest config via `[tool.pytest.ini_options]` (strict markers/config, test discovery patterns). Name tests `test_*.py`.
- Add parametrized tests for edge cases; mirror existing style in `tests/test_hello.py` & `tests/test_cli.py`.
- Run locally: `poetry run pytest` or `make test`; coverage: `make test-cov`.
- Quality bundle: `make quality` (flake8 + format-check + mypy). Always pass before PR.
- Keep all new code fully type annotated (mypy strict flags enforced).

## 5. Build, Release, Versioning
- Common commands: `make install`, `make build`, `make clean`.
- Version bump helpers: `make release-patch|release-minor|release-major` (creates commit + tag; user must push tags manually per echo message).
- Manual alternative: `poetry version patch` then sync `__init__.__version__`.
- CI publishes to PyPI only on tagged pushes (`v*`). Ensure tag matches `pyproject` version.
- Poetry 2 enforced: if adding docs/scripts, do not assume legacy `1.x` behaviors (installer env vars unchanged here).

## 6. Tooling & Formatting
- Black line length = 88; isort profile = black. Do not hand-format differently.
- Pre-commit hooks defined in `.pre-commit-config.yaml`; install via `poetry run pre-commit install`.
- Add new dependencies with `poetry add <pkg>` (or `poetry add --group dev <pkg>` for tooling) and commit updated lockfile if present.

## 7. Docker & Dev Environment
- Multi-stage Dockerfile builds wheels then produces slim runtime (non-root `appuser`). Entrypoint invokes CLI module. If adding runtime deps, modify builder install step and rebuild.
- Dev container (`.devcontainer/`) assumed to run `poetry install --with dev`; rely on Make targets inside.

## 8. Contribution Conventions
- Maintain small, focused modules; avoid embedding logic directly in Click command bodies.
- Update or add tests alongside code changes (no untested public behavior).
- Keep messages & outputs stable; changing greeting formatting = breaking change.
- Prefer pure functions; side effects (I/O, env reads) isolated for testability.

## 9. Typical Extension Examples
- New utility: create `src/super_octo_bassoon/goodbye.py`, export in `__init__`, add tests in `tests/test_goodbye.py`.
- New CLI flag: implement logic in existing module (e.g., `hello.py`), parse flag in `cli.py`, add a CLI test using `CliRunner`.

## 10. What NOT To Do
- Don’t bypass Poetry (no raw `pip install` into project env).
- Don’t modify generated artifacts under `dist/`—rebuild instead.
- Don’t change version in only one location.

## 11. AI Agent Checklist (Pre-PR)
- [ ] Code + tests added / updated
- [ ] `make quality` passes
- [ ] Version sync if behavior change (else leave)
- [ ] Public API adjustments reflected in `__all__`
- [ ] Docstrings follow existing concise style

Questions or ambiguity: surface in PR description; keep this file updated if new conventions emerge.
