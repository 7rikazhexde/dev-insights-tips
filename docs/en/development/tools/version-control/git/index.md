---
title: Git
tags:
  - Git
description: Git
---

This section summarizes information related to git.

## Basic Flow

The general flow of pushing code to a remote repository using Git is as follows.

### Initialize or clone the repository

If you already have a remote repository, use the `git clone` command to clone the existing repository locally.<br />
To create a new repository, use the `git init` command to initialize the new repository.

### Staging

Add the modified file to the staging area.<br />
This is preparatory work before committing your changes.<br />
To stage all changes, use the `git add .`command to stage all changes.<br />
To stage only specific files, use the `git add filename` command.

### Commit

Commit the changes you have added to the staging area. This will record the changes in the repository history.<br />
Use the `git commit -m "commit message"` command to create a commit. The commit message is a description of the change.

### Remote Repository Settings

Add a remote repository. Usually, this remote repository is on a hosting service such as GitHub or GitLab.<br />
Use the `git remote add origin remote repository URL` command to add a remote repository. origin" is the name of the reference to the remote repository.

### Push

Push local commits to the remote repository. This will push changes to the remote repository.
Use the `git push origin branch name` command to push changes on a specified branch to the remote repository.
Here, branch name is the name of the branch you are pushing to. By default, this is usually main or master.

## Details for each command

### Staging(git add)

git add is a command that adds files you have modified in Git to the staging area (index). You can see the files and folders you have changed with the `git status` command. By adding a file to the staging area, Git treats that change as the subject of the next commit.

```bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
(use "git push" to publish your local commits)

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified:   folder/file3.txt
modified:   folder/file4.txt
modified:   file1.txt
```

This example display contains the following information

- A line indicating that the current branch is `main`.
- A line indicating that the branch is one commit ahead of the `origin/main` branch.
- A list of files whose changes have not been staged. Lines indicating that changes to `folder/file3.txt`,`folder/file4.txt`, and `file1.txt` have not yet been staged.
- A message indicating that the changes have not been staged.

From this output, you can see the change status of the files in the working tree. Before committing these changes, you can use the `git add` command to stage the necessary changes.

The `git add` command is used as follows

```bash
git add folder/file3.txt
```

If multiple files are to be added to the staging area, multiple files can be specified in the `git add` command.

```bash
git add folder/file3.txt folder/file4.txt file1.txt
```

You can also specify a directory to add all changes in that directory to the staging area at once.

```bash
git add folder/
```

If you want to stage all the files that you have changed, you can run the command under the project (**. refers to the current directory**), execute the command

```bash
git add .
```

Files added to the staging area can be committed to the local repository by running the `git commit` command.

### Undo staging (git reset)

The `git reset` command can be used to undo files added to the staging area (index).

First, check the files added to the staging area with the `git status` command.

```bash
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
new file:   folder/file3.txt
modified:   folder/file4.txt
modified:   file1.txt
```

Use the `git reset` command to cancel files added to the staging area.

```bash
git reset HEAD folder/file3.txt folder/file4.txt file1.txt
```

The `HEAD` refers to the latest commit. You can undo changes added to the staging area by specifying HEAD to the `git reset` command.

If no file is specified, all files can be undone from the staging area.

```bash
git reset HEAD
```

Thus, the `git reset` command can be used to undo changes to files that have been added to the staging area. However, the undone changes will remain in the working directory. If necessary, you can also use the `git restore` command to undo changes in the working directory.

Note that if you do not specify HEAD for the `git reset` command, the commit history is not changed, but you can undo changes to files from the staging area. Specifically, changes to files that are undone from the staging area are returned to the working directory. **But note that the commit history is not changed.**

## Revert changes in the working tree (git restore command)

The `git restore` command is used to restore changes from the working tree to the staging area or from the staging area to the commits. Specifically, it can be used as follows.

```bash
git restore file.txt
```

Changes to `file.txt` in the staging area are undone and the \*\*file reverts to the state of the previous commit. \*\*

If you added a file to the staging area with the `git add` command, but want to revert it, use `git restore --staged`.

For example, if you added the `file1.txt` file to the staging area and want to revert the changes, use

```bash
git add file1.txt     # Add changes to staging area
git restore --staged file1.txt  # Return changes from staging area
```

The `--satge` option will undo \*\*changes to `file.txt` in the staging area, but the file itself will remain unchanged. \*\*
That is, the changes remain in the staging area.

## git commit

### basic form

The git commit command is used to commit changes to a local repository.<br />
Below is an example of a basic git commit command.

```bash
git commit -m "Add new feature"
```

### Example using commit type and emojis

Whether or not to include a space after the emoji depends on the style of the commit message and the guidelines of the project. Some projects may require a space after the emoji in the commit message, but generally spaces are often omitted.

```bash
git commit -m ":+1:feat: Add new feature"
```

### commit type

A commit type refers to a generic identifier used to succinctly describe the purpose of a commit.<br />
The commit type helps other developers understand the purpose of the developer's modification of the code.

Common commit types include the following

- feat: used when a new feature is added.
- fix: Used to fix bugs.
- docs: Used for document changes.
- style: Used when you have made changes to the style of the code (spacing, formatting, etc.).
- refactor: Used when you have made changes that do not change the functionality of the code.
- test: Used when changes are made to the test code.
- chore: Used when changes are made to the build process or auxiliary tools.

For example, when modifying the README.md file, the commit type is "docs". Therefore, the commit message would be as follows.

```bash
docs: Update README.md with new information
```

This allows other developers to understand that this commit updates the documentation in the README.md file.

### commit message

There are several elements in the commit message that can be used to add details

- Scope: an optional element that indicates the scope affected by the commit. This element can be used to specify the files, modules, functions, etc. that the commit modifies.

In the case of modifying the README.md file, the scope is the README. Therefore, the commit message would be as follows.

```bash
docs(README): Update README.md with new information
```

- Subject: A required element that gives a brief summary of the commit. It is written on the first line of the commit message.

Example: If the subject is about modifying the README.md file, the subject would be about the updated information. Therefore, the commit message would look like this

```bash
docs(README): Update README.md with new information
```

- Body: An optional element detailing the commit.
  This element is used to describe the details of the changes made by the commit, background, reasons, etc.

Example: In the case of a modification to the README.md file, the body can include a detailed description of the new information. Thus, the commit message would look like this

```bash
docs(README): Update README.md with new information

Add a new section to the README.md file describing the new features
that have been added to the application. This should help users to
better understand how to use the application and take advantage of
its latest features.
```

- Footer: An optional element indicating metadata about the commit.
  This element is used to indicate the associated Issue number, significant changes, destructive changes, etc.

Example: In the case of a modification to the README.md file, the footer may include the associated Issue number. Thus, the commit message would look like this

```bash
docs(README): Update README.md with new information

Add a new section to the README.md file describing the new features
that have been added to the application. This should help users to
better understand how to use the application and take advantage of
its latest features.

Issue #123
```

### Example of adding commit type and git message

This example specifies "search" as the scope and uses a commit type of "feat" to indicate that a new feature has been added. The body describes the changes in detail, and the footer describes the associated issue number as "Closes #1234." This clearly indicates which issue this commit is related to and facilitates collaboration across the team.

```bash
git commit -m "feat(search): add fuzzy search to search bar

This commit adds fuzzy search functionality to the search bar component. Fuzzy search allows users to find search results even if they make spelling mistakes or typos. This feature will enhance the user experience and make it easier to find what they are looking for.

Closes #1234"
```

### Commit Message Templates

#### How to specify a commit message template

In the git commit command, the -t option can be used to specify a commit message template.

##### Example template for docs

This example template includes scope, commit type, changes, and test method to create a more detailed commit message.

Contents of docs_gt

```bash
docs(README): Update README.md with new information

Add a new section to the README.md file describing the new features
that have been added to the application. This should help users to
better understand how to use the application and take advantage of
its latest features.

Issue #[]
Closes #[]
Refs #[]
```

Specified with the -t option at commit time

```bash
git commit -t ~./git_message_template/docs_gt
```

#### Template settings for commit messages to be used by default

By specifying a path in commit.template, the file specified in that path can be used as the default commit message template.

Reference：[Gitコミットスタイル](https://zenn.dev/ianchen0419/articles/99564425e43dd4)

##### Creating a .gitmessage

```bash
mkdir ~/.git_message_template
touch ~/.git_message_template/.gitmessage
```

```text
# ==== Prefix ====
# fix       バグ修正、クリティカルなバグ修正なら hotfix
# feat      feat は feature の略
# docs      ドキュメントのみ修正
# style     空白、セミコロン、行、コーディングフォーマットなどの修正
# refactor  整理 （リファクタリング等）
# test      テスト追加や間違っていたテストの修正
# chore     ビルドツールやライブラリで自動生成されたものをコミットするとき

# ==== Emojis ====
# :bug:         バグ修正 (fix)
# :+1:          機能改善 (fix/feat)
# :sparkles:    部分的な機能追加 (feat)
# :tada:        盛大に祝うべき大きな機能追加 (feat)
# :rocket:      パフォーマンス改善 (feat)
# :lock:        新機能の公開範囲の制限 (feat)
# :cop:         セキュリティ関連の改善 (feat)
# :note:        ドキュメント修正 (docs)
# :shirt:       Lintエラーの修正やコードスタイルの修正 (style)
# :recycle:     リファクタリング (refactor)
# :shower:      不要な機能・使われなくなった機能の削除 (refactor)
# :green_heart: テストやCIの修正・改善 (test)
# :up:          依存パッケージなどのアップデート (chore)
```

Specify the path to the template file to be used at commit time in Git's global configuration with the `git config --global` command.

```bash
git config --global commit.template ~/.git_message_template/.gitmessage
```

If commit.template is set, the template will be automatically loaded and displayed as the initial text of the editable commit message when the git commit command is executed.

In the case of vscode, it will be displayed by default on COMMIT_EDITMSG when you commit after staging changes.

Note that, as with the --template option, the commit.template setting will be overwritten if another template file is specified with the -t option when the git commit command is executed.

```bash
$ git commit -t $HOME/.git_message_template/.docs_gt
Aborting commit; you did not edit the message. # If no overwrite save

$ git commit -t $HOME/.git_message_template/.docs_gt
[main e4db099] docs(README): Update README.md with new information
1 file changed, 106 insertions(+), 1 deletion(-)
```

#### 【GitHub】About the display of GitHub after git commit / push

##### When you write the issue number (with #) of the forked source on git commit, it is automatically converted to a URL with the title "account name# issue number"

[参考](https://github.com/7rikazhexde/twitter-video-dl-for-sc/commit/08c13970a84804e48c80d589002189e452cb8183)

## Undo a commit after git commit (git reset / git revert)

To undo a commit after a `git commit`, the `git reset` command is generally used. Be careful, however, as undoing a commit may affect your ability to work with other developers and remote repositories. The following describes how to undo a commit.

### Reference(Japanese)

- [git resetでどのオプション(hard, mixed, soft)を指定すべきか、シチュエーション別に分けてみる](https://qiita.com/kmagai/items/6b4bfe3fddb00769aec4)
- [【Git】git reset --soft、--mixed、--hardの違い](https://naomi-homma.hatenablog.com/entry/2020/08/11/170039)

### Only HEAD is restored.

```bash
git reset --soft HEAD^
```

This command undoes the previous commit and returns the changes to the staging area, retaining the commit message. After this, the changes can be modified and re-committed.

### HEAD, restore index

```bash
git reset --mixed HEAD^
```

This command undoes the commit, returns the changes to the working directory, and removes them from the staging area. The commit is not removed from the history, but the changes are retained as unstaged.

### HEAD, index, and working tree all restored

```bash
git reset --hard HEAD^
```

This command completely undoes the previous commit and its changes, and also restores the working tree to its pre-modified state. Note that, once undone, commits and changes cannot be restored.

### Undo a specific commit

```bash
git revert <commit-hash>
```

The `git revert` command creates a new commit that undoes the changes in a given commit. This not only undoes the changes, but also records them in the history. This is a way to undo changes while still keeping up with other developers.

### Changing commit messages

The following method overwrites the commit history with the changed commit message.

```bash
touch new_file.txt
git add new_file.txt
git commit -m "Add new_file.txt"
# Change the contents of new_file.txt
git add new_file.txt
git commit --amend -m "Modify new_file.txt and update commit message"
```

## 【GitHub】About Project Forking

Forking a project on GitHub allows you to copy the original repository and bring it to your own GitHub account.<br />
Below are the etiquette, precautions, and methods for forking.

### Etiquette

- As a general rule, it is advisable to check the license of the project to be forked and properly credit it.
- When contributing to a forked project, be sure to follow the same proper development process as for the original project.

### Note

- Make sure you understand and comply with the license, including the project from which you are forking.
- If the project from which you are forking is updated, synchronize regularly to ensure that you are using the latest code.

### Usage

1. Log in to GitHub and access the repository of the project you wish to fork.
1. Click the "Fork" button in the upper right corner.
1. A copy of the forked repository will be created in your GitHub account.
1. Make the necessary modifications to the copied repository and commit.

## How to incorporate changes in the fork source

### Add the forked repository to the remote

```bash
git remote add upstream <フォーク元のリポジトリのURL>
```

### Update local forked repositories

```bash
git fetch upstream
```

### Merge changes from the fork source

```bash
git merge upstream/<Branch name to import changes into>
```

#### To rebase, execute the following command

```bash
git rebase upstream/<Branch name to import changes into>
```

### Conflict Resolution

If conflicts arise when merging or rebasing changes, they must be resolved manually. The method of resolving conflicts depends on the nature of the change.

### Push changes

After merging or rebasing the changes, push the changes to the forked repository.

```bash
git push origin <Remote destination branch name>
```

By following these steps, you can incorporate the changes from the forked source into your own forked repository.
