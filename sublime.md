#  PLUGINS
* Alignment
* Markdown Preview
* MarkdownEditing
* TrailingSpaces

# Essential moving around

```
    Option Left/Right - Move one word forward/backward
    C Left/Right      - Move to the beginning/end of line
    C Up/Down         - Go to the beginning/end of file
```
<br/>

I like moving up and down a number of lines (5 lines) at a time. This is
possible through Sublime Plugin.

* Create a folder for your plugin in ''~/Library/Application Support/Sublime Text 2/Packages/''
* Follow this guide to create functions for moving a number of lines:
[http://www.sublimetext.com/forum/viewtopic.php?f=5&t=5513](http://www.sublimetext.com/forum/viewtopic.php?f=5&t=5513)

Better way is to move to blank line

```
    # add this to KeyBinding > User
    { "keys": ["alt+up"], "command": "move", "args": {"by": "stops", "empty_line":
    true, "forward": false}  },
    { "keys": ["alt down"], "command": "move", "args": {"by": "stops", "empty_line": true, "forward": true}  }
```
<br/>


# Essential open file

```
    C P - Open anything
    C R - Open function
```
<br/>

# Essential line manipulation

```
    Ctrl Shift K   - Delete line
    C K            - Delete to end of line
    C Shift Enter  - Insert line before
    C J            - Join line
    C Shift D      - Duplicate line
    C K U          - To Upper Case
    C K L          - To Lower Case
    C /            - Toggle comment
    C Ctrl up/down - Move code up down
    Alt drag       - Select multiple column
```
<br/>

# Block manipulation use TralingSpaces plugin

```
    # add this to KeyBinding > User
    { "keys": ["ctrl shift t"], "command": "delete_trailing_spaces"  },
```
<br/>

# Use alignment plugin

```
    # add this to KeyBinding > User
    { "keys": ["ctrl shift l"], "command": "alignment"  },
```
<br/>

# Use reindent command

```
    # add this to KeyBinding > User
    { "keys": ["ctrl shift f"], "command": "reindent" } ,
```
<br/>

# Searching and Replacing

```
    C F       - Search
    Alt C G   - Find all under cursor
    Ctrl C G  - Find all under cursor and put multiple cursors
    C D       - Add next match to selection
    C Alt F   - Replace in file
    C Shift F - Replace in multiple files
    C E       - Use word undercursor for search
```
<br/>

# Windows

```
    C `    - Switch windows
    Ctrl ` - Toggle Console
    C K B  - Toggle sidebar
```
<br/>

# Syntax check
* [http://mondaybynoon.com/20110421/jslint-in-sublime-text-2-on-os-x/](http://mondaybynoon.com/20110421/jslint-in-sublime-text-2-on-os-x/)

# Vintage mode

```
    c-i ' - Change inside single quote
    c-a ' - Change around single quote
    v-i ' - select inside single quote
    v-a ' - select around single quote
    d-i ' - Delete inside single quote
    d-a ' - Delete around single quote
```
<br/>
