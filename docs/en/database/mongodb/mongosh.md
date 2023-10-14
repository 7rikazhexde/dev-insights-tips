# mongosh

!!! info

    MongoDB can be manipulated with the mongo command,  
    However, if you use the "mongo" command, you will receive a warning that the "mongo" command is deprecated and will be removed in a future release.  
    This is because the "mongo" command will be replaced by the more user-friendly and compatible "mongosh" command.  
    For this reason, the following is a description of how to use mongosh.

## mongosStarting mongosh

!!! info "mogosh"

    ```bash
    mongosh
    ```

    ```bash
    Current Mongosh Log ID: [id]
    Connecting to:  mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.1
    Using MongoDB:  7.0.2
    Using Mongosh:  2.0.1

    For mongosh info see: https://docs.mongodb.com/mongodb-shell/

    test>
    ```

!!! warning

    For security reasons, we recommend avoiding command lines containing passwords. Instead, authentication can be performed after connecting in the MongoDB shell.

    ```bash
    mongosh
    > use admin
    switched to db admin
    > db.auth("admin","[password]")
    ```

!!! info

    The following warning may appear in mongosh.

    ```bash
    Warning: Found ~/.mongorc.js, but not ~/.mongoshrc.js. ~/.mongorc.js will not be loaded.
    You may want to copy or rename ~/.mongorc.js to ~/.mongoshrc.js.
    ```

    In that case, just rename it as described.

    ```bash
    cp ~/.mongorc.js ~/.mongorc_old.js
    mv ~/.mongorc.js ~/.mongoshrc.js
    ```

!!! info

    If admin is specified

    ```bash
    mongosh -u admin -p --authenticationDatabase admin

    Enter password: **********
    Current Mongosh Log ID: 652a46b96004ccbf87fa73d4
    Connecting to:  mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=admin&appName=mongosh+2.0.1
    Using MongoDB:  7.0.2
    Using Mongosh:  2.0.1
    ```

    For registered user designation

    ```bash
    mongosh -u [user] -p --authenticationDatabase [db]

    Enter password: ******
    Current Mongosh Log ID: [id]
    Connecting to:  mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=[db名]&appName=mongosh+2.0.1
    Using MongoDB:  7.0.2
    Using Mongosh:  2.0.1

    For mongosh info see: https://docs.mongodb.com/mongodb-shell/
    ```

## Check the version of Mongosh

!!! info "db.version()"

    ```
    test> db.version()
    6.0.4
    ```

## Listing of databases

!!! info "show dbs"

    ```bash
    test> show dbs
    admin       180.00 KiB
    config      108.00 KiB
    ec_sol_db1   92.00 KiB
    local        76.00 KiB
    ```

!!! info

    When you first log in, you may see the following error message

    ```
    test> show dbs
    MongoServerError: Command listDatabases requires authentication
    ```

    When an error is displayed, you must log in again with authentication.

    ```bash
    mongosh -u admin -p --authenticationDatabase admin
    ```

## Select the DB

!!! info "use [db]"

    ```bash
    test> use ec_sol_db1
    switched to db ec_sol_db1
    ```

## Check the collection

!!! info "show collections"

    ```bash
    ec_sol_db1> show collections
    ec_sol_pes_tbl
    ```

## Check access privileges in the user list

!!! info "admin> db.system.users.find()"

    If you want to check access privileges in the user list, you must log in with the admin designation.

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
          { role: 'readWrite', db: '[db]' }
        ]
      },
      {
        _id: '[db].[user]',
        userId: new UUID("[UUID]"),
        user: '[user]',
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
        roles: [ { role: 'readWrite', db: '[db]' } ]
      }
    ]
    ```

## admin registration

The user administrator (admin) must be registered to use the DB for the first time.

!!! info "db.createUser()"

    ```bash
    mongosh
    use admin
    db.createUser({user: "admin", pwd: "[password]", roles: ["userAdminAnyDatabase"]})
    ```

## Database Creation

!!! info "use [db]"

    Create a database (database name is "myDatabase")

    ```bash
    use myDatabase
    ```

## Collection Creation

!!! info "db.createCollection('コレクション名')"

    Create a collection (name the collection "myCollection")

    ```bash
    db.createCollection('myCollection')
    ```

## Registration of a specific user

!!! info "db.createUser()"

    Connect to a specific database (database name is "myDatabase")

    ```bash
    use myDatabase
    db.createUser({user: "user", pwd: "[password]", roles: ["readWrite"]})
    ```

!!! info "db.grantRolesToUser()"

    If you wish to grant the same privileges to other databases, do the following  
    Connect to a specific database (database name is "anotherDatabase")

    ```bash
    use anotherDatabase
    db.grantRolesToUser("user", [{role: "readWrite", db: "anotherDatabase"}])
    ```

    It is a good idea to add root privileges to admin privileges.  
    Please be careful with password management and permission settings as you have access to all db's and collections.

    ```bash
    db.grantRolesToUser("admin", ["root"])
    ```

## Check the contents of the collection

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
    # …
    ```
