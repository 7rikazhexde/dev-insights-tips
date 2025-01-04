---
title: Obsidian
tags:
description: Obsidian関連のtipsをまとめてます。
---

## Obsidian

「マークダウン」のフォーマットによってドキュメントの構造化や装飾などを行うことのできるマークダウンエディタアプリ。

### ダウンロードリンク

[https://obsidian.md/download](https://obsidian.md/download)

### 使い方

ファイルは最初に設定した保管庫(Vault)に保存されるがWindowsとiOSを使う場合はiCloud[^1]に設定するとそれぞれのOSで共有できるようになる。(未確認ですが、Google Drive,OneDriveでも可能だと思います。)

現状、保存先をiCloudにしない場合は月額のクラウド版を利用するしかない。

[^1]: Windowsでは[Windows 用 iCloud](https://support.apple.com/ja-jp/HT204283) をダウンロードする必要がある。

#### プラグインの追加

obsidianではプラグインが公開されている。<br />
`Community Plugins`からプラグインを検索、インストールすることで便利な機能を使用することができる。

```bash
Settings > Third-party plugins > Community Plugins > Browse
```

!!! info
    以下は個人的におすすめするプラグインです。

##### [PlantUML](./community_plugins/plantuml.md)

Render PlantUML Diagrams in Obsidian.

##### [Recent Files](https://github.com/tgrosinger/recent-files-obsidian?tab=readme-ov-file#recent-files-for-obsidian)

> This plugin displays a list of most recently opened files in the sidebar. Optionally include paths of files which should be excluded from the list.

##### [Mind Map](https://github.com/lynchjames/obsidian-mind-map?tab=readme-ov-file#obsidian-mind-map)

複数の見出し(#)を元にマインドマップ形式で表示するプラグインです。以下の指定で表示できます。

`Open command palette > Mind Map: Preview the current note as a Mind Map`

##### [Auto Template Trigger](./community_plugins/auto_template_trigger.md)

ノート作成時に事前に作成したフォーマット(`Core plugins > Templates`)を選択して実行できるプラグイン

##### [Daily Notes Editor](https://github.com/Quorafind/Obsidian-Daily-Notes-Editor?tab=readme-ov-file#daily-notes-editor)

> A plugin for you to edit a bunch of daily notes in one page(inline), which works similar to Roam Research's default daily note view.

`Daily Notes Editor`は`Open Daily Notes Editor`でデフォルトで`YYYYY-MM-DD.md`に指定されている各ファイルを取得してスクロール表示できるようにするプラグインである。
