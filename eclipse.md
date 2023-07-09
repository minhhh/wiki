ECLIPSE
=======

### Recommended setup
* Replace tabs by white spaces.
    * `Window->preferences->editors->text editors->insert spaces for tabs`
    * `Window->preferences->editors->text editors->Show whitespace characters`
    * `PHP > Code Style > Formatter > Tab policy `(choose "spaces")
    * `PHP > Code Style > Formatter > Indentation size` (set to 4)

* Open with single click
    * `Window > Preferences > General > Open Mode` (single click)

* Vim binding
    * https://marketplace.eclipse.org/content/vrapper-vim

* Configure Shortcuts `General > Editor > Keys`
    * Set `Show In (Project Explorer)` binding to `C F12`, when `Editing Text`
    * Set `Next Editor` binding to `C Shift [`, when `In Windows`

* Ref [http://www.rossenstoyanchev.org/write/prog/eclipse/eclipse3.html](http://www.rossenstoyanchev.org/write/prog/eclipse/eclipse3.html)

### Openning Windows

```
    C Shift L    - Show shortcuts
    C F7         - Show Next View
    C Shift F7   - Show Previous View
    C O          - Quick Outline
    C F12        - Switch to Editor / Explorer
    Ctrl M       - Maximize Active View or Editor
    C + F6       - Switch between Editor
    C + E        - Switch between open files
    C Option Q,S - Switch to Search
    C Option Q,O - Switch to Outline
    C Option Q,X - Switch to Problems

```

### Moving Around

```
    F3          - Open Declaration
    C Shift G   - Find all occurences
    C L         - Go to Line
```


### Editing

```
    C   D        - Delete Line
    Alt Shift R  - Rename Refactoring
    C Shift F    - Format code
    C /          - Add / remove comments
    C \          - Remove Block Comment
    C Shift X    - To Uppercase
    C Shift Y    - To lower case
    Ctrl Space   - Content Assist  Context sensitive content completion suggestions while editing Java code.
```

### Search and replace

```
    C F       - Find / Replace
    Ctrl H    - Open Search Dialog
```

### Debugging

```
    Ctrl Shift B - Toggle breakpoint
    F9      - Regular Launch
    C F11   - Debug Launch
    F5      - Step in
    F6      - Step over
    F7      - Step return
    F8      - Continue
```

### Changing workspace directory
* Goto `ECLIPSE_HOME\configuration\.settings directory`, edit the `org.eclipse.ui.ide.prefs` file and change the `RECENT_WORKSPACES` value to the desired location.


### Configure Snippet Use Snip Tree View as part of the CFEclipse, which can be installed [http://www.cfeclipse.org/update](http://www.cfeclipse.org/update)
