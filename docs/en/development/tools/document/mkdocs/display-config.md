---
title: Display Config
tags:
  - MKDocs
  - Material for MKDocs
description: MKDocs関連の設定に関するtipsをまとめてます。
---

## Highlight notes, hints, and warnings in the text

Reference: [admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

```yaml title="mkdocs.yml" linenums="1"
markdown_extensions:
  - admonition # (1)!
  - pymdownx.details # (2)!
  - pymdownx.superfences # (3)!
```

1. highlight notes, hints, and warnings in the text
2. detail block(!!! to ???)
3. code fence

!!! tip
    If you are using a markdown formatter (e.g. mdformat), you should use [pre-commit-hooks](https://pre-commit.com/#pre-commit-configyaml---hooks) to set up the [mdformat-mkdocs](https://github.com/KyleKing/mdformat-mkdocs#usage) plugin is recommended.
    The reason is explained in the [mdformat-admon section](./mdformat.md/#mdformat-admon).

## Display code block

Reference: [Code blocks](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)

## Tabbed display of code blocks

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

## Add copy, code selection, and annotations to code blocks

```yaml title="mkdocs.yml"
thema:
  features:
    - content.code.copy
    - content.code.select
    - content.code.annotate
```

## Display code

!!! tip

     - To highlight using pygments, enable the following comment-outs.
     - `linenums: true` displays the number of lines of code.
     - The number of lines is displayed without python `linenum="1"`.

```yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.highlight:
      #use_pygments: true
      #noclasses: true
      #pygments_style: monokai
      linenums: true
```

## Display code in admonition

[Highlight notes, hints, and warnings in the text](#highlight-notes-hints-and-warnings-in-the-text)参照

## Display emoji

```yaml title="mkdocs.yml"
markdown_extensions:
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
```

:smile:

:simple-bitcoin:

## Pop-up image display

[glightbox](https://github.com/blueswen/mkdocs-glightbox) plugin.

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
