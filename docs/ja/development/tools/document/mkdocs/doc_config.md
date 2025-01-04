---
title: MKDocs Document Config
tags:
  - MKDocs
  - Material for MKDocs
description: MKDocs関連のtipsをまとめてます。
---

!!! tip

    - ドキュメントの構成は`mkdocs.yml`の`nav`に指定します。
    - navを設定すると画面左側に表示されるドキュメントの一覧が表示されます。
    - 以下の`nav`設定をベースにするとドキュメントの追加、変更に適した構成で管理がしやすいと思います。

```yaml title="mkdocs.yaml"
nav: # (1)!
  - Home: index.md # (2)!
  - Programming language:
      - ja/programming-language/index.md # (3)!
      - Python:
      - ja/programming-language/python/index.md # (4)!
          - Mkdocs tips:
              - ja/programming-language/python/mkdocs/index.md # (5)!
              - ja/programming-language/python/mkdocs/display-config_tips.md # (6)!
```

1. `- navigation.indexes`を有効にすると`index.md`をリンク先として設定する
2. 初期画面
3. Programming languageセクションの初期ページ
4. Pythonセクションの初期ページ
5. ・Mkdocs tipsの初期ページ<br/>
   ・`Page1: ja/programming-language/python/mkdocs/index.md`という表記も可能<br/>
   ・明示的に表示しない場合は"h1"タグの内容が表示される
6. サブセクション、または、`index.md`内でリンクを設定してアクセス可能

## navの表示設定

!!! tip

    複数のドキュメントを持つ構成の場合は以下の設定で十分です。

```yaml title="mkdocs.yaml"
theme:
  features:
    # Enable link setting on section
    - navigation.indexes
    # Back-to-top button
    - navigation.top
    # groups in the sidebar
    #- navigation.sections
    # expand all collapsible subsections
    #- navigation.expand
```
