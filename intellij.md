INTELLIJ GUIDE
==============

Guide to using IntelliJ for everyday work.

## Settings
* Vim emulation plugin: `IdeaVim`
* Change max heap http://stackoverflow.com/questions/20545435/why-is-the-new-version-of-intellij-idea-so-slow
    * Find `/Applications/IntelliJ IDEA.app/Contents/bin/idea.vmoptions`
    * Set the max heap to 8 GB (was 512 MB) and the Max PermGen to at least 1GB (was 300MB).
* Preferences > Editor > General > Appearance
* Preferences > Editor > General > Auto Import
* Editor > Appearance : Show right margin

* Change Shortcut for Next and Previous Editor Tabs:
    * Preferences > Keymap > Main Menu > Window > Editor Tabs > Select Next Tab


## Openning Windows

```
    Esc - Go back to Editor Window
    C S F12 - Maximize Editor window. Hide all Tool windows
    C S A - Find action by name
    C 1 - Toggle project window
    C 3 - Toggle Find window
    C 7 - Toggle structure window
```


## Moving Around

```
    C O - Go to class
    C Shift O - Go to file
    Ctrl M - Go to matching brace
    C B - Go to declaration or Usage
    C Option B - Go to implementation
    Option F7 - Search all occurences
    Ctrl Tab - Previous Editor Tab
    C Shift Left - Previous Editor Tab
    C Shift Right - Next Editor Tab
    C \ - Switch to REPL (Cursive)
```

## Editing
```
    C - - Collapse all nodes in a tree view.
    C + - Expand all nodes in a tree view.
    C F12 - Open current file structure
    C / - Line Comment
    C Option L - Format code
    C Shift L - Load file in REPL (Cursive)
```

## Search and replace

```
    C O - Find classname
    Double S - Search everywhere
    C F - Search in file
    C R - Search and replace in file
    C Shift F - Search in project
    C Shift R - Replace in project
    Option F7 - Search all occurences
    C Option F7 - Search all occurences
```

## Compile and Run
```
    C F9 - Make project
    Ctrl Alt R - Run
    Ctrl Alt D - Debug
```

### Windows

```
    Esc - Go back to Editor Window
    C Shift F12 - Maximize Editor window. Hide all Tool windows
    C O - Find class
    C Shift O - Find files
    C Option O - Find symbol
    C Shift A - Find action by name
    C 1 - Toggle project window
    C 3 - Toggle Find window
    C 7 - Toggle structure window
```



References
----------
* http://gaerfield.github.io/ide-shortcuts/
* https://www.jetbrains.com/idea/help/keyboard-shortcuts-you-cannot-miss.html
