# SCREEN
Screen is best described as a terminal multiplexer. Using it, you can run any number of console-based applications--interactive command shells, curses-based applications, text editors, etc.--within a single terminal. Screen prevents a session from “timing out” or disconnecting SSH connections or local terminal emulators. This makes screen a better alternative to `nohup`.

Screen is freely available on most OSs.

## Creating a new screen sessions
```
    screen -U # Don't forget the -U if you want unicode
    screen -S # start a new screen session with session name
```

## Basic commands

```
    Ctrl-A-C new window
    Ctrl-A-A Switch window
    Ctrl-A-N Next window
    Ctrl-A-P Previous window
    Ctrl-A-W List windows
```

## Detach and attach session

```
    Ctrl-A-D Detach current session

    screen -ls # List sessions

    screen -r # If there's only one session
    screen -r 23034 # If there's multiple sessions

    screen -x # attaching to a running session

    screen -d <name> # detach a running session
```

## Scroll up and down
```
    Ctrl-A [ # then using Vim navigation. q to quit
```
* [GNU/Screen Scroll Up and Down Look At Data](http://www.cyberciti.biz/faq/scroll-up-down-look-at-data-in-gnuscreen-using-pageup-pagedown-keys/)

## screen and vim
To make vim works with screen, showing correct colors, put the following in `~/.screenrc`

```
    shell "bash"
    startup_message off
    vbell off
    altscreen on
    attrcolor b ".I"
    defbce "on"
    termcapinfo xterm* 'is=\E[r\E[m\E[2J\E[H\E[?7h\E[?1;4;6l'
    termcapinfo xterm 'Co#256:AB=\E[48;5;%dm:AF=\E[38;5;%dm'
    term screen-256color
```

