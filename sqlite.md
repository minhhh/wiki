# SQLITE

## <a id="toc">TOC
* [Basics](#user-content-basics)
* [View Data](#user-content-view-data)
* [Modify Data](#user-content-modify-data)
* [Import/Export](#import-export)
* [References](#user-content-references)

### <a id="basics"></a>Basics

#### Show help
```
    .help
```

#### List databases

```
    .database
```

#### List schema and tables

```
    .tables
    .schema
```

#### Quit
```
    .quit
```

### <a id="view-data"></a>View Data

#### View table
```
    select * from <table name>;
```

#### Turn on/off column names on query results

```
    .explain on
    .explain off

    # See the current explain status
    .show
```

### <a id="modify-data"></a>Modify Data
#### Modify data
```
    update employee set deptid=3 where empid=101;
```

#### Add column
```
    alter table employee add column deptid integer;
```

#### Create an Index
```
    create unique index empidx on employee(empid);
```

### <a id="import-export"></a>Import/Export
#### Import
```
    sqlite3 <database file> < insert-data.sql
```

#### Dump database as SQL
```
    sqlite3 <database file> .dump > output.sql
```

#### Dump table as SQL
```
    sqlite3 <database file> ".dump <table name>" > output.sql
```

### GUITool
* [sqlitebrowser](http://sqlitebrowser.org/)

### <a id="references"></a>References
* https://gist.github.com/vincent178/10889334
* http://www.thegeekstuff.com/2012/09/sqlite-command-examples/
* http://lzone.de/cheat-sheet/sqlite

