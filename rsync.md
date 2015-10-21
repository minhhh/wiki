# RSYNC
## References
* [The Non-Beginner’s Guide to Syncing Data with Rsync][gtsd]

## Copy and delete old

```bash
    rsync -avl --delete --progress <source> <dest>  # Linux only
```

## rsync through ssh tunnel

```bash
    # tunner rsync through ssh port 12345
    rsync -avl --delete -e 'ssh -p 12345' <source> user@192.168.10.1:<dest>
```

## Copy with rsync and progress

```bash
    rsync -avl --info=progress2 source dest  # Linux only
    export SOURCE=<source> DEST=<dest> && export SC=$(find "$SOURCE" | wc -l) rsy&& rsync -vrltd  --stats --human-readable "$SOURCE" "$DEST" | pv -lep -s $SC > /dev/null
```


[gtsd]: http://www.howtogeek.com/175008/the-non-beginners-guide-to-syncing-data-with-rsync/
