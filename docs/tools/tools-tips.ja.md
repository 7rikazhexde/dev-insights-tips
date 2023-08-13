# Tools tips

個人で利用しているツールを紹介します。

## Workflowy

アウトライナーツール<br />
文章に特化していてフォルダもないので管理に悩まないのが特徴

### ダウンロードリンク

[https://workflowy.com/downloads/windows/](https://workflowy.com/downloads/windows/)

### 使い方

アプリをDLするか、ブラウザからアクセスしてHOME以下に文章を書いていく。<br />
ただし、全ての文章はHOMEに集約されるので縦長になるので、タグ(#,@)を利用することでタグ管理できるので。必要に応じてカテゴライズすると良い。

#### デザイン変更

デフォルトだと白背景なので、画面右上の三点リーダー縦（︙）から以下Themeで変更できる。

```text
setting > Appearance > Theme > Dark
```

## obsidian

「マークダウン」のフォーマットによってドキュメントの構造化や装飾などを行うことのできるマークダウンエディタアプリ。

### ダウンロードリンク

[https://obsidian.md/download](https://obsidian.md/download)

### 使い方

ファイルは最初に設定した保管庫(Vault)に保存されるがWindowsとiOSを使う場合は\[iCloud\]\[1\]に設定するとそれぞれのOSで共有できるようになる。

現状、保存先をiCloudにしない場合は月額のクラウド版を利用するしかない。

\[1\]:Windowsでは[Windows 用 iCloud](https://support.apple.com/ja-jp/HT204283) をダウンロードする必要がある。

#### プラグインの追加

obsidianではプラグインが公開されている。<br />
以下設定を変更してプラグインの検索とインストールをすることができる。

```bash
Settings > Third-party plugins > Community Plugins > Browse and search for PlantUML
```

例えば、UMLはデフォルトだと描画されないのでPlantUMLインストールして有効化すると描画できるようになる。
