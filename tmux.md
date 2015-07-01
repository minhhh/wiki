# TMUX
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
    C-b s # List all session

    C-b $ # Rename current session
```

## Attach to a session

```
    tmux a # Attach to first available session

    tmux a -t <session_name> # Attach to session by session name
```

## Detach from a session

```
    tmux detach

    C-b d

    tmux kill-session -t <session_name> # destroy a session by name
```

## Switch between sessions

```
    C-b (          previous session
    C-b )          next session
    C-b s          choose a session from a list
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
    C-b c           create a new window

    # Switch between windows
    C-b 1           switch to window 1
    C-b p           previous window
    C-b n           next window
    C-b w           choose window from a list

    # Rename the current window
    C-a ,

    # Kill the current window
    C-a &
```

## Managing panes

```
    # Creating a new pane by splitting an existing one
    C-a "          split vertically
    C-a %          split horizontally

    # Switching between panes
    C-a <direction>     Go to the next pane in that direction
    C-a o               go to the next pane
    C-a ;               go to the previously used pane

    # Moving panes around
    C-a {               move the current pane to the previous position
    C-a }               move the current pane to the next position
    C-a C-o             rotate window ‘up’ (i.e. move all panes)
    C-a M-o             rotate window ‘down’
    C-a !               move the current pane into a new separate window (‘break pane’)

    # Resizing panes
    C-a M-up, C-a M-down, C-a M-left, C-a M-right resize by 5 rows/columns

    # Applying predefined layouts
    C-a M-1             switch to even-horizontal layout
    C-a M-2             switch to even-vertical layout
    C-a M-3             switch to main-horizontal layout
    C-a M-4             switch to main-vertical layout
    C-a M-5             switch to tiled layout
    C-a space           switch to the next layout

    # Other
    C-a x               kill the current pane
    C-a q               display pane numbers for a short while
```

# REFERENCES
* [A tmux Primer][a_tmux_primer]

[a_tmux_primer]: https://danielmiessler.com/study/tmux/
