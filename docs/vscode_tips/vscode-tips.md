# vscode-tips

vscode関連のtipsをまとめてます。

[Top.mdに戻る](../index.md)

## Table Of Contents

- [vscode-tips](#vscode-tips)
  - [Table Of Contents](#table-of-contents)
  - [拡張機能まとめ(用途別)](#%E6%8B%A1%E5%BC%B5%E6%A9%9F%E8%83%BD%E3%81%BE%E3%81%A8%E3%82%81%E7%94%A8%E9%80%94%E5%88%A5)
    - [マークダウンファイル(.md)の目次作成](#%E3%83%9E%E3%83%BC%E3%82%AF%E3%83%80%E3%82%A6%E3%83%B3%E3%83%95%E3%82%A1%E3%82%A4%E3%83%ABmd%E3%81%AE%E7%9B%AE%E6%AC%A1%E4%BD%9C%E6%88%90)

## 拡張機能まとめ(用途別)

### マークダウンファイル(.md)の目次作成

「Markdown All in One - Web」を使用する。\
コマンドパレットを起動して、「Markdown All in One: 目次（TOC）の作成」を実行する。

以下のように目次（一部省略）が作られる。

```bash
- [vscode-tips](#vscode-tips)
  - [Table Of Contents](#table-of-contents)
  - [拡張機能まとめ(用途別)](#拡張機能まとめ用途別)
    - [マークダウンファイル(.md)の目次作成](#マークダウンファイルmdの目次作成)
```

デフォルトではタイトルと目次も出力される。\
設定ではプロジェクトファイルの目次（TOC）で除外する見出しの一覧を設定できるが、文言はプロジェクトで変わるので設定はできない？正規表現が使えればできそうだが未確認。\
Markdown › Extension › Toc: Omitted From Toc

もしタイトルと目次が不要ならば削除して字上げをすれば良い。

Windowsの場合\
インデントのレベルを下げる：「Ctrl + \]」 or 「Tab」\
インデントのレベルを上げる：「Ctrl ＋ \[」 or 「Tab ＋ Shift」

もしくはテキストを矩形選択して調整すれば良い。\
参考： [VS Codeでテキストを矩形選択するには](https://atmarkit.itmedia.co.jp/ait/articles/1805/11/news022.html)
