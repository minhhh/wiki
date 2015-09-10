# MEMCACHE CHEATSHEET
Memcached is simple yet powerful. Its simple design promotes quick deployment, ease of development, and solves many problems facing large data caches. Its API is available for most popular languages.

## Viewing memcache stats
```
    echo "stats" | nc localhost 11211
```

## Viewing memcache server stats
```
    memcached -vv
```

## Viewing slab stats
```
    echo "stats slabs" | nc localhost 11211
```

## Viewing item stats
```
    echo "stats items" | nc localhost 11211
```

## Viewing stats sizes
```
    echo "stats sizes" | nc localhost 11211
```

## Flush all cache
```
    echo "flush_all" | nc localhost 11211
```

## Print all items of a slab
```
    echo "stats cachedump 1 0" | nc localhost 11211
```

## Get multiple items
```
    echo "get key1 key2" | nc localhost 11211
```



# REFERENCES
* [Memcache Wiki][memcache_wiki]
* [Memcache Cheatsheet][memcache_cheatsheet]

[memcache_wiki]: https://code.google.com/p/memcached/wiki/NewStart
[memcache_cheatsheet]: http://lzone.de/cheat-sheet/memcached
