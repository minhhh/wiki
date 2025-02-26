# INTRODUCTION

This is the list of some useful tools I used to setup my OSX.

For more awesome osx command lines, see [Awesome OS X Command Line][awesome_osx_command_line].

# SETUP

* [Fix the home and end keys](http://lifehacker.com/225873/mac-switchers-tip--remap-the-home-and-end-keys)

* [Make Your Keyboard Keys Repeat Properly](http://lifehacker.com/5826055/make-your-keyboard-keys-repeat-properly-when-held-down-in-mac-os-x-lion)
```
defaults write -g ApplePressAndHoldEnabled -bool false

defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false              # For VS Code
defaults write com.microsoft.VSCodeInsiders ApplePressAndHoldEnabled -bool false      # For VS Code Insider
defaults write com.vscodium ApplePressAndHoldEnabled -bool false                      # For VS Codium
defaults write com.microsoft.VSCodeExploration ApplePressAndHoldEnabled -bool false   # For VS Codium Exploration users
defaults delete -g ApplePressAndHoldEnabled                       
```

* [Use Fn key normally in Mac](https://support.apple.com/kb/HT3399)
    * System Settings > Keyboard > Keyboard Shortcut > Function Keys > Use F1, F2, etc keys as standard function keys

* [Disable automatic spelling](http://macs.about.com/od/OSXLion107/qt/Os-X-Lion-Automatic-Spelling-Correction.htm)

* [Word Movement Shortcuts for iTerm](http://www.michael-noll.com/blog/2007/01/04/word-movement-shortcuts-for-iterm-on-mac-os-x/)

* Terminal settings
    * Settings > Profiles > Keyboard > Use option as Meta key

# OSX SHORTCUTS & KEYS

```bash
    F11             - Show desktop
    Ctrl left/right - Scroll to the next working desktop
    Command Space   - Show search
    Ctrl Up         - Show all programs
    Ctrl Down       - Show other windows of the same program
    Ctrl Command F  - Toggle full screen
    Cmd Option D    - Toggle taskbar
    Cmd Delete      - Move to trash
    Cmd K           - Clear terminal screen
```

* Setup `Command + Option + Space` to switch Input Source
    * Go to System Settings > Keyboard > Keyboard Shortcuts > Input Sources. Choose `Command + Option + Space`
    * Also go to System Settings > Keyboard > Spotlight and uncheck `Shot Finder Search Window`


# TOOLS

* Testdisk - Disk recovery
* Blackmagic Disk Speed Test - Disk performance measurement tool.
* [iexplorer](http://www.macroplant.com/iexplorer/) - Transfer file with iPhone easily

## QuickSilver

* Great replacement for spotlight

## Diff tools

* [Meld](http://scoobygalletas.blogspot.com/2011/09/how-to-install-meld-in-mac-os-x-lion.html)




# MOUNT SSH

Install sshfs. Then run

```bash
    sshfs <username>@<ip>:<folder> /Users/<username>/<folder>
```



[awesome_osx_command_line]: https://github.com/herrbischoff/awesome-osx-command-line
