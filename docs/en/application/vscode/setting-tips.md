# setting

This section summarizes information related to vscode / setting.

## setting file(user/workspace)

Either of the following

- Search for `settings.json` in the command palette (Mac: Command + Shift + P / Windows: Ctrl + Shift + P) and press Open Settings (json).
- Open a user or workspace with the shortcut keys (Mac: Command + , / Windows: Ctrl + ,)

### File path

#### 参考記事

[VS Code の設定ファイルの場所 (settings.json)](https://maku.blog/p/tfq2cnw/#%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E8%A8%AD%E5%AE%9A%E3%81%A8%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E8%A8%AD%E5%AE%9A)

#### User

|OS| User configuration file path(settings.json)|
| ---- | ---- |
|Windows |%APPDATA%\\Code\\User\\settings.json|
|macOS |$HOME/Library/Application Support/Code/User/settings.json|
|Linux |$HOME/.config/Code/User/settings.json|

#### Workspace

`<project root>/.vscode/settings.json`

## .git

Settings > Workspace(Search:`Exclude`) > Press `X`(remove excluded items) for `**/.git` from file
