---
tags:
  - python
  - git
  - pre-commit
---

# pre-commit tips

pre-commit, a feature of `git hook`, is a tool available on PyPl to set up commands and scripts to be run automatically before committing in a Git repository. This tool is used to maintain code quality and ensure consistency.

See official documentation for details.<br />
[https://pre-commit.com/](https://pre-commit.com/)

With pre-commit, developers can run a variety of static analysis and code formatting tools prior to commit. Pre-commit allows developers to set customizable hooks (hooks) for the entire repository or for individual files.

The pre-commit configuration is described in a file named.`pre-commit-config.yaml`. This file specifies settings such as hooks to use, commands to execute, files to exclude, etc. pre-commit automatically executes hooks before commit and decides whether to accept or abort the commit based on the results of the hooks.

pre-commit is supported by a variety of programming languages and tools, and many existing hooks are publicly available. Custom hooks can also be created.

The main advantages of pre-commit are:

- Improved code quality: pre-commit can be used to improve code quality by unifying code styles and detecting common error patterns.
- Automated static analysis: pre-commit automatically runs static analysis and code formatting tools, eliminating the need for developers to run these tools manually.
- Team adherence to common rules: pre-commit settings are shared within the repository, making it easier for the entire development team to adhere to consistent coding rules and best practices.
- Early detection of errors: pre-commit runs hooks before committing, allowing for early detection and correction of errors and problems.

As a precaution, pre-commit is executed before commit, so commits may be delayed if hooks are executed over time. Also, pre-commit settings are included in the repository, and you must ensure that all team members are using the same settings.

pre-commit is a widely used tool for quality control and development efficiency and has been adopted by many projects.

## Usage

### Hooks used in `.pre-commit-config.yaml`

#### Reference article (Japanese): [pre-commitでコミット時にコードの整形やチェックを行う](https://zenn.dev/yiskw713/articles/3c3b4022f3e3f22d276d)

- pre-commit-hooks: A collection of plug-ins provided as part of the pre-commit tool.
  - trailing-whitespace: Detects the presence of unwanted whitespace characters at the end of a file.
  - end-of-file-fixer: Make the last line of the file a newline code.
  - mixed-line-ending: Unify line feed code to LF.
  - check-added-large-files: Prohibit commit of large files.
  - check-yaml: Check the validity of the syntax of YAML files.
  - check-toml: Check the validity of the syntax of TOML files.
  - detect-aws-credentials: Check if there is an AWS credential file. By adding the --allow-missing-credentials option, the hook will pass even if there is no credentail file.
- formatter
  - black: Automatic formatting of Python code to unify code styles.
  - isort: Organize and sort Python import statements.
  - mdformat: Enforce consistent styles in Markdown files.
- linter
  - flake8: Perform static analysis of Python code to detect code style violations and common error patterns.
  - mypy: Static Type Inspection Tool
- Poetry related
  - poetry-check: Call the poetry check command to make sure that the poetry setting is not committed in a broken state.
  - poetry-lock: Call the poetry lock command to ensure that the lock file is up-to-date when committing changes.
  - poetry-export: Call the `poetry export` command to synchronize the `requirements.txt` file with the current dependencies. `dev-dependencies` can also be exported by adding `--dev` to the args.
- Original script
  - Case(Japanese): [【Pythonバージョン管理】git hookを使用してコミットをトリガーにpyproject.tomlとgit tagを更新するスクリプトについて](https://7rikazhexde-techlog.hatenablog.com/entry/2023/06/10/005231)

### hook processing

#### pre-commit hook for individual mdformat[^1]

```bash
git add your_file.md # Stage the target Markdown file
poetry run pre-commit run mdformat
```

#### To run hooks on unstaged files, too.[^1]

```bash
poetry run pre-commit run mdformat --all-files # run with id
poetry run pre-commit run --all-files # Run all id's
```

#### Example

##### [dev-insights-tips /.pre-commit-config.yaml](https://github.com/7rikazhexde/dev-insights-tips/blob/main/.pre-commit-config.yaml)

```yaml
# pre-commit stop running hooks after the first failure.
fail_fast: true
# A list of repository mappings
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    # Specify version or tag to use (as of 23.5.31)
    rev: v4.4.0
    hooks:
      # Remove spaces at end of lines except markdown
      - id: trailing-whitespace
        args: [--markdown-linebreak-ext=md]
        exclude:
          (site|site/tool_tips|site/db_tips|site/search|site/git_tips|site/python_tips|site/vscode_tips|site/assets|site/tool_tips/tool\-tips|site/db_tips/mariadb|site/db_tips/mariadb/mariadb\-tips|site/git_tips/git\-tips|site/python_tips/pymysql|site/python_tips/dash_plotly|site/python_tips/pymysql/pymysql\-tips|site/python_tips/dash_plotly/dash\-plotly\-tips|site/vscode_tips/vscode\-tips|site/assets/images|site/assets/javascripts|site/assets/stylesheets|site/assets/javascripts/lunr|site/assets/javascripts/workers|site/assets/javascripts/lunr/min)/.*
      # Make the last line of the file a newline code
      - id: end-of-file-fixer
      # Unify line break code to LF
        exclude:
          (site|site/tool_tips|site/db_tips|site/search|site/git_tips|site/python_tips|site/vscode_tips|site/assets|site/tool_tips/tool\-tips|site/db_tips/mariadb|site/db_tips/mariadb/mariadb\-tips|site/git_tips/git\-tips|site/python_tips/pymysql|site/python_tips/dash_plotly|site/python_tips/pymysql/pymysql\-tips|site/python_tips/dash_plotly/dash\-plotly\-tips|site/vscode_tips/vscode\-tips|site/assets/images|site/assets/javascripts|site/assets/stylesheets|site/assets/javascripts/lunr|site/assets/javascripts/workers|site/assets/javascripts/lunr/min)/.*
      - id: mixed-line-ending
        args: [--fix=lf]
      # toml syntax check
      - id: check-toml
      # yaml syntax check
      - id: check-yaml

  # https://python-poetry.org/docs/pre-commit-hooks/#usage
  - repo: https://github.com/python-poetry/poetry
    # Cannot be executed with local designation (as of 23.5.31)
    rev: 1.5.1
    hooks:
      - id: poetry-check
        verbose: true
      - id: poetry-lock
        verbose: true
      - id: poetry-export
        args: [-f, requirements.txt, -o, requirements.txt]
        verbose: true
        files: ^pyproject\.toml$
      - id: poetry-export
        args: [--dev, -f, requirements.txt, -o, requirements-dev.txt]
        verbose: true
        files: ^pyproject\.toml$

  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.16
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-admon
          - mdformat-beautysh
          - mdformat-black
          - mdformat-config
          - mdformat-footnote
          - mdformat-frontmatter
          - mdformat-simple-breaks
          - mdformat-tables
          - mdformat-toc
          - mdformat-web

  # Repository local hooks
  - repo: local
    hooks:
      - id: isort
        name: isort
        stages: [commit]
        language: system
        entry: poetry run isort ci
        types: [python]

      - id: black
        name: black
        stages: [commit]
        language: system
        entry: poetry run black ci
        types: [python]
        exclude: resources_bin.py

      - id: flake8
        name: flake8
        stages: [commit]
        language: system
        entry: poetry run flake8 ci
        types: [python]

      - id: mypy
        name: mypy
        stages: [commit]
        language: system
        entry: poetry run mypy
        types: [python]

      #- id: mdformat
      #  name: mdformat
      #  stages: [commit]
      #  language: system
      #  entry: poetry run mdformat .
      #  types: [markdown]

    # Original script
      - id: update-pyproject
        name: mkdocs build
        entry: poetry run python ci/run_mkdocs_cmd.py
        language: system
        verbose: true
        pass_filenames: false
        stages: [commit]
        additional_dependencies: []

      - id: update-pyproject
        name: Update pyproject.toml version
        entry: poetry run python ci/update_pyproject_version.py
        language: system
        verbose: true
        pass_filenames: false
        stages: [commit]
        additional_dependencies: []
```

[^1]: If you don't use poetry, only pre-commit run is fine.
