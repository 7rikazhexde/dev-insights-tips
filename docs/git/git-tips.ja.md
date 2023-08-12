# git tips

git関連のtipsです。

## 基本的な流れ

Gitを使用してコードをリモートリポジトリにプッシュする一般的な流れは以下の通りです。

### リポジトリの初期化またはクローン

リモートリポジトリを既に持っている場合は、git clone コマンドを使用して既存のリポジトリをローカルに複製します。<br />
新しいリポジトリを作成する場合は、`git init`コマンドを使用して新しいリポジトリを初期化します。

### ファイルのステージング

変更したファイルをステージングエリアに追加します。これは、変更をコミットする前の準備作業です。<br />
すべての変更をステージングするには、`git add .`コマンドを使用します。<br />
特定のファイルのみをステージングするには、`git add ファイル名`コマンドを使用します。

### コミット

ステージングエリアに追加した変更をコミットします。これにより、変更がリポジトリの履歴に記録されます。<br />
`git commit -m "コミットメッセージ"`コマンドを使用してコミットを作成します。コミットメッセージはその変更の内容を説明するためのものです。

### リモートリポジトリの設定:

リモートリポジトリを追加します。通常、このリモートリポジトリは GitHub や GitLab などのホスティングサービス上にあります。
`git remote add origin リモートリポジトリのURL` コマンドを使用してリモートリポジトリを追加します。"origin" はリモートリポジトリへの参照の名前です。

### プッシュ

ローカルのコミットをリモートリポジトリにプッシュします。これにより、リモートリポジトリに変更が反映されます。
`git push origin ブランチ名` コマンドを使用して、指定したブランチの変更をリモートリポジトリにプッシュします。
ここで ブランチ名 はプッシュする対象のブランチの名前です。デフォルトでは、通常は main や master といった名前になります。

## コマンド毎の詳細

### ステージング(git add)

git addは、Gitで変更したファイルをステージングエリア（インデックス）に追加するコマンドです。変更したファイル、フォルダは`git status`コマンドで確認できます。ステージングエリアにファイルを追加することで、Gitはその変更を次のコミットの対象として扱います。

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

この表示例では、以下の情報が含まれています：

- 現在のブランチが `main`ブランチであることを示す行。
- ブランチが`origin/main`ブランチよりも 1コミット進んでいることを示す行。
- 変更がステージングされていないファイルの一覧。`folder/file3.txt`,`folder/file4.txt`、`file1.txt`の変更がまだステージングされていません。
- 変更がステージングされていないことを示すメッセージ。

この出力から、ワーキングツリー内のファイルの変更状態がわかります。これらの変更をコミットする前に、必要な変更をステージングするために `git add`コマンドを使用することができます。

git addコマンドは、次のように使用します。

```bash
git add folder/file3.txt
```

複数のファイルをステージングエリアに追加する場合は、`git add`コマンドに複数のファイルを指定することができる。

```bash
git add folder/file3.txt folder/file4.txt file1.txt
```

また、ディレクトリを指定することで、そのディレクトリ内のすべての変更を一度にステージングエリアに追加することもできる。

```bash
git add folder/
```

もし、変更したすべてのファイルをステージングしたい場合はプロジェクト以下(**.はカレントディレクトリを指す**)をコマンドを実行する

```bash
git add .
```

ステージングエリアに追加されたファイルは、`git commit`コマンドを実行することで、ローカルリポジトリにコミットすることができる。

### ステージングの取り消し(git reset)

ステージングエリア（インデックス）に追加したファイルを取り消す方法は、`git reset`コマンドを使用することができる。

まず、`git status`コマンドで、ステージングエリアに追加されたファイルを確認します。

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

`git reset`コマンドを使用して、ステージングエリアに追加したファイルを取り消します。

```bash
git reset HEAD folder/file3.txt folder/file4.txt file1.txt
```

`HEAD`は、最新のコミットを指す。`git reset`コマンドにHEADを指定することで、ステージングエリアに追加された変更を取り消すことができる。

ファイル指定しない場合はステージングエリアからすべてのファイルを取り消すことができる。

```bash
git reset HEAD
```

このように、`git reset`コマンドを使用することで、ステージングエリアに追加したファイルの変更を取り消すことができる。ただし、取り消した変更は作業ディレクトリに残ります。必要に応じて、`git restore`コマンドを使用して作業ディレクトリの変更を取り消すこともできる。

なお、git resetコマンドにHEADを指定しない場合、コミットの履歴は変更されませんが、ステージングエリアからファイルの変更を取り消すことができる。具体的には、ステージングエリアから取り消されたファイルの変更は、作業ディレクトリに戻される。**ただし、コミットの履歴は変更されないため、注意が必要。**

## ワーキングツリー内の変更を取り消す(git restoreコマンド)

`git restore`コマンドは、ワーキングツリーからステージングエリアに変更を戻したり、ステージングエリアからコミットに変更を戻すために使用される。具体的には、次のような使い方ができる。

```bash
git restore file.txt
```

ステージングエリアにある `file.txt`の変更が取り消され、**ファイルは以前のコミットの状態に戻ります。**

`git add`コマンドでファイルをステージングエリアに追加したが、戻したい場合は、`git restore --staged`を使用します。

例えば、`file1.txt`ファイルをステージングエリアに追加し、変更を戻したい場合は、次のようにする。

```bash
git add file1.txt     # ステージングエリアに変更を追加
git restore --staged file1.txt  # ステージングエリアから変更を戻す
```

`--satge`オプションを指定することにより、ステージングエリアにある `file.txt`の**変更は取り消されますが、ファイル自体は変更されたままです。**
つまり、変更はステージングエリア内に残ります。

## git commitコマンド

### 基本形

git commit コマンドは、ローカルリポジトリに変更をコミットするために使用されます。<br />
以下は、基本的な git commit コマンドの例。

```bash
git commit -m "Add new feature"
```

### commit typeとemojisを使用した例

emojiの後ろにスペースを入れるかどうかは、コミットメッセージのスタイルやプロジェクトのガイドラインによります。一部のプロジェクトでは、コミットメッセージに絵文字の後ろにスペースを入れることを求める場合がありますが、一般的にはスペースを省略することが多いようです。

```bash
git commit -m ":+1:feat: Add new feature"
```

### commit type

commit typeは、コミットの目的を簡潔に表すために使用される、一般的な識別子のことを指す。<br />
コミットタイプは、開発者がコードを修正する目的を他の開発者が理解しやすくするのに役立つ。

一般的なコミットタイプには、以下のようなものがある。

- feat：新しい機能を追加した場合に使用します。
- fix：バグ修正のために使用します。
- docs：ドキュメントを変更した場合に使用します。
- style：コードのスタイルに関する変更（スペース、フォーマットなど）を行った場合に使用します。
- refactor：コードの機能を変更しない変更を行った場合に使用します。
- test：テストコードに関する変更を行った場合に使用します。
- chore：ビルドプロセスや補助ツールの変更を行った場合に使用します。

例えば、README.mdファイルを修正する場合、コミットタイプは「docs」となる。そのため、コミットメッセージは以下のようになる。

```bash
docs: Update README.md with new information
```

これにより、他の開発者は、このコミットがREADME.mdファイルのドキュメントを更新したことを理解できる。

### commit message

コミットメッセージには、詳細を追加するために使用できるいくつかの要素がある。

- Scope：コミットが影響を受ける範囲を示すオプションの要素。この要素は、コミットが変更を加えたファイルやモジュール、機能などを指定するために使用できる。

README.mdファイルの修正に関する場合、スコープはREADMEとなります。そのため、コミットメッセージは以下のようになる。

```bash
docs(README): Update README.md with new information
```

- Subject：コミットの簡潔な要約を示す必須要素。コミットメッセージの最初の行に書かれる。

例：README.mdファイルの修正に関する場合、サブジェクトは更新された情報に関するものになる。そのため、コミットメッセージは以下のようになる。

```bash
docs(README): Update README.md with new information
```

- Body：コミットの詳細を示すオプションの要素。
  この要素は、コミットが行った変更の詳細や、背景、理由などを記述するために使用される

例：README.mdファイルの修正に関する場合、ボディには、新しい情報についての詳細な説明が含めることができる。そのため、コミットメッセージは以下のようになる。

```bash
docs(README): Update README.md with new information

Add a new section to the README.md file describing the new features
that have been added to the application. This should help users to
better understand how to use the application and take advantage of
its latest features.
```

- Footer：コミットに関するメタデータを示すオプションの要素。
  この要素は、関連するIssue番号、重要な変更、破壊的な変更などを示すために使用される。

例：README.mdファイルの修正に関する場合、フッターには、関連するIssue番号を含めることができる。そのため、コミットメッセージは以下のようにな。

```bash
docs(README): Update README.md with new information

Add a new section to the README.md file describing the new features
that have been added to the application. This should help users to
better understand how to use the application and take advantage of
its latest features.

Issue #123
```

### commit typeとgit messageを加えた例

この例では、スコープとして "search" を指定し、"feat" というコミットタイプを使用して、新しい機能が追加されたことを示している。ボディでは、変更内容の詳細が説明され、フッターでは関連する問題番号が "Closes #1234" として記述されている。これにより、このコミットがどの問題に関連しているのかを明確に示し、チーム全体でのコラボレーションをスムーズに進めることができ。

```bash
git commit -m "feat(search): add fuzzy search to search bar

This commit adds fuzzy search functionality to the search bar component. Fuzzy search allows users to find search results even if they make spelling mistakes or typos. This feature will enhance the user experience and make it easier to find what they are looking for.

Closes #1234"
```

### コミットメッセージのテンプレート

#### コミットメッセージのテンプレートを指定する方法

git commit コマンドでは、-t オプションを使用して、コミットメッセージのテンプレートを指定することができる。

##### docs用のテンプレート例

この例のテンプレートには、スコープ、コミットタイプ、変更内容、テスト方法などが含まれており、より詳細なコミットメッセージを作成することができる。

docs_gtの中身

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

コミット時に-tオプションで指定

```bash
git commit -t ~./git_message_template/docs_gt
```

#### デフォルトで使用するコミットメッセージのテンプレート設定

commit.template にパスを指定することで、そのパスで指定したファイルがデフォルトのコミットメッセージのテンプレートとして使用できる。

参考：[Gitコミットスタイル](https://zenn.dev/ianchen0419/articles/99564425e43dd4)

##### .gitmessageの作成

```bash
mkdir ~/.git_message_template
touch ~/.git_message_template/.gitmessage
```

```text
# ==== Prefix ====
# fix      バグ修正、クリティカルなバグ修正なら hotfix
# feat     feat は feature の略
# docs     ドキュメントのみ修正
# style    空白、セミコロン、行、コーディングフォーマットなどの修正
# refactor 整理 （リファクタリング等）
# test     テスト追加や間違っていたテストの修正
# chore    ビルドツールやライブラリで自動生成されたものをコミットするとき

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

`git config --global`コマンドでGitのグローバル設定で、コミット時に使用されるテンプレートファイルのパスを指定する。

```bash
git config --global commit.template ~/.git_message_template/.gitmessage
```

commit.template を設定すると、git commit コマンドを実行したときにテンプレートが自動的に読み込まれ、編集可能なコミットメッセージの初期テキストとして表示されるようになる。<br />
vscodeの場合は変更をステージ後コミットするとCOMMIT_EDITMSG上にデフォルトで表示されるようになる。

なお、commit.template は --template オプションと同様に、git commit コマンド実行時に -t オプションで別のテンプレートファイルを指定すると、commit.template の設定は上書きされる。

```bash
$ git commit -t $HOME/.git_message_template/.docs_gt
Aborting commit; you did not edit the message. # 上書き保存しない場合

$ git commit -t $HOME/.git_message_template/.docs_gt
[main e4db099] docs(README): Update README.md with new information
1 file changed, 106 insertions(+), 1 deletion(-)
```

#### 【GitHub】 git commit / push後の GitHubの表示について

##### git commit時ににフォーク元のissue番号(# 付き)を書くと、自動で「アカウント名# issue番号」のタイトルでURLに変換される

[参考](https://github.com/7rikazhexde/twitter-video-dl-for-sc/commit/08c13970a84804e48c80d589002189e452cb8183)

## git commit後のコミットを取消する(git reset / git revert)

`git commit`後のコミットを取消する場合、一般的には `git reset`コマンドを使用します。ただし、注意が必要であり、コミットを取り消すことは他の開発者やリモートリポジトリとの連携に影響を与える可能性があります。以下に、コミットの取消方法を説明します。

### 直前のコミットを取消し、変更をステージングエリアに戻す

```bash
git reset --soft HEAD^
```

このコマンドは直前のコミットを取り消し、コミットメッセージを保持したまま変更をステージングエリアに戻します。この後、変更を修正して再コミットすることができます。

### 直前のコミットと変更を完全に取り消す

```bash
git reset --hard HEAD^
```

このコマンドは直前のコミットとその変更を完全に取り消し、ワーキングツリーも変更前の状態に戻します。注意が必要で、取り消したコミットと変更は復元できません。

### 特定のコミットを取り消す

```bash
git revert <commit-hash>
```

`git revert` コマンドは、指定したコミットの変更を取り消す新しいコミットを作成します。これにより、変更を取り消すだけでなく、履歴にも記録されます。他の開発者との連携を維持しつつ、変更を取り消す方法です。

## 【GitHub】プロジェクトのフォークについて

GitHubでのプロジェクトのフォークは、オリジナルのリポジトリをコピーして自分のGitHubアカウントに持ってくることができる。<br />
以下は、フォークする際の作法、注意点、やり方。

### 作法

- 原則として、フォークするプロジェクトのライセンスを確認し、適切にクレジットを表示することが望ましい。
- フォークしたプロジェクトに対してコントリビュートする際は、オリジナルのプロジェクトと同じように、適切な開発プロセスを行うようにする。

### 注意点

- フォーク元のプロジェクトを含め、ライセンスについてしっかりと理解し、遵守するようこと。
- フォーク元のプロジェクトがアップデートされた場合、定期的に同期をとることで、最新のコードを利用することができる。

### やり方

1. GitHubにログインし、フォークしたいプロジェクトのリポジトリにアクセスする。
1. 右上にある「Fork」ボタンをクリックする。
1. 自分のGitHubアカウントで、フォークしたリポジトリのコピーが作成される。
1. コピーしたリポジトリに対して、必要な修正を行い、コミットする。

## フォーク元の変更を取り込む方法

### フォーク元のリポジトリをリモートに追加する

```bash
git remote add upstream <フォーク元のリポジトリのURL>
```

### ローカルのフォークしたリポジトリを更新する

```bash
git fetch upstream
```

### フォーク元の変更をマージする

```bash
git merge upstream/<変更を取り込むブランチ名>
```

#### リベースする場合は以下のコマンドを実行する。

```bash
git rebase upstream/<変更を取り込むブランチ名>
```

### コンフリクトの解決

変更をマージまたはリベースする際にコンフリクトが発生した場合は、手動で解決する必要があります。コンフリクトの解決方法は、変更の内容に応じて異なります。

### 変更をプッシュする

変更をマージまたはリベースした後は、フォークしたリポジトリに変更をプッシュする。

```bash
git push origin <リモート先のブランチ名>
```

これらの手順に従うことで、フォーク元の変更を自分のフォークしたリポジトリに取り込むことができる。
