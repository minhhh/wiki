# SQLITE

## <a id="toc">TOC
* [Basics](#user-content-basics)
* [Import/Export](#import-export)
* [References](#user-content-references)

### <a id="basics"></a>Basics

#### Show help
```
    .help
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


### <a id="import-export"></a>Import/Export
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

