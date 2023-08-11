# pre-commit tips

pre-commitは、`git hook`の一機能ですが、Gitリポジトリ内のコミット前に自動的に実行されるコマンドやスクリプトを設定するためのツールとしてPyPlで公開されています。このツールは、コードの品質を維持し、一貫性を確保するために使用されます。

詳細は公式ドキュメント参照<br />
[https://pre-commit.com/](https://pre-commit.com/)

pre-commitを使用すると、開発者はコミット前にさまざまな静的解析やコードフォーマットツールを実行することができます。これにより、コードスタイルの遵守や一般的なエラーパターンの検出、セキュリティの脆弱性のチェックなどが自動的に行われます。pre-commitは、リポジトリ全体または個々のファイルに対して、カスタマイズ可能なフック（hooks）を設定することができます。

pre-commitの設定は、.pre-commit-config.yamlという名前のファイルに記述されます。このファイルでは、使用するフックや実行するコマンド、除外するファイルなどの設定を指定する。pre-commitは、コミット前にフックを自動的に実行し、フックの結果に基づいてコミットの承認または中止を判断する。

pre-commitは、さまざまなプログラミング言語やツールに対応しており、多くの既存のフックが公開されています。また、カスタムフックを作成することも可能です。

pre-commitの主な利点は次のとおりです:

- コードの品質向上: pre-commitを使用することで、コードスタイルの統一や一般的なエラーパターンの検出など、コードの品質を向上させることができます。
- 自動化された静的解析: pre-commitは、静的解析ツールやコードフォーマットツールを自動的に実行するため、開発者は手動でこれらのツールを実行する手間を省くことができます。
- チームの共通ルールの遵守: pre-commitの設定はリポジトリ内で共有されるため、開発チーム全体で一貫したコーディングルールやベストプラクティスの遵守が容易になります。
- エラーの早期検出: pre-commitは、コミット前にフックを実行するため、エラーや問題を早期に検出し修正することができます。

注意点として、pre-commitはコミット前に実行されるため、フックが時間をかけて実行されるとコミットが遅くなる場合があります。また、pre-commitの設定はリポジトリに含まれており、チームメンバーが同じ設定を使用していることを確認する必要があります。

pre-commitは、品質管理と開発効率の向上のために広く利用されているツールであり、多くのプロジェクトで採用されています。

## 使い方

### .pre-commit-config.yamlで使用するフック

#### 参考記事: [pre-commitでコミット時にコードの整形やチェックを行う](https://zenn.dev/yiskw713/articles/3c3b4022f3e3f22d276d)

- pre-commit-hooks: pre-commitツールの一部として提供されるプラグインの集合体。
  - trailing-whitespace: ファイルの末尾に不要な空白文字があるかどうかを検出する。
  - end-of-file-fixer: ファイル最終行を改行コードにする。
  - mixed-line-ending: 改行コードを LF に統一。
  - check-added-large-files: 巨大なファイルの commit を禁止。
  - check-yaml: YAMLファイルの構文の妥当性を確認する。
  - check-toml: TOMLファイルの構文の妥当性を確認する。
  - detect-aws-credentials: AWSのcredentialファイルがあるかどうかを確認。`--allow-missing-credentials`オプションを追加することで，credentailファイルがない場合でもhookが通るようになる。
- フォーマッター (formatter)
  - black: Pythonコードの自動フォーマットを行い、コードスタイルを統一する。
  - isort: Pythonのインポートステートメントを整理・ソートする。
  - mdformat: Markdownファイルに一貫したスタイルを強制する。
- リンター (linter)
  - flake8: Pythonコードの静的解析を行い、コードスタイルの違反や一般的なエラーパターンを検出する。
  - mypy: 静的型検査ツール
- Poetry関連
  - poetry-check: poetryの設定が壊れた状態でコミットされないことを確認するためにpoetry checkコマンドを呼び出す。
  - poetry-lock: 変更をコミットする際にロックファイルが最新であることを確認するために poetry lock コマンドを呼び出す。
  - poetry-export: poetry export コマンドを呼び出して、requirements.txt ファイルと現在の依存関係を同期させる。argsに--devを追加することで、dev-dependenciesを書き出すことも可能。
- オリジナルスクリプト
  - 事例: [【Pythonバージョン管理】git hookを使用してコミットをトリガーにpyproject.tomlとgit tagを更新するスクリプトについて](https://7rikazhexde-techlog.hatenablog.com/entry/2023/06/10/005231)

#### 実例

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
        exclude: '(site|site/tool_tips|site/db_tips|site/search|site/git_tips|site/python_tips|site/vscode_tips|site/assets|site/tool_tips/tool\-tips|site/db_tips/mariadb|site/db_tips/mariadb/mariadb\-tips|site/git_tips/git\-tips|site/python_tips/pymysql|site/python_tips/dash_plotly|site/python_tips/pymysql/pymysql\-tips|site/python_tips/dash_plotly/dash\-plotly\-tips|site/vscode_tips/vscode\-tips|site/assets/images|site/assets/javascripts|site/assets/stylesheets|site/assets/javascripts/lunr|site/assets/javascripts/workers|site/assets/javascripts/lunr/min)/.*'
      # Make the last line of the file a newline code
      - id: end-of-file-fixer
      # Unify line break code to LF
        exclude: '(site|site/tool_tips|site/db_tips|site/search|site/git_tips|site/python_tips|site/vscode_tips|site/assets|site/tool_tips/tool\-tips|site/db_tips/mariadb|site/db_tips/mariadb/mariadb\-tips|site/git_tips/git\-tips|site/python_tips/pymysql|site/python_tips/dash_plotly|site/python_tips/pymysql/pymysql\-tips|site/python_tips/dash_plotly/dash\-plotly\-tips|site/vscode_tips/vscode\-tips|site/assets/images|site/assets/javascripts|site/assets/stylesheets|site/assets/javascripts/lunr|site/assets/javascripts/workers|site/assets/javascripts/lunr/min)/.*'
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

      - id: mdformat
        name: mdformat
        stages: [commit]
        language: system
        entry: poetry run mdformat .
        types: [markdown]

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
