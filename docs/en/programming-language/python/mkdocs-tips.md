# MkDocs tips

MkDocs is a static site generator. Contents are basically source files written in markdown format.

!!! warning
    This article describes the subject content of [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) unless otherwise noted.

## Usage

For more information, please check the following:

- [Official Documents](https://squidfunk.github.io/mkdocs-material/getting-started/)
- [Reference](./mkdocs-tips.md/#reference)

### Highlight notes, hints, and warnings in the text

Reference: [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

```yaml title="" linenums="1"
markdown_extensions:
  - admonition # (1)!
  - pymdownx.details # (2)!
  - pymdownx.superfences # (3)!
```

1. Highlight notes, hints, and warnings within sentences
2. detail blocks (!!!! to ??? to be)
3. code fences

!!! tip
    If you are using a markdown formatter (e.g. mdformat), you should use [pre-commit-hooks](https://pre-commit.com/#pre-commit-configyaml---hooks) to set up the [mdformat-mkdocs](https://github.com/KyleKing/mdformat-mkdocs#usage) plugin is recommended.
    The reason is that [here](./mdformat-tips.md/#mdformat-admon).

## Reference

I am referring to the following article.

- [なかけんのMkDocsノート](https://mkdocs.nakaken88.com/)
- [コジオン: チェスさんのGitHub Pages(MkDocs)](https://kojion.github.io/chess/mkdocs/001/)
- [MkDocsによるドキュメント作成](https://zenn.dev/mebiusbox/articles/81d977a72cee01)
- [Github Pages / ゼロから学ぶPython](https://rinatz.github.io/python-book)
- [プロジェクトドキュメント構築向け静的サイトジェネレータ『MkDocs』及び『Material for MkDocs』の個人的導入＆設定まとめ](https://dev.classmethod.jp/articles/mkdocs-and-material-for-mkdocs-tips-matome/)
