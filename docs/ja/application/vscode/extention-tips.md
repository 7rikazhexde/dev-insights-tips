# 拡張機能

拡張機能を用途別で紹介します。

## マークダウンファイル(.md)の目次作成

「Markdown All in One」を使用します。

### リポジトリ

[https://github.com/yzhang-gh/vscode-markdown](https://github.com/yzhang-gh/vscode-markdown)

### 使い方

コマンドパレットを起動して、「Markdown All in One: 目次（TOC）の作成」を実行します。

以下のように目次（一部省略）が作られる。

```bash
- [vscode-tips](#vscode-tips)
- [Table Of Contents](#table-of-contents)
- [拡張機能まとめ(用途別)](#拡張機能まとめ用途別)
- [マークダウンファイル(.md)の目次作成](#マークダウンファイルmdの目次作成)
```

デフォルトではタイトルと目次も出力されます。<br />
設定ではプロジェクトファイルの目次（TOC）で除外する見出しの一覧を設定できるが、文言はプロジェクトで変わるので設定はできない？正規表現が使えればできそすが未確認です。

```bash
Markdown › Extension › Toc: Omitted From Toc
```

もしタイトルと目次が不要ならば削除して字上げをすることで可能です。

Windowsの場合:

- インデントのレベルを下げる：「Ctrl+\]」 or 「Tab」
- インデントのレベルを上げる：「Ctrl＋\[」 or 「Tab＋Shift」

もしくはテキストを矩形選択して調整することが可能です。

参考： [VS Codeでテキストを矩形選択するには](https://atmarkit.itmedia.co.jp/ait/articles/1805/11/news022.html)

## Markdownの構文やスタイルをチェックして修正する

markdownlintを使用します。<br />
markdownlintはMarkdownファイルの標準と一貫性を促進するルールのライブラリを含むVSCodeの拡張機能です。

### リポジトリ

[https://github.com/DavidAnson/vscode-markdownlint](https://github.com/DavidAnson/vscode-markdownlint)

### 使い方

### Markdownのチェック項目を意図的にOFFにする

### 参考記事: markdownlint Markdownのチェック項目を意図的にOFFにする

[(https://qiita.com/miriwo/items/132750876e37df26e976)](https://qiita.com/miriwo/items/132750876e37df26e976)

#### Markdownのチェック項目の変更(settings.json)

```text
拡張機能の有効 > ユーザー > Markdownlint: Config(settings.jsonで編集)
```

#### 無効化しているmarkdownlint Markdownのチェック項目(markdownlint.config)

使用している設定は下記の通りです。

```json
    "markdownlint.config": {
        //"MD007": false, // Unordered list indentation / 番号なしリストのインデント
        //"MD009": false, // Trailing spaces / 末尾のスペース
        //"MD010": false, // Hard tabs / インデントのタブ
        //"MD014": false, // Dollar signs used before commands without showing output / コマンドの前にドル記号を使用して出力を表示しない
                          // コードブロックでコマンドライン(bash/zsh)を書く場合、コピー＆ペーストを考慮すると、
                          // "$"や"%"は表示しない方が良いので警告を有効にする。(見た目重視であれば無効にする。)
        "MD024": false,   // Multiple headings with the same content / 同じ内容の複数の見出し
        "MD025": false,   // Multiple top-level headings in the same document / 同じドキュメント内の複数のトップレベルの見出し
        "MD026": false,   // Trailing punctuation in heading / 見出しの末尾の句読点
        "MD033": false,   // Inline HTML / raw HTMLの記入
                          // MD009を無効にする変わりに改行に<br/>を使用するため無効にする。
        //"MD040": false  // Fenced code blocks should have a language specified / フェンスされたコードブロックには言語を指定する必要があります
                          // 個人的に言語問わずハイライトした方が良いので有効にする。
    }
```

### ファイル単位で修正する

```text
Markdownファイルを全て選択 > 右クリック > ドキュメントのフォーマット…(２つある内の下で「…」の方) > markdownlint
```

### ファイル保存時に修正する

```text
Markdownファイルを全て選択 > 右クリック > ドキュメントのフォーマット…(２つある内の下で「…」の方) > 既定のフォーマッタ…変更
```

![markdown-defaultFormatter](./images/markdown-defaultFormatter.png)

デフォルト設定が成功するとユーザー指定の`setting.json`に以下が反映される。(他の言語の場合も同様)

```json
  "[markdown]": {
    "editor.defaultFormatter": "DavidAnson.vscode-markdownlint"
  },
```

もし、`markdown-all-in-one`　に変更すると変更されます。

```json
  "[markdown]": {
    "editor.defaultFormatter": "yzhang.markdown-all-in-one"
  },
```

!!! info
    - もし、実行されない場合は`Editor: Format On Save`が有効になっているか確認してください。
    - settigs.json: `"editor.formatOnSave": true,`

## 多言語指向フォーマッタ

markdownlintはMarkdown向けのフォーマッタですが、htmlやjavascriptなどに対応した[Prettier](https://prettier.io/)という拡張機能もあります。

## 使い方

markdownlintの使い方と同様です。

!!! info
    - フォマート対象にはMarkdownも含まれますが、いくつか意図しない変換がされないケースがあります。(設定次第では回避できる可能性はありますが、未確認です。)
    - Markdownファイルをフォーマットする場合は、markdownlintが良いと思います。
