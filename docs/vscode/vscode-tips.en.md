# Visual Studio Code(VsCode) tips

This section summarizes information related to vscode.

## setting file

### `.vscode/settings.json`

#### hidden file view

##### .git

Settings>Workspace(Search:`Exclude`)>Press `X`(remove excluded items) for `**/.git` from file

## Extension Summary (by use)

### Creating a table of contents for markdown files (.md)

Use "Markdown All in One - Web".<br />
Launch the command palette and execute "Markdown All in One: Create Table of Contents (TOC)".

A table of contents (some parts are omitted) will be created as follows.

```bash
- [vscode-tips](#vscode-tips)
  - [Table Of Contents](#table-of-contents)
  - [拡張機能まとめ(用途別)](#拡張機能まとめ用途別)
    - [マークダウンファイル(.md)の目次作成](#マークダウンファイルmdの目次作成)
```

By default, the title and table of contents are also output.<br />
In the settings, you can set a list of headings to be excluded from the table of contents (TOC) of the project file, but the wording changes from project to project, so it is not possible to set the wording? If regular expressions can be used, it may be possible, but I have not tested it yet.

```bash
Markdown › Extension › Toc: Omitted From Toc
```

If the title and table of contents are not needed, they can be deleted and lettered up.

In Windows:

- Decrease the level of indentation: "Ctrl+\]" or "Tab
- Increase the level of indentation: "Ctrl+\[" or "Tab+Shift

Or you can select a rectangle of text and adjust it.

Reference(Japanese： [VS Codeでテキストを矩形選択するには](https://atmarkit.itmedia.co.jp/ait/articles/1805/11/news022.html)
