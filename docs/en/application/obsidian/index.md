# Obsidian tips

This section summarizes information related to Obsidian.

## Obsidian

A markdown editor application that can structure and decorate documents according to a "markdown" format.

### Download Link

[https://obsidian.md/download](https://obsidian.md/download)

### Usage

Files are stored in the vault you initially set up, but if you use Windows and iOS, you can set it to iCloud[^1] so that you can share it with each OS.(Unconfirmed, but I believe it is also possible with Google Drive and OneDrive.)

Currently, if you do not choose iCloud as the storage location, you can only use the monthly cloud version.

[^1]: For Windows, you need to download [iCloud for Windows](https://support.apple.com/ja-jp/HT204283).

#### Adding Plug-ins

Plug-ins are available at obsidian.<br />
You can search for and install plug-ins from `Community Plugins` to use useful features.

```bash
Settings > Third-party plugins > Community Plugins > Browse
```

!!! info
    The following are plug-ins that I personally recommend.

##### [PlantUML](./community_plugins/plantuml.md)

Render PlantUML Diagrams in Obsidian.

##### [Recent Files](https://github.com/tgrosinger/recent-files-obsidian?tab=readme-ov-file#recent-files-for-obsidian)

> This plugin displays a list of most recently opened files in the sidebar. Optionally include paths of files which should be excluded from the list.

##### [Mind Map](https://github.com/lynchjames/obsidian-mind-map?tab=readme-ov-file#obsidian-mind-map)

This plugin displays a mind map format based on multiple headings (#). It can be displayed with the following specification.

`Open command palette > Mind Map: Preview the current note as a Mind Map`

##### [Auto Template Trigger](./community_plugins/auto_template_trigger.md)

Plug-in that allows you to select a pre-made format (`Core plugins > Templates`) to run when creating notes.

##### [Daily Notes Editor](https://github.com/Quorafind/Obsidian-Daily-Notes-Editor?tab=readme-ov-file#daily-notes-editor)

> A plugin for you to edit a bunch of daily notes in one page(inline), which works similar to Roam Research's default daily note view.

`Daily Notes Editor` is a plugin that allows the `Open Daily Notes Editor` to retrieve and scroll through each file specified in `YYYYY-MM-DD.md` by default.
