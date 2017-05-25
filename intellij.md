# INTELLIJ GUIDE

Guide to using IntelliJ for everyday work.

## Install
* IdeaVim
* Change max heap http://stackoverflow.com/questions/20545435/why-is-the-new-version-of-intellij-idea-so-slow
    * Find `/Applications/IntelliJ IDEA.app/Contents/bin/idea.vmoptions`
    * Set the max heap to 8 GB (was 512 MB) and the Max PermGen to at least 1GB (was 300MB).
* Preferences > Editor > General > Appearance



## Shortcuts
### Editing
```
    C - - Collapse all nodes in a tree view.
    C + - Expand all nodes in a tree view.
    C B - Go to declaration
    C F12 - Open current file structure
    C / - Line Comment
    C S / - Line Comment
```

### Search and replace

```
    C O - Find classname
    Double S - Search everywhere
    C S F - Search in project
    C S R - Replace in project
    Option F7 - Search all occurences
```

### Compile and Run
```
    C F9 - Make project
    C Alt R - Run
    C Alt D - Debug
```

### Windows

```
    C S A - Find action by name
    C 1 - Toggle project window
    C 3 - Toggle Find window
    C 7 - Toggle structure window
```



## References
* http://gaerfield.github.io/ide-shortcuts/
* https://www.jetbrains.com/idea/help/keyboard-shortcuts-you-cannot-miss.html
