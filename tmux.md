TMUX
====

`tmux` is a tool to maintain persistent working states on remote servers—allowing you to detach and re-attach at will. It's similar to `screen`, but it has a number of advantages:
* Screen is a largely dead project, and its code has significant issues
* Tmux is an active project with an active codebase
* Tmux is built to be truly client/server; screen emulates this behavior
* Tmux supports both emacs and vim shortcuts
* Tmux supports auto-renaming windows
* Tmux is highly scriptable
* Window splitting is more advanced in tmux


## Open new tmux session
```
    tmux # Open an anonymous session, with number 0,1,2,.. as name

    tmux new -s <session_name> # Open a new session with name <session_name>

    tmux ls # List all session
    <prefix> s # List all session

    <prefix> $ # Rename current session
```

## Attach to a session

```
    tmux a # Attach to first available session

    tmux a -t <session_name> # Attach to session by session name
```

## Detach from a session

```
    tmux detach

    <prefix> d

    tmux kill-session -t <session_name> # destroy a session by name
```

## Switch between sessions

```
    <prefix> (          previous session
    <prefix> )          next session
    <prefix> s          choose a session from a list
```

## Remap prefix
The default prefix is C-b. If you prefer C-a, you need to add this to `~/.tmux.conf`:

```
    set -g prefix C-a
    bind C-a send-prefix
    unbind C-b
```

## Managing windows

```
    # Create a window
    <prefix> c           create a new window

    # Switch between windows
    <prefix> 1           switch to window 1
    <prefix> p           previous window
    <prefix> n           next window
    <prefix> w           choose window from a list

    # Rename the current window
    <prefix> ,

    # Kill the current window
    <prefix> &
```

## Managing panes

```
    # Creating a new pane by splitting an existing one
    <prefix> "          split vertically
    <prefix> %          split horizontally

    # Switching between panes
    <prefix> <direction>     Go to the next pane in that direction
    <prefix> o               go to the next pane
    <prefix> ;               go to the previously used pane

    # Moving panes around
    <prefix> {               move the current pane to the previous position
    <prefix> }               move the current pane to the next position
    <prefix> C-o             rotate window ‘up’ (i.e. move all panes)
    <prefix> M-o             rotate window ‘down’
    <prefix> !               move the current pane into a new separate window (‘break pane’)

    # Resizing panes
    <prefix> M-up, <prefix> M-down, <prefix> M-left, <prefix> M-right resize by 5 rows/columns

    # Applying predefined layouts
    <prefix> M-1             switch to even-horizontal layout
    <prefix> M-2             switch to even-vertical layout
    <prefix> M-3             switch to main-horizontal layout
    <prefix> M-4             switch to main-vertical layout
    <prefix> M-5             switch to tiled layout
    <prefix> space           switch to the next layout

    # Other
    <prefix> x               kill the current pane
    <prefix> q               display pane numbers for a short while
```

## Scroll mode

```
    <prefix> [          Enter scroll mode. q to quit.

    Shift-j             Scroll down
    Shift-k             Scroll up

    y                   Copy
    <prefix> ]          Paste
```

## Restore Tmux session after reboot

* [tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)
* https://github.com/mislav/dotfiles/blob/d2af5900fce38238d1202aa43e7332b20add6205/bin/tmux-session

Refs
* https://superuser.com/questions/440015/restore-tmux-session-after-reboot

## Tmux.conf

* `bind-key -n` means no prefix (https://superuser.com/questions/238545/binding-a-command-in-tmux-without-using-the-prefix-key)
    * Example 1: `bind-key -n C-1 select-pane -t 1`

* Bind copy command to clipboard (https://github.com/tmux/tmux/issues/754)

* Reorder tmux windows (https://unix.stackexchange.com/questions/151329/reorder-tmux-windows)
    * I bind reorder window to `<prefix> n` and `<prefix> p` and by window navigation to `S-Left` and `S-Right`

* Bind prefix to `Capslock` key (https://blog.guilhermegarnier.com/2017/12/increasing-productivity-in-tmux-with-a-single-prefix-key/)

* https://stackoverflow.com/questions/81272/how-to-move-the-cursor-word-by-word-in-the-os-x-terminal

* Workaround for a bug in tmux-resurrect: https://gist.github.com/rootulp/93f67511ae97c20c4d32b600a5ab6a8d


REFERENCES
==========
* [A tmux Primer][a_tmux_primer]

[a_tmux_primer]: https://danielmiessler.com/study/tmux/
