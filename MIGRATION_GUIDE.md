# Migration Guide: Poetry + Material for MkDocs → uv + Zensical

This guide documents the migration process from Poetry + Material for MkDocs to uv + Zensical, based on the successful migration of [dev-insights-tips](https://github.com/7rikazhexde/dev-insights-tips).

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Reference Documentation](#reference-documentation)
- [Migration Steps](#migration-steps)
- [Special Considerations](#special-considerations)
- [Troubleshooting](#troubleshooting)
- [Verification](#verification)

## Overview

### What is Zensical?

Zensical is a modern static site generator built by the creators of Material for MkDocs:

- Built with Rust and Python for better performance
- Backward compatible with `mkdocs.yml` configuration
- Can read existing MkDocs configurations natively
- Supports both YAML (`mkdocs.yml`) and TOML (`zensical.toml`) configuration formats

### Why Migrate to uv?

- **Faster dependency resolution**: 10-100x faster than pip/Poetry
- **Simpler configuration**: Standard PEP 621 `pyproject.toml` format
- **Better caching**: Built-in cache management
- **Modern toolchain**: Single tool for dependency management

## Prerequisites

- Python 3.10 or higher
- Git installed
- Basic understanding of your current MkDocs setup
- Backup of your current repository

## Reference Documentation

### Official Zensical Documentation

- **Main Documentation**: <https://zensical.org/docs/>
- **Get Started**: <https://zensical.org/docs/get-started/>
- **Setup Basics**: <https://zensical.org/docs/setup/basics/>
- **Configuration Compatibility**: <https://zensical.org/compatibility/configuration/>
- **Command Line Interface**: <https://zensical.org/compatibility/cli/>
- **Customization**: <https://zensical.org/docs/customization/>

### Additional Resources

- **Zensical Announcement**: <https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/>
- **uv Documentation**: <https://docs.astral.sh/uv/>
- **Example Project**: <https://github.com/7rikazhexde/dev-insights-tips>

## Migration Steps

### Step 1: Pre-Migration Assessment

Before starting migration, assess your current setup:

```bash
# Check current dependencies
poetry show

# Check if you have custom templates
ls -la overrides/

# Check for custom plugins in mkdocs.yml
grep "plugins:" mkdocs.yml -A 20

# Check for multilingual setup
grep "i18n" mkdocs.yml
```

**⚠️ IMPORTANT CHECKPOINTS:**

1. **Multilingual Sites (mkdocs-static-i18n)**
   - If your site uses `mkdocs-static-i18n` plugin, note that it is **not yet fully compatible with Zensical**
   - Language switching will need to be manual (e.g., `/ja/` and `/en/` paths)
   - **ACTION REQUIRED**: Confirm with the project owner how they want to handle multilingual access

2. **Custom Templates and Overrides**
   - Check all files in `overrides/` directory
   - Custom templates may need updates for Zensical compatibility
   - **ACTION REQUIRED**: Review each custom template file

3. **Custom Plugins**
   - List all plugins in `mkdocs.yml`
   - Check if they are compatible with Zensical
   - **ACTION REQUIRED**: Research compatibility for each non-standard plugin

### Step 2: Install uv

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version
```

### Step 3: Update pyproject.toml

Replace Poetry configuration with PEP 621 standard format:

**Before (Poetry format):**

```toml
[tool.poetry]
name = "your-project"
version = "0.1.0"
description = "..."
authors = ["Your Name"]

[tool.poetry.dependencies]
python = "^3.10"
mkdocs-material = "^9.7.0"
# ... other dependencies

[tool.poetry.group.dev.dependencies]
black = "^25.11.0"
# ... other dev dependencies
```

**After (PEP 621 format):**

```toml
[project]
name = "your-project"
version = "0.1.0"
description = "..."
authors = [{name = "Your Name"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "zensical>=0.0.8",
    # Copy other dependencies from [tool.poetry.dependencies]
    # Note: Remove mkdocs-material, add zensical
]

[project.optional-dependencies]
dev = [
    "black>=25.11.0",
    # Copy from [tool.poetry.group.dev.dependencies]
]

[tool.taskipy.tasks]
# Update commands from 'mkdocs' to 'zensical'
serve = "zensical serve"
build = "zensical build"
deploy = "zensical build --clean && ghp-import -npfm 'Deploy site' site"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

# Add this for non-package projects
[tool.hatch.build.targets.wheel]
packages = ["src/your_project_name"]

# Keep other [tool.*] sections (ruff, black, mypy, etc.)
```

**Important Notes:**

- Replace `mkdocs-material` with `zensical>=0.0.8`
- Keep all other MkDocs plugins (mkdocs-glightbox, mkdocs-static-i18n, etc.)
- Update version constraints from `^x.y.z` to `>=x.y.z`

### Step 4: Create Minimal Package Structure

For non-package projects, create a minimal structure for hatchling:

```bash
mkdir -p src/your_project_name
touch src/your_project_name/__init__.py
```

### Step 5: Update .gitignore

```bash
# Add to .gitignore
echo "src/" >> .gitignore
```

### Step 6: Remove Poetry Files and Install with uv

```bash
# Remove Poetry lock file
rm poetry.lock

# Install dependencies with uv
uv sync --all-extras

# Verify uv.lock was created
ls -la uv.lock
```

### Step 7: Update Custom Templates (if any)

If you have custom templates in `overrides/`, you may need to update them:

**Common Issue**: Undefined variables in Jinja2 templates

**Example Fix:**

```jinja
{# Before #}
{% if page.meta.description %}

{# After - Add existence check for page.meta #}
{% if page and page.meta and page.meta.description %}
```

**⚠️ ACTION REQUIRED**: Review all files in `overrides/` directory and test them locally.

### Step 8: Update GitHub Actions Workflows

Update all workflow files to use uv instead of Poetry:

**Before:**

```yaml
- name: Set up Python
  uses: actions/setup-python@v6
  with:
    python-version: "3.13"
- name: Install Poetry
  run: pip install poetry
- name: Install dependencies
  run: poetry install
- name: Deploy
  run: poetry run mkdocs gh-deploy --force
```

**After:**

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v5
  with:
    enable-cache: true
    cache-dependency-glob: "pyproject.toml"
- name: Set up Python
  run: uv python install 3.12
- name: Install dependencies
  run: uv sync --all-extras
- name: Build site
  run: uv run zensical build --clean
- name: Deploy to GitHub Pages
  run: uv run ghp-import -npfm "Deploy site" site
```

**Key Changes:**

- Use `astral-sh/setup-uv@v5` action
- Replace `poetry install` with `uv sync --all-extras`
- Split deployment into build + ghp-import (Zensical doesn't have `gh-deploy` command)
- Change from Python 3.13 to 3.12 (or your preferred version)

### Step 9: Update pre-commit Hooks

Remove Poetry-specific hooks from `.pre-commit-config.yaml`:

**Remove:**

```yaml
- repo: https://github.com/python-poetry/poetry
  rev: 2.2.1
  hooks:
    - id: poetry-check
    - id: poetry-lock
```

**Add (optional):**

```yaml
- repo: https://github.com/python-jsonschema/check-jsonschema
  rev: 0.31.0
  hooks:
    - id: check-github-workflows
    - id: check-github-actions
```

### Step 10: Update CI Scripts

If you have scripts that manage versions (like `ci/update_pyproject_version.py`), update them to support `[project]` section:

```python
# Support both [project] and [tool.poetry] sections
if "project" in toml_data:
    current_data = toml_data["project"].get("version", "0.0.0")
elif "tool" in toml_data and "poetry" in toml_data["tool"]:
    current_data = toml_data["tool"]["poetry"].get("version", "0.0.0")
else:
    current_data = "0.0.0"
```

### Step 11: Update Documentation

Update README.md and other documentation:

```markdown
## Development Setup

This project uses **uv** for dependency management.

### Installation

```bash
# Install dependencies
uv sync --all-extras

# Set up pre-commit hooks
uv run pre-commit install
```

### Common Commands

```bash
# Serve documentation locally
uv run zensical serve

# Build documentation
uv run zensical build --clean

# Deploy to GitHub Pages
uv run task deploy
```

**For multilingual sites:**

```markdown
## Site URLs

- Japanese: https://your-site.github.io/your-project/ja/
- English: https://your-site.github.io/your-project/en/

> **Note**: Direct language switching is currently not supported because
> mkdocs-static-i18n is not yet compatible with Zensical. Please access
> the site by specifying `/ja/` or `/en/` in the URL.
```

## Special Considerations

### Multilingual Sites (mkdocs-static-i18n)

**Current Status**: mkdocs-static-i18n is **NOT yet fully compatible** with Zensical.

**Implications**:

- Language switcher in the UI may not work
- Users must access different language versions via URL paths
- Configuration remains in `mkdocs.yml` but runtime behavior is limited

**Configuration** (still works):

```yaml
plugins:
  - i18n:
      docs_structure: folder
      fallback_to_default: true
      languages:
        - locale: en
          name: English
        - locale: ja
          name: 日本語
          default: true
```

**Access Pattern**:

- Japanese: `/ja/`
- English: `/en/`
- No automatic language switching

**⚠️ DECISION POINT**: Ask project owner if they want to:

1. Accept manual language switching
2. Wait for mkdocs-static-i18n compatibility
3. Implement a custom solution
4. Stay with Material for MkDocs for now

### Custom Plugins Compatibility

Check each plugin's compatibility:

**Known Compatible:**

- `mkdocs-glightbox` ✅
- `plantuml-markdown` ✅
- `tags` ✅

**Known Issues:**

- `mkdocs-static-i18n` ⚠️ (limited functionality)

**⚠️ ACTION**: For any custom or uncommon plugins:

1. Check plugin documentation for Zensical compatibility
2. Test locally before deploying
3. Have a rollback plan ready

### Custom Templates and Overrides

**Common Template Issues:**

1. **Undefined Variables**

   ```jinja
   {# Add existence checks #}
   {% if page and page.meta and page.meta.description %}
       {{ page.meta.description }}
   {% endif %}
   ```

2. **Theme Structure Changes**
   - Zensical may have different template structure
   - Test all custom templates locally
   - Check for console errors in browser

3. **CSS/JavaScript Overrides**
   - Custom CSS in `docs/stylesheets/` should work
   - Custom JavaScript may need updates

**⚠️ ACTION**:

- Review every file in `overrides/` directory
- Test each custom template locally
- Check browser console for JavaScript errors
- Verify all custom styling works

### Theme Configuration

Zensical supports Material for MkDocs theme configuration in `mkdocs.yml`:

```yaml
theme:
  name: material  # Keep this - Zensical understands it
  palette:
    # Your existing palette configuration
  features:
    # Your existing features
```

**Note**: You can keep `theme.name: material` - Zensical will automatically adapt it.

## Troubleshooting

### Build Errors

**Error**: `No such command 'gh-deploy'`

- **Solution**: Use `zensical build --clean` + `ghp-import` instead
- See Step 8 for GitHub Actions workflow example

**Error**: `Unable to determine which files to ship inside the wheel`

- **Solution**: Add minimal package structure (see Step 4)

**Error**: `undefined value (in main.html:X)`

- **Solution**: Add existence checks in templates (see Custom Templates section)

### Template Errors

If you get template errors:

1. Check browser console for specific error messages
2. Review the specific template file mentioned in error
3. Add defensive checks: `{% if var and var.property %}`
4. Test locally before deploying

### Language Switching Not Working

This is expected with mkdocs-static-i18n:

1. Verify URLs work: `/ja/` and `/en/`
2. Update documentation to inform users
3. Consider adding language selection links manually

### Dependency Resolution Issues

```bash
# Clear uv cache
uv cache clean

# Re-sync dependencies
uv sync --all-extras

# Check for conflicts
uv pip tree
```

## Verification

### Local Testing

```bash
# 1. Test build
uv run zensical build --clean

# 2. Test serve
uv run zensical serve

# 3. Check for errors in browser console
# Visit http://localhost:8000

# 4. Test all pages, especially:
#    - Custom template pages
#    - Multilingual pages (if applicable)
#    - Pages with custom plugins
```

### Pre-Deployment Checklist

- [ ] All dependencies installed successfully
- [ ] Local build completes without errors
- [ ] Local serve works correctly
- [ ] All custom templates render properly
- [ ] No console errors in browser
- [ ] Links work correctly
- [ ] Search functionality works
- [ ] Code blocks render correctly
- [ ] Images and assets load properly
- [ ] (Multilingual) Both language versions accessible
- [ ] GitHub Actions workflows updated
- [ ] Documentation updated
- [ ] Pre-commit hooks working

### Post-Deployment Verification

After pushing to GitHub:

1. **Check GitHub Actions**: Verify workflow completes successfully
2. **Check Deployed Site**: Visit the GitHub Pages URL
3. **Test All Features**: Click through navigation, search, etc.
4. **Check Multiple Browsers**: Test in Chrome, Firefox, Safari
5. **Mobile Testing**: Verify responsive design works

## Rollback Plan

If migration fails, you can rollback:

```bash
# Restore poetry.lock
git checkout HEAD~1 poetry.lock

# Restore pyproject.toml
git checkout HEAD~1 pyproject.toml

# Restore workflows
git checkout HEAD~1 .github/workflows/

# Reinstall with Poetry
poetry install
```

## Example Migration Commit

See the actual migration commit from dev-insights-tips:

- <https://github.com/7rikazhexde/dev-insights-tips/commit/d159a38>

## Getting Help

If you encounter issues:

1. Check this guide's Troubleshooting section
2. Review the example project: <https://github.com/7rikazhexde/dev-insights-tips>
3. Check Zensical documentation: <https://zensical.org/docs/>
4. Check uv documentation: <https://docs.astral.sh/uv/>

## Summary

**Key Takeaways:**

- Zensical is backward compatible with `mkdocs.yml`
- uv is significantly faster than Poetry
- Most MkDocs plugins work with Zensical
- mkdocs-static-i18n has limited compatibility (manual language switching)
- Custom templates may need updates
- Test thoroughly before deploying

**Migration Time Estimate:**

- Simple site (no custom plugins/templates): 1-2 hours
- Complex site (custom plugins/templates): 3-6 hours
- Multilingual site: Add 1-2 hours for testing

**Success Criteria:**

- Site builds without errors
- All pages render correctly
- Navigation works properly
- Deployment to GitHub Pages succeeds

---

**Document Version**: 1.0
**Last Updated**: 2025-11-16
**Based on Project**: [dev-insights-tips](https://github.com/7rikazhexde/dev-insights-tips)
**Zensical Version**: 0.0.8
