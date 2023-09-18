# setting

vscodeの設定関連についてまとめます。

## 設定ファイル(ユーザー/ワークスペース)

以下のいずれか。

- コマンドパレット(Mac: Command + Shift + P / Windows: Ctrl + Shift + P)から`settings.json`を検索し、設定(json)を開くを押下する。
- ショートカットキー(Mac: command + , / Windows: Ctrl + ,)でユーザーまたはワークスペースを開く

### Fileパス

#### Reference(Japanese)

[VS Code の設定ファイルの場所 (settings.json)](https://maku.blog/p/tfq2cnw/#%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E8%A8%AD%E5%AE%9A%E3%81%A8%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E8%A8%AD%E5%AE%9A)

#### ユーザー

|OS| ユーザー設定ファイルのパス|
| ---- | ---- |
|Windows |%APPDATA%\\Code\\User\\settings.json|
|macOS |$HOME/Library/Application Support/Code/User/settings.json|
|Linux |$HOME/.config/Code/User/settings.json|

#### ワークスペース

`<project root>/.vscode/settings.json`.

## .git

設定 > ワークスペース(検索:`Exclude`) > ファイルから`**/.git`を`X`(除外項目を削除)を押す
