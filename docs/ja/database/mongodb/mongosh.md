# mongoshによる使い方

!!! info

    MongoDBではmongoコマンドにより操作できますが、  
    "mongo"コマンドを使用すると"mongo"コマンドは非推奨となり、今後のリリースで削除される予定と警告が表示されます。  
    これは"mongo"コマンドが、より使いやすく互換性のある"mongosh"コマンドに取って代わられるためです。  
    そのため、以下ではmongoshを使用した方法を記載します。

## mongoshの起動

!!! info "mogosh"

    ```bash
    mongosh
    ```

    ```bash
    Current Mongosh Log ID: [id情報]
    Connecting to:  mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.1
    Using MongoDB:  7.0.2
    Using Mongosh:  2.0.1

    For mongosh info see: https://docs.mongodb.com/mongodb-shell/

    test>
    ```

!!! warning

    セキュリティ上の理由から、パスワードを含むコマンドラインは避けることをお勧めします。代わりに、MongoDBシェルで接続後に認証を実行することができます。

    ```bash
    mongosh
    > use admin
    switched to db admin
    > db.auth("admin","[password]")
    ```

!!! info

    mongoshでは以下の警告が表示されることがあります。

    ```bash
    Warning: Found ~/.mongorc.js, but not ~/.mongoshrc.js. ~/.mongorc.js will not be loaded.
    You may want to copy or rename ~/.mongorc.js to ~/.mongoshrc.js.
    ```

    その際は記載の通りリネームすれば問題ありません。

    ```bash
    cp ~/.mongorc.js ~/.mongorc_old.js
    mv ~/.mongorc.js ~/.mongoshrc.js
    ```

!!! info

    admin指定の場合

    ```bash
    mongosh -u admin -p --authenticationDatabase admin

    Enter password: **********
    Current Mongosh Log ID: 652a46b96004ccbf87fa73d4
    Connecting to:  mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=admin&appName=mongosh+2.0.1
    Using MongoDB:  7.0.2
    Using Mongosh:  2.0.1
    ```

    登録ユーザー指定の場合

    ```bash
    mongosh -u [登録ユーザ名] -p --authenticationDatabase [db名]

    Enter password: ******
    Current Mongosh Log ID: [id]
    Connecting to:  mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=[db名]&appName=mongosh+2.0.1
    Using MongoDB:  7.0.2
    Using Mongosh:  2.0.1

    For mongosh info see: https://docs.mongodb.com/mongodb-shell/
    ```

## Mongoshのバージョン確認

!!! info "db.version()"

    ```
    test> db.version()
    6.0.4
    ```

## データベース表示

!!! info "show dbs"

    ```bash
    test> show dbs
    admin       180.00 KiB
    config      108.00 KiB
    ec_sol_db1   92.00 KiB
    local        76.00 KiB
    ```

!!! info

    最初ログインした時は以下のエラーが表示されることがあります。

    ```
    test> show dbs
    MongoServerError: Command listDatabases requires authentication
    ```

    エラーが表示される時は認証付きでログインし直す必要があります。

    ```bash
    mongosh -u admin -p --authenticationDatabase admin
    ```

## DB選択

!!! info "use [db名]"

    ```bash
    test> use ec_sol_db1
    switched to db ec_sol_db1
    ```

## コレクション確認

!!! info "show collections"

    ```bash
    ec_sol_db1> show collections
    ec_sol_pes_tbl
    ```

## ユーザー一覧でアクセス権限を確認する

!!! info "admin> db.system.users.find()"

    ユーザー一覧でアクセス権限を確認する場合はadmin指定でログインする必要があります。

    ```bash
    mongosh -u admin -p --authenticationDatabase
    ```

    ```bash
    test> use admin
    switched to db admin
    ```

    ```bash
    admin> db.system.users.find();
    [
      {
        _id: 'admin.admin',
        userId: new UUID("[UUID]"),
        user: 'admin',
        db: 'admin',
        credentials: {
          'SCRAM-SHA-1': {
            iterationCount: 10000,
            salt: '[salt]',
            storedKey: '[storedKey]',
            serverKey: '[serverKey]'
          },
          'SCRAM-SHA-256': {
            iterationCount: 15000,
            salt: '[salt]',
            storedKey: '[storedKey]',
            serverKey: '[serverKey]'
          }
        },
        roles: [
          { role: 'userAdminAnyDatabase', db: 'admin' },
          { role: 'readWrite', db: '[db名]' }
        ]
      },
      {
        _id: '[db名].[user名]',
        userId: new UUID("[UUID]"),
        user: '[user名]',
        db: '[db名]',
        credentials: {
          'SCRAM-SHA-1': {
            iterationCount: 10000,
            salt: '[salt]',
            storedKey: '[storedKey]',
            serverKey: '[serverKey]'
          },
          'SCRAM-SHA-256': {
            iterationCount: 15000,
            salt: '[salt]',
            storedKey: '[storedKey]',
            serverKey: '[serverKey]'
          }
        },
        roles: [ { role: 'readWrite', db: '[db名]' } ]
      }
    ]
    ```

## admin登録

最初にDBを使用する場合はユーザ管理者(admin)を登録する必要があります。

!!! info "db.createUser()"

    ```bash
    mongosh
    use admin
    db.createUser({user: "admin", pwd: "[password]", roles: ["userAdminAnyDatabase"]})
    ```

## データベースの作成

!!! info "use [db名]"

    データベースを作成する（データベース名は"myDatabase"とします）

    ```bash
    use myDatabase
    ```

## コレクションの作成

!!! info "db.createCollection('コレクション名')"

    コレクションを作成する（コレクション名は"myCollection"とします）

    ```bash
    db.createCollection('myCollection')
    ```

## 特定ユーザーの登録

!!! info "db.createUser()"

    特定のデータベースに接続する（データベース名は"myDatabase"とします）

    ```bash
    use myDatabase
    db.createUser({user: "user", pwd: "[password]", roles: ["readWrite"]})
    ```

!!! info "db.grantRolesToUser()"

    もし他のデータベースに対しても同様の権限を付与したい場合は、以下のように行います。  
    特定のデータベースに接続する（データベース名は"anotherDatabase"とします）

    ```bash
    use anotherDatabase
    db.grantRolesToUser("user", [{role: "readWrite", db: "anotherDatabase"}])
    ```

    admin権限にはroot権限をつけると良いと思います。  
    ※全てのdb,コレクションにアクセスできるためパスワード管理および権限設定には注意してください。

    ```bash
    db.grantRolesToUser("admin", ["root"])
    ```

## コレクションの中身の確認

!!! info "db.ec_sol_pes_tbl.find()"

    ```bash
    [test> use ec_sol_db1
    switched to db ec_sol_db1
    ec_sol_db1> db.ec_sol_pes_tbl.find()
    [
      {
        _id: ObjectId("65294a82e062ec915f2c95be"),
        col1: ISODate("2023-03-03T00:05:14.071Z"),
        col2: 'ALONE',
        col3: 414,
        col4: 1,
        col5: 87.99,
    # 省略
    ```
