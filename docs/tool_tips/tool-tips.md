# tool-tips

個人が利用しているツールをまとめです。

[Top.mdに戻る](../index.md)

## Table of Contents

- [tool-tips](#tool-tips)
  - [Table of Contents](#table-of-contents)
  - [Workflowy](#workflowy)
    - [ダウンロードリンク](#%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%83%AA%E3%83%B3%E3%82%AF)
    - [使い方](#%E4%BD%BF%E3%81%84%E6%96%B9)
      - [デザイン変更](#%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E5%A4%89%E6%9B%B4)
  - [obsidian](#obsidian)
    - [ダウンロードリンク](#%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%83%AA%E3%83%B3%E3%82%AF-1)
    - [使い方](#%E4%BD%BF%E3%81%84%E6%96%B9-1)
      - [プラグインの追加](#%E3%83%97%E3%83%A9%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%AE%E8%BF%BD%E5%8A%A0)

## Workflowy

アウトライナーツール\
文章に特化していてフォルダもないので管理に悩まないのが特徴

### ダウンロードリンク

[https://workflowy.com/downloads/windows/](https://workflowy.com/downloads/windows/)

### 使い方

アプリをDLするか、ブラウザからアクセスしてHOME以下に文章を書いていく。\
ただし、全ての文章はHOMEに集約されるので縦長になるので、タグ(#,@)を利用することでタグ管理できるので。必要に応じてカテゴライズすると良い。

#### デザイン変更

デフォルトだと白背景なので、画面右上の三点リーダー縦（︙）から以下Themeで変更できる。

```
setting > Appearance > Theme > Dark
```

## obsidian

Markdownツール

### ダウンロードリンク

[https://obsidian.md/download](https://obsidian.md/download)

### 使い方

ファイルは最初に設定した保管庫(Vault)に保存されるがWindowsとiOSを使う場合はiCloud（※）に設定するとそれぞれのOSで共有できるようになる。\
現状、保存先をiCloudにしない場合は月額のクラウド版を利用するしかない。\
※Windowsでは[Windows 用 iCloud](https://support.apple.com/ja-jp/HT204283) をダウンロードする必要がある。

#### プラグインの追加

obsidianではプラグインが公開されている。\
以下設定を変更してプラグインの検索とインストールをすることができる。

```bash
Settings > Third-party plugins > Community Plugins > Browse and search for PlantUML
```

例えば、UMLはデフォルトだと描画されないのでPlantUMLインストールして有効化すると描画できるようになる。
