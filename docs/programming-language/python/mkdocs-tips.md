# MkDocs tips

MkDocsは静的サイトジェネレータです。コンテンツは基本的にmarkdown形式で記述したソースファイルになります。

!!! warning
    本記事は特記事項がない限り、[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)のテーマ内容を記載します。

## 使い方

詳細は下記を確認してください。

- [公式ドキュメント](https://squidfunk.github.io/mkdocs-material/getting-started/)
- [参考記事](./mkdocs-tips.md/#_3)

### プラグインの設定

!!! tip
    markdownフォーマッタ(例: mdformat)を使用している場合は、[pre-commit-hooks](https://pre-commit.com/#pre-commit-configyaml---hooks)で[mdformat-mkdocs](https://github.com/KyleKing/mdformat-mkdocs#usage)のプラグインを設定するのを推奨します。
    理由は[こちらのページ](./mdformat-tips.md/#mdformat-admon)でも記載しています。

### mkdocs.yml

```yaml
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
```

## 参考記事

以下の記事を参考にさせていただいています。

- [なかけんのMkDocsノート](https://mkdocs.nakaken88.com/)
- [コジオン: チェスさんのGitHub Pages(MkDocs)](https://kojion.github.io/chess/mkdocs/001/)
- [MkDocsによるドキュメント作成](https://zenn.dev/mebiusbox/articles/81d977a72cee01)
- [Github Pages / ゼロから学ぶPython](https://rinatz.github.io/python-book)
- [プロジェクトドキュメント構築向け静的サイトジェネレータ『MkDocs』及び『Material for MkDocs』の個人的導入＆設定まとめ](https://dev.classmethod.jp/articles/mkdocs-and-material-for-mkdocs-tips-matome/)
