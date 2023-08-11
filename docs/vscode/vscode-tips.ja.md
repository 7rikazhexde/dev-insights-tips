# Visual Studio Code(VsCode) tips

vscode関連のtipsをまとめてます。

## 設定ファイル

### `.vscode/settings.json`

#### 隠しファイル表示

##### .git

設定>ワークスペース(検索:`Exclude`)>ファイルから`**/.git`を`X`(除外項目を削除)を押す

## 拡張機能まとめ(用途別)

### マークダウンファイル(.md)の目次作成

「Markdown All in One - Web」を使用する。<br />
コマンドパレットを起動して、「Markdown All in One: 目次（TOC）の作成」を実行する。

以下のように目次（一部省略）が作られる。

```bash
- [vscode-tips](#vscode-tips)
  - [Table Of Contents](#table-of-contents)
  - [拡張機能まとめ(用途別)](#拡張機能まとめ用途別)
    - [マークダウンファイル(.md)の目次作成](#マークダウンファイルmdの目次作成)
```

デフォルトではタイトルと目次も出力される。<br />
設定ではプロジェクトファイルの目次（TOC）で除外する見出しの一覧を設定できるが、文言はプロジェクトで変わるので設定はできない？正規表現が使えればできそすが未確認です。

```bash
Markdown › Extension › Toc: Omitted From Toc
```

もしタイトルと目次が不要ならば削除して字上げをすれば良い。

Windowsの場合:

- インデントのレベルを下げる：「Ctrl+\]」 or 「Tab」
- インデントのレベルを上げる：「Ctrl＋\[」 or 「Tab＋Shift」

もしくはテキストを矩形選択して調整すれば良い。

参考： [VS Codeでテキストを矩形選択するには](https://atmarkit.itmedia.co.jp/ait/articles/1805/11/news022.html)
