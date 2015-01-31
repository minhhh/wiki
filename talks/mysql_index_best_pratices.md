# SUMMARY

    Title: MySQL Indexing: Best Practices
    Date: 2013-11-20
    Speaker: Peter Zaitsev
    Conference: Percona webinar
    Tags: mysql

Url: https://www.youtube.com/watch?v=qd0RcBXpDI8

Mysql index best pratices by percona

# MYSQL INDEX BEST PRACTICES
## types of indices
* btree: mysql
* rtree: myisam only
* hash: memory, ndb
* bitmap: not supported by mysql
* fulltext: myisam, innodb 5.6

## Index in myisam vs innodb
* In myisam data pointers point to physical offset in data file
    * All indices are the same
* index in innodb
    * primary key: data stored in leaf nodes
    * other indexes: pointer to primary key

## What operations can btree index do
* key=5
* key>5
* 10 > key > 5
* not find all rows with last digit of key is zero

##  String index
* strings also have sort order
* prefix is a special type of range. like 'abc%' means 'abc[lowest]' < key < 'abc[highest]'
* like '%abc' cannot be optimized

## Multicolumn index
* sort order is defined, comparing leading column, then second, and so on
* still one btree

## Overhead of indexing
* Better to extend than to create new
    * write: updating index is often major cost of database write
    * read: waste space and memory

## Cost of indexing
* long primary key (innodb) make secondary indexes slower
* random primary key (innodb) cause page split
* low selectivity indexes are cheap
* correlated indices are less expensive

## Indexing innodb
    * data is clustered by primary key
    * primary key implicitly appended to all indices

## How mysql uses indexes
* data lookup
* sorting
* avoid reading data
* special optimization

## Use index for data lookup
* select * from employees where last_name="smith"
    * will use index(last_name)

## Index usage on multiple columns
* index(a, b, c)
* will use index on
    * a>5
    * a=5 and b>6
    * a=5 and b in (2,3) and c>5
* will NOT use index on
    * b>5
    * b=6 and b=7
* will use part of the index
    * a>5 and b=2 - range on first column
    * a=5 and b>5 and c=2 - range on first column
* mysql will stop using key parts if it meets real range (<, >, BETWEEN)

## Index for sorting
* select * from players order by score desc limit 10
    * use index on score
    * without index mysql will use `filesort`
* often combined with using index for lookup
    * select * from players where country='us' order by score desc limit 10
    * best served with index on (country, score)

## Multicolumn index for efficient sorting
* key(a,b) will use index for sorting
    * order by a
    * a = 5 order by b
    * order by a desc, b desc - sorting 2 columns in the same order
    * a > 5 order by a
* will not use index for sorting
    * order by b
    * a > 5 order by b
    * a in (1,2) order by b
    * order by a asc, b desc

## Avoid reading data
* covering index
    * applies to index use for specific query, not type of index
* select status from orders where customer_id=123
    * key(customer_id, status)

## Special optimization
    * min/max optimization
    * select max(salary) from employee group by dept_id
        * will use index(dept_id, salary)

## Index and joins
* join is performed as nested loop
    * select * from posts, comments where author="peter" and comments.post_id=posts.id
* very important to have all join indexed
* index is only needed on table which is being looked up. the index on posts.id is not needed
* redesign join query which can't be indexed

## Using multiple indexes for table
* select * from tbl where a = 5 and b=6
    * can use index on a and b separately
    * index on (a,b) is much better
* select * from tbl where a=5 or b=6
    * 2 separate index is much better
    * index(a,b) can't be used

## Prefix index
* you can build index on the left most prefix of the column
    * alter table title add key(title(20))
    * needed to index blob/text columns
    * can be significantly smaller
    * can't be used as covering index
    * choosing prefix length is the question
* choosing index length
    * prefix should be selective enough
    * check the number of distinct value vs distinct index
* check for outliers
    * ensure that there are not too many rows sharing the same prefix

## How mysql choose index
* perform dynamic picking for every query execution
* estimate the number of rows it needs to access
* use "cardinality" statistics if possible
* explain is a great tool to see how mysql plans to execute the query
    * real execution might be different
    * `type` sorted from good to bad
    * `rows` - higher number mean slow query
    * `key_len` shows how many parts of the keys are really used
    * `extra`
        * using index - good
        * using filesort, temporary - bad

## Indexing strategy
* Build indexes for set of performance critical queries
    * Look at them together not just one by one
* Best if all where and join clauses use index for lookup
* General extend index if you can, not create new

## Indexing strategy example
* Build index order which benefits more queries
    * select from tbl where a=5 and b=6
    * select from tbl where a>5 and b=6
    * key(b,a) is better
* do not add index for non performance critical queries

## Trick 1: Enumerating ranges
* key(a,b)
* select * from tbl where a between 2 and 4 and b=5
    * will only use the first key part
* select * from tbl where a in (2,3,4) and b=5
    * will use both key parts

## Trick 2: Add fake filter
* key(gender, city)
* select * from people where city="newyork"
    * will not be able to use index
* select * from people where gender in ("m", "f") and city="newyork"
    * will be able to use the index
* the trick works best with low selectivity columns
    * gender, status, boolean type

## Trick 3: unionizing filesort
* key(a,b)
* select * from tbl where a in (1,2) order by b limit 5
    * will not be able to use index for sorting
* (select * from tbl where a =1 order by b limit 5) union all (select * from tbl where a=2 order by b limit 5) order by b limit 5
    * will use index for sorting. "filesort" will be needed only to sort over 10 rows

