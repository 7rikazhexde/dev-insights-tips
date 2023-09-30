# Display Config Tips

## 文章内にメモ、ヒント、警告をハイライト表示する

参考: [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

```yaml title="mkdocs.yml" linenums="1"
markdown_extensions:
  - admonition # (1)!
  - pymdownx.details # (2)!
  - pymdownx.superfences # (3)!
```

1. 文章内にメモ、ヒント、警告をハイライト表示する
2. 詳細ブロック(!!!を???にする)
3. コードフェンス

!!! tip
    markdownフォーマッタ(例: mdformat)を使用している場合は、[pre-commit-hooks](https://pre-commit.com/#pre-commit-configyaml---hooks)で[mdformat-mkdocs](https://github.com/KyleKing/mdformat-mkdocs#usage)のプラグインを設定するのを推奨します。
    理由は[こちらのページ](./mdformat-tips.md/#mdformat-admon)でも記載しています。

## コードブロックを表示する

参考: [Code blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)

## コードブロックをタブ表示する

```yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
```

=== "C"

    ```c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ```c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

## コードブロックにコピー、コード選択、注釈を追加する

```yaml title="mkdocs.yml"
thema:
  features:
    - content.code.copy
    - content.code.select
    - content.code.annotate
```

## コード表示

pygmentsを使ってハイライト表示する場合は以下のコメントアウトを有効にする。<br/>
`linenums: true`はコード行数表示。<br/>
\```python linenum="1"\```を指定しなくとも行数が表示されます。

```yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.highlight:
      #use_pygments: true
      #noclasses: true
      #pygments_style: monokai
      linenums: true
```

## admonitionでコードを表示する

「文章内にメモヒント警告をハイライト表示する」を参照してください。

## emojiを表示する

```yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
```

:smile:

:simple-bitcoin:

## 画像をポップアップ表示する

[glightbox](https://github.com/blueswen/mkdocs-glightbox)プラグインを使用します。

```bash
poetry add mkdocs-glightbox
```

```bash
pip install mkdocs-glightbox
```

```yaml title="mkdocs.yml"
plugins:
  - glightbox
```
