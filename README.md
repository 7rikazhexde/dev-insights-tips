# dev-insights-tips

A repository that gathers insights and tips for development.<br />
It aims to share information related to programming and development.

## URL

Content(website) is managed by GitHub Pages.

- Japanese (日本語): [https://7rikazhexde.github.io/dev-insights-tips/ja/](https://7rikazhexde.github.io/dev-insights-tips/ja/)
- English: [https://7rikazhexde.github.io/dev-insights-tips/en/](https://7rikazhexde.github.io/dev-insights-tips/en/)

> **Note**: Direct language switching is currently not supported because mkdocs-static-i18n is not yet compatible with Zensical. Please access the site by specifying `/ja/` or `/en/` in the URL.

## Usage

### For local

If you want to launch website in a local repository, do the following.

```bash
git clone https://github.com/7rikazhexde/dev-insights-tips.git
cd dev-insights-tips
```

> 🚨 **Note:**<br />
> **This project uses uv for dependency management.**\
> **For uv installation, [check the official website](https://docs.astral.sh/uv/getting-started/installation/).**

```bash
# Install dependencies
uv sync --all-extras
```

> ℹ️ **Alternative: Using pip with virtual environment**<br />
> **You can also use pip with a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

create `.git/hooks/pre-commit`

> ℹ️ **Note:**<br />
> **Install pre-commit if you want to run static analysis before committing.**

```bash
uv run pre-commit install
```

> ℹ️ **Note:**<br />
> **The following script excludes files under the generated site folder from pre-commit hooks.**

```bash
uv run python ci/set_pre-commit-hooks_exclude.py
```

#### Launch local website

Execute the following command to access the URL displayed.
This project uses Zensical (by the creators of Material for MkDocs).

- <https://zensical.org/>
- <https://squidfunk.github.io/mkdocs-material/>

```bash
uv run zensical serve
```

#### Update documents

Add or update content (.md) under docs. Then execute the following command.

```bash
uv run zensical build --clean
uv run zensical serve
```

### For remote (GitHub Pages)

Content is built using Github Actions and deployed to GitHub Pages.<br />
Please check the following for the contents of the configuration file. (Basically, no change is necessary.)

[.github/workflows/push_gh-deploy.yml](.github/workflows/push_gh-deploy.yml)
