---
title: MongoDB Install
tags:
  - MongoDB
  - NoSQL
description:
---

## For Mac

公式ドキュメント参考:  
[Install MongoDB Community Edition on macOS — MongoDB Manual](https://www.mongodb.com/docs/v6.0/tutorial/install-mongodb-on-os-x/)

`brew tap mongodb/brew`コマンドを実行すると、MongoDBのHomebrewリポジトリが追加され、その後`brew install mongodb-community`コマンドを実行することで、MongoDB Community Editionがインストールされます。このインストールには、以下のバイナリが含まれます。

- `mongod`サーバー
- `mongos`シャーディングクラスタクエリルータ
- MongoDB Shell（`mongosh`）

??? info "brew tap mongodb/brew"

    ```bash
    brew tap mongodb/brew
    ```

    ```bash
    ==> Tapping mongodb/brew
    Cloning into '/usr/local/Homebrew/Library/Taps/mongodb/homebrew-brew'...
    remote: Enumerating objects: 1256, done.
    remote: Counting objects: 100% (541/541), done.
    remote: Compressing objects: 100% (175/175), done.
    remote: Total 1256 (delta 412), reused 449 (delta 365), pack-reused 715
    Receiving objects: 100% (1256/1256), 274.40 KiB | 7.62 MiB/s, done.
    Resolving deltas: 100% (707/707), done.
    Tapped 17 formulae (36 files, 360.0KB).
    ```

??? info "brew install mongodb-community"

    ```bash
    brew install mongodb-community
    ```

    ```bash
    ==> Fetching dependencies for mongodb/brew/mongodb-community: mongodb/brew/mongodb-database-tools, node and mongosh
    ==> Fetching mongodb/brew/mongodb-database-tools
    ==> Downloading https://fastdl.mongodb.org/tools/db/mongodb-database-tools-macos-x86_64-100.8.0.zip
    ################################################################################################################################################################################################### 100.0%
    ==> Fetching node
    ==> Downloading https://ghcr.io/v2/homebrew/core/node/manifests/20.7.0
    ################################################################################################################################################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/node/blobs/sha256:4ca2870c75178c5caaed1f04014b3daea02a3883e9d146c1eb42274e1185b9fa
    ################################################################################################################################################################################################### 100.0%
    ==> Fetching mongosh
    ==> Downloading https://ghcr.io/v2/homebrew/core/mongosh/manifests/2.0.1-1
    ################################################################################################################################################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/mongosh/blobs/sha256:8d83db48a99274d8b11516bef376110a59cf7c27346d08cc5cda0bd4e3a76e3e
    ################################################################################################################################################################################################### 100.0%
    ==> Fetching mongodb/brew/mongodb-community
    ==> Downloading https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-7.0.0.tgz
    ################################################################################################################################################################################################### 100.0%
    ==> Installing mongodb-community from mongodb/brew
    ==> Installing dependencies for mongodb/brew/mongodb-community: mongodb/brew/mongodb-database-tools, node and mongosh
    ==> Installing mongodb/brew/mongodb-community dependency: mongodb/brew/mongodb-database-tools
    🍺  /usr/local/Cellar/mongodb-database-tools/100.8.0: 13 files, 119.0MB, built in 9 seconds
    ==> Installing mongodb/brew/mongodb-community dependency: node
    ==> Downloading https://ghcr.io/v2/homebrew/core/node/manifests/20.7.0
    Already downloaded: $HOME/Library/Caches/Homebrew/downloads/845229805459d6627ee2224ad2abe6b713799aef8cd074907d76e9ece563ec41--node-20.7.0.bottle_manifest.json
    ==> Pouring node--20.7.0.ventura.bottle.tar.gz
    Error: The `brew link` step did not complete successfully
    The formula built, but is not symlinked into /usr/local
    Could not symlink share/doc/node/gdbinit
    Target /usr/local/share/doc/node/gdbinit
    already exists. You may want to remove it:
      rm '/usr/local/share/doc/node/gdbinit'

    To force the link and overwrite all conflicting files:
      brew link --overwrite node

    To list all files that would be deleted:
      brew link --overwrite --dry-run node

    Possible conflicting files are:
    /usr/local/share/doc/node/gdbinit
    /usr/local/share/doc/node/lldb_commands.py
    /usr/local/share/man/man1/node.1
    ==> Summary
    🍺  /usr/local/Cellar/node/20.7.0: 2,517 files, 59.3MB
    ==> Installing mongodb/brew/mongodb-community dependency: mongosh
    ==> Downloading https://ghcr.io/v2/homebrew/core/mongosh/manifests/2.0.1-1
    Already downloaded: $HOME/Library/Caches/Homebrew/downloads/7293ba9929bc4138046847c24722858b4cc4bfca72156b4bb1fd71d8b79a61cc--mongosh-2.0.1-1.bottle_manifest.json
    ==> Pouring mongosh--2.0.1.ventura.bottle.1.tar.gz
    🍺  /usr/local/Cellar/mongosh/2.0.1: 9,875 files, 47.7MB
    ==> Installing mongodb/brew/mongodb-community
    ==> Caveats
    To start mongodb/brew/mongodb-community now and restart at login:
      brew services start mongodb/brew/mongodb-community
    ==> Summary
    🍺  /usr/local/Cellar/mongodb-community/7.0.0: 11 files, 278.5MB, built in 7 seconds
    ==> Running `brew cleanup mongodb-community`...
    Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
    Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
    ==> Caveats
    ==> mongodb-community
    To start mongodb/brew/mongodb-community now and restart at login:
      brew services start mongodb/brew/mongodb-community
    ```
