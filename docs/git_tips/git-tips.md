# git-tips

git関連のtipsをまとめてます。

[Topに戻る](../index.md)

## git commitコマンド

### 基本形

git commit コマンドは、ローカルリポジトリに変更をコミットするために使用されます。<br />
以下は、基本的な git commit コマンドの例。

```bash
git commit -m "Add new feature"
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

```
# ==== Prefix ====
# fix		バグ修正、クリティカルなバグ修正なら hotfix
# feat		feat は feature の略
# docs		ドキュメントのみ修正
# style		空白、セミコロン、行、コーディングフォーマットなどの修正
# refactor	整理 （リファクタリング等）
# test		テスト追加や間違っていたテストの修正
# chore		ビルドツールやライブラリで自動生成されたものをコミットするとき

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

git config --globalコマンドでGitのグローバル設定で、コミット時に使用されるテンプレートファイルのパスを指定する。

```
git config --global commit.template ~/.git_message_template/.gitmessage
```

commit.template を設定すると、git commit コマンドを実行したときにテンプレートが自動的に読み込まれ、編集可能なコミットメッセージの初期テキストとして表示されるようになる。<br />
vscodeの場合は変更をステージ後コミットするとCOMMIT_EDITMSG上にデフォルトで表示されるようになる。

なお、commit.template は --template オプションと同様に、git commit コマンド実行時に -t オプションで別のテンプレートファイルを指定すると、commit.template の設定は上書きされる。

```
$ git commit -t $HOME/.git_message_template/.docs_gt
Aborting commit; you did not edit the message. # 上書き保存しない場合

$ git commit -t $HOME/.git_message_template/.docs_gt
[main e4db099] docs(README): Update README.md with new information
 1 file changed, 106 insertions(+), 1 deletion(-)
```

#### 【GitHub】 git commit / push後の GitHubの表示について

##### git commit時ににフォーク元のissue番号(# 付き)を書くと、自動で「アカウント名# issue番号」のタイトルでURLに変換される

[参考](https://github.com/7rikazhexde/twitter-video-dl-for-sc/commit/08c13970a84804e48c80d589002189e452cb8183)

## git addコマンド

### ステージング

git addは、Gitで変更したファイルをステージングエリア（インデックス）に追加するコマンドです。ステージングエリアにファイルを追加することで、Gitはその変更を次のコミットの対象として扱う。

git addコマンドは、次のように使用する。
ステージングエリアに追加するファイルのパスを指定します。例えば、以下のようにしてindex.htmlファイルをステージングエリアに追加することができる。

```
git add index.html
```

複数のファイルをステージングエリアに追加する場合は、git addコマンドに複数のファイルを指定することができる。

```
git add index.html style.css script.js
```

また、ディレクトリを指定することで、そのディレクトリ内のすべての変更を一度にステージングエリアに追加することもできる。

```
git add images/
```

ステージングエリアに追加されたファイルは、git commitコマンドを実行することで、ローカルリポジトリにコミットすることができる。

### ステージングの取り消し

ステージングエリア（インデックス）に追加したファイルを取り消す方法は、git resetコマンドを使用することができる。
まず、git statusコマンドで、ステージングエリアに追加されたファイルを確認します。

```
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   index.html
        modified:   style.css
```

git resetコマンドを使用して、ステージングエリアに追加したファイルを取り消す

```
git reset HEAD index.html style.css
```

HEADは、最新のコミットを指す。git resetコマンドにHEADを指定することで、ステージングエリアに追加された変更を取り消すことができる。

ファイル指定しない場合はステージングエリアからすべてのファイルを取り消すことができる。

```
git reset HEAD
```

git statusコマンドで、変更がステージングエリアから取り消されたことを確認する。

```
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   index.html
        modified:   style.css
```

このように、git resetコマンドを使用することで、ステージングエリアに追加したファイルの変更を取り消すことができる。ただし、取り消した変更は作業ディレクトリに残ります。必要に応じて、git restoreコマンドを使用して作業ディレクトリの変更を取り消すこともできる。

なお、git resetコマンドにHEADを指定しない場合、コミットの履歴は変更されませんが、ステージングエリアからファイルの変更を取り消すことができる。具体的には、ステージングエリアから取り消されたファイルの変更は、作業ディレクトリに戻される。**ただし、コミットの履歴は変更されないため、注意が必要。**

## git restoreコマンド

git restoreコマンドは、ワーキングツリーからステージングエリアに変更を戻したり、ステージングエリアからコミットに変更を戻すために使用される。具体的には、次のような使い方ができる。

### ワーキングツリーからステージングエリアに変更を戻す

git addコマンドでファイルをステージングエリアに追加したが、戻したい場合は、git restore --stagedを使用します。

例えば、index.htmlファイルをステージングエリアに追加し、変更を戻したい場合は、次のようにする。

```
$ git add index.html     # ステージングエリアに変更を追加
$ git restore --staged index.html   # ステージングエリアから変更を戻す
```

### ステージングエリアからコミットに変更を戻す

git commitコマンドでコミットした変更を戻したい場合は、git restoreコマンドを使用する。

例えば、最新のコミットからindex.htmlファイルの変更を取り消したい場合は、次のようにする。

```
$ git restore index.html   # 最新のコミットから変更を戻す
```

> **Note**
> **git restoreコマンドでコミットを戻した場合、変更が含まれていた最新のコミットは削除されません。そのため、コミットログには変更が含まれていたことが残ります。**

例えば、次のようにindex.htmlファイルを変更し、コミットしたとする。

```bash
git add index.html
git commit -m "update index.html"
```

その後、index.htmlファイルの変更を取り消すために、git restoreコマンドで戻した場合、以下のようにコミットログには変更が含まれていたことが残る。

```bash
git restore index.html
git commit -m "revert index.html changes"
```

上記のように、新しいコミットメッセージを指定して、変更を戻したことを記録する必要があります。また、変更を含む最新のコミットを完全に削除するには、git resetコマンドを使用する必要がある。

### ワーキングツリーから変更を戻す

ワーキングツリーで行った変更を戻したい場合は、git restoreコマンドを使用する。

例えば、index.htmlファイルの変更を取り消したい場合は、次のようにする。

```bash
git restore index.html   # ワーキングツリーから変更を戻す
```

git restoreコマンドは、変更を取り消す方法が複数ある場合にも利用できる便利なコマンドですが、操作が完了する前に必ずgit statusコマンドで状態を確認することが必要。

## 【GitHub】プロジェクトのフォークについて

GitHubでのプロジェクトのフォークは、オリジナルのリポジトリをコピーして自分のGitHubアカウントに持ってくることができる。<br />
以下は、フォークする際の作法、注意点、やり方。

【作法】

- 原則として、フォークするプロジェクトのライセンスを確認し、適切にクレジットを表示することが望ましい。
- フォークしたプロジェクトに対してコントリビュートする際は、オリジナルのプロジェクトと同じように、適切な開発プロセスを行うようにする。

【注意点】

- フォーク元のプロジェクトを含め、ライセンスについてしっかりと理解し、遵守するようこと。
- フォーク元のプロジェクトがアップデートされた場合、定期的に同期をとることで、最新のコードを利用することができる。

【やり方】

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
git push origin <自分のブランチ名>
```

これらの手順に従うことで、フォーク元の変更を自分のフォークしたリポジトリに取り込むことができる。
