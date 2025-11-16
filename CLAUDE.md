# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a multilingual (Japanese/English) documentation site that gathers development insights and tips. The site is built using **Zensical** (by the creators of Material for MkDocs) and deployed to GitHub Pages. The project uses **uv** for fast, modern Python dependency management.

## Repository Structure

```text
dev-insights-tips/
├── docs/               # Documentation content organized by language
│   ├── en/            # English documentation
│   ├── ja/            # Japanese documentation (primary)
│   ├── assets/        # Shared images and resources
│   └── stylesheets/   # Custom CSS
├── ci/                # Python CI/automation scripts
├── scripts/           # Utility scripts
├── overrides/         # MkDocs Material theme overrides
├── site/              # Generated site (do not edit, auto-generated)
├── mkdocs.yml         # MkDocs configuration
└── pyproject.toml     # Poetry dependencies and tool config
```

## Development Setup

This project uses **uv** for dependency management. Python 3.10+ is required.

### Initial Setup

```bash
# Install dependencies (including dev dependencies)
uv sync --all-extras

# Set up pre-commit hooks (excludes site/ folder automatically)
uv run pre-commit install
uv run python ci/set_pre-commit-hooks_exclude.py
```

### Common Development Commands

```bash
# Serve documentation locally (with live reload)
uv run zensical serve

# Build documentation (clean build)
uv run zensical build --clean

# Deploy to GitHub Pages (manual - normally done via CI)
uv run zensical gh-deploy
```

### Taskipy Shortcuts

The project uses taskipy for common tasks (defined in pyproject.toml):

```bash
# Format Python code
uv run task black

# Lint Python code
uv run task flake8

# Sort imports
uv run task isort

# Type check
uv run task mypy

# Zensical commands
uv run task serve   # zensical serve
uv run task build   # zensical build
uv run task mkds    # zensical serve (legacy alias)
uv run task mkdb    # zensical build --clean (legacy alias)
uv run task mkddp   # zensical gh-deploy (legacy alias)
```

## Code Quality

### Pre-commit Hooks

The project uses extensive pre-commit hooks configured in `.pre-commit-config.yaml`:

- Code formatting: ruff, black
- Linting: ruff, flake8, mypy
- YAML/TOML validation
- Markdown linting (markdownlint)
- Shell script checking (shellcheck)
- GitHub Actions validation (check-jsonschema)

Important: The `site/` folder is automatically excluded from pre-commit hooks using `ci/set_pre-commit-hooks_exclude.py`.

### Python Tool Configuration

All Python linting tools are configured in `pyproject.toml`:

- **Target version**: Python 3.10
- **Ruff**: Line length tolerant (E501 ignored), import sorting enabled
- **Black**: py310 target
- **MyPy**: Strict mode with type checking for `ci/` and `scripts/`
- **Flake8**: Similar rules to ruff

## Zensical Architecture

### About Zensical

Zensical is a modern static site generator built by the creators of Material for MkDocs. Key advantages:

- **Backward compatible**: Can read `mkdocs.yml` configuration files
- **Modern stack**: Built with Rust and Python for better performance
- **Same philosophy**: Batteries included, easy to use, powerful customization
- **Native TOML support**: New projects can use `zensical.toml` (though `mkdocs.yml` remains supported)

### i18n (Internationalization)

The site uses `mkdocs-static-i18n` plugin with folder-based structure:

- **Primary language**: Japanese (ja)
- **Secondary language**: English (en)
- **Fallback**: Enabled (falls back to default if translation missing)

Each language has its own complete docs folder under `docs/en/` and `docs/ja/`.

### Key Plugins

- `zensical`: Modern static site generator (replaces mkdocs-material)
- `mkdocs-static-i18n`: Multilingual support
- `mkdocs-glightbox`: Image lightbox
- `plantuml-markdown`: PlantUML diagram support
- `tags`: Tag-based navigation

### Theme Features

Configured in `mkdocs.yml` (Zensical is backward compatible):

- Navigation indexes (section landing pages)
- Back-to-top button
- Code copy/select/annotate
- Google Analytics with feedback widget
- Cookie consent

## CI/CD

### GitHub Actions Workflows

All workflows now use **uv** for dependency management instead of Poetry.

1. **push_gh-deploy.yml**: Automatically builds and deploys to GitHub Pages
   - Triggers on: push to main (excluding `[skip ci]`), after other workflow completions
   - Uses `uv sync --all-extras` for dependency installation
   - Uses `uv run zensical gh-deploy` for deployment
   - Caches Zensical resources

2. **update_pre-commit_hooks.yml**: Keeps pre-commit hooks updated
   - Uses `uv run pre-commit autoupdate`

3. **update_requirements_after_dependabot.yml**: Manages Dependabot updates
   - Uses `uv pip compile` to generate requirements files

4. **update_version_and_release.yml**: Version bumping and release automation
   - Uses shell scripting to update version in pyproject.toml
   - Supports patch/minor/major version bumps

5. **delete-spam-issues.yml**: Automated spam issue cleanup

### CI Scripts

Located in `ci/` directory:

- **set_pre-commit-hooks_exclude.py**: Dynamically updates `.pre-commit-config.yaml` to exclude the generated `site/` folder from hooks
- **run_git_tag_base_pyproject.py**: Git tagging based on pyproject.toml version
- **run_mkdocs_cmd.py**: Zensical command wrapper (legacy, can still be used)
- **update_pyproject_version.py**: Version management in pyproject.toml (supports both `[project]` and `[tool.poetry]` sections)

## Working with Documentation

### Adding New Content

1. Create markdown files in both `docs/en/` and `docs/ja/` with parallel structure
2. Update the `nav` section in `mkdocs.yml` for both language sections
3. Use the appropriate frontmatter and tags if needed
4. Test locally with `uv run zensical serve`
5. Build and verify with `uv run zensical build --clean`

### Markdown Extensions

Available markdown extensions (configured in mkdocs.yml):

- Admonitions (notes, warnings, tips)
- Code blocks with line numbers
- Tabbed content
- Footnotes
- PlantUML diagrams
- Emoji support (Material icons)
- Table of contents with permalinks

## Deployment

The site is automatically deployed to GitHub Pages via GitHub Actions when:

- Code is pushed to `main` branch
- Commit message does not contain `[skip ci]`
- After successful completion of pre-commit or requirements update workflows

Manual deployment: `uv run zensical gh-deploy`

## Important Notes

- **Never edit files in `site/`**: This folder is auto-generated by Zensical
- **Maintain language parity**: Keep English and Japanese documentation in sync
- **Pre-commit hook exclusions**: Run `uv run python ci/set_pre-commit-hooks_exclude.py` after significant changes to site structure
- **uv.lock**: The uv.lock file tracks exact dependency versions (committed to version control)
- **Line length**: E501 errors are ignored to accommodate long URLs and documentation text
- **Zensical compatibility**: Zensical can read mkdocs.yml natively, so no configuration migration is required
- **Python version**: Project requires Python 3.10+, workflows use Python 3.12
