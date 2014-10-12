# COMMANDS
### Services

```bash
    #start, stop
    sc start "service"

    #remove service
    sc delete "service"
```
<br/>




# POWERSHELL
### How to rename multiple files
* [http://notgartner.wordpress.com/2006/10/26/fun-with-scripting-shells-how-to-rename-multiple-files-in-powershell/](http://notgartner.wordpress.com/2006/10/26/fun-with-scripting-shells-how-to-rename-multiple-files-in-powershell/)

### List only Files and/or only Folders using PowerShell
* [http://technologist.pro/systems/list-only-files-andor-only-folders-using-powershell](http://technologist.pro/systems/list-only-files-andor-only-folders-using-powershell)

### List only files with full names

```bash
    Get-ChildItem -Recurse | where {!$_.PsIsContainer} | Select-Object FullName
```
<br/>





# WINDOWS HOWTO AND TROUBLESHOOTING
### Move program files to external drive
* [http://www.tested.com/tech/2341-how-to-move-your-apps-and-user-files-to-a-secondary-drive/](http://www.tested.com/tech/2341-how-to-move-your-apps-and-user-files-to-a-secondary-drive/)

### Access ext2, ext3 in Windows
* [ext2fsd](http://www.ext2fsd.com/)
* [Other ways](http://www.howtoforge.com/access-linux-partitions-from-windows)

### Share hidden folder
If a sharename has a **$** (dollar sign) at the end of it, the share becomes hidden and does not appear in listing, though you can still acccess it through it's UNC name.

### How to fix intel 855 problem on windows 7
* [http://www.groundstate.net/855GMWin7.html](http://www.groundstate.net/855GMWin7.html)

### Install windows 7 from USB
* [Install Windows 7 Or Windows 8 From USB Drive](http://www.intowindows.com/how-to-install-windows-7vista-from-usb-drive-detailed-100-working-guide/)

### Use Ctrl+Alt+Del when logon
* [http://www.tudy.ro/2006/10/16/enable-ctrl-alt-del-at-login-screen/](http://www.tudy.ro/2006/10/16/enable-ctrl-alt-del-at-login-screen/)

How to do this:
  * Press the START button, go to Run
  * Type control userpasswords2, and then press ENTER
  * Click on the Advanced tab
  * Check the box in the Secure Login section
  * Click Apply and then Reboot, and the Ctrl-Alt-Del login screen should appear


### Change the product key on Windows XP
**Reference:** [http://articles.techrepublic.com.com/5100-10878_11-5034890.html?tag=3Drbxccnbtr1](http://articles.techrepublic.com.com/5100-10878_11-5034890.html?tag=3Drbxccnbtr1)

### How to remove Windows services
**Reference:** [http://www.governmentsecurity.org/forum/index.php?showtopic=3D3339](http://www.governmentsecurity.org/forum/index.php?showtopic=3D3339)

Use the `sc` tool:

    sc delete


### How to reset Administrator password
**Reference:** [http://www.ke= llys-korner-xp.com/win_xp_passwords.htm](http://www.ke= llys-korner-xp.com/win_xp_passwords.htm)

### Install SSH on Windows
1. Install OpenSSH
2. Synchronize windows users
        mkpasswd --local > opensshpath/passwd
        mkgroup'' ''--local > opensshpath/group


### XP Myths
**Reference:** [http://home.comc= ast.net/~SupportCD/XPMyths.html](http://home.comc= ast.net/~SupportCD/XPMyths.html)

### How to turn on automatic logon in Windows XP
**Reference**: [http://support.microsoft.com/kb/315231](http://support.microsoft.com/kb/315231)

1. Click **Start**, and then click **Run**.
2. In the **Open** box, type
   **control userpasswords2**, and then **click OK**.

    **Note**: When users try to display help information in the = User Accounts window in Windows XP Home Edition, the help information is not displayed. Additionally, users receive the following error message:

>    Cannot find the Drive:\Windows\System32\users.hlp Help file. Check to see the file exists on your hard disk drive. If it does not exist, you must reinstall it.

3. Clear the "Users must enter a user name and password to use this computer" check box, and then click **Apply**.
4. In the **Automatically Log On** window, type the password in the **Password** box, and then retype the password in theConfirm Password box.
5. Click **OK** to close the **Automatically Log On window**, and then click **OK** to close the **User Accounts** window.

### How to use Enterprise Architect without a license
* Get Installation Files
    * Sandboxie can be found on the Internet.
    * EA: Ask around for the trial version setup file.
* Install Sandboxie
* Start Sandboxie
    * will find an icon on the Task Tray. Right click and Open Main Window.
* Function > Run Sandboxed > Windows Installer Service.
* Install EA Sandboxed
    * Right click on EA Installation File and choose Run Sandboxed
* Start EA Sandboxed
    * Function > Run Sandboxed > From Start Menu. Then choose Enterprise
      Architect from the poped up Start Menu Using Enterprise Architect without a license 3
* Reinstall EA
    * When your EA expires, you can create a new Sandbox and start the whole
      process again.

### How to force MSC mode on XP with WMP 10
Reference: [http://www.anythingbutipod.com/forum/showthread.php?t=12426](http://www.anythingbutipod.com/forum/showthread.php?t=12426)

I've bought a Sansa Express mp3 player and even though it's good for the price, I couldn't get my Windows XP to recognize it as a normal USB drive. It turned out that because I've installed Windows Media Player (WMP) 10 which come with MTP driver taking precedence over MSC driver, consequently prohibiting SE to be recognized as normal USB drive. So the trick is to remove MTP and install SE using MSC.

In this [http://www.anythingbutipod.com/forum/showthread.php?t=12426](http://www.anythingbutipod.com/forum/showthread.php?t=12426), mail1548074 and winwithben have provided 2 methods for SE to work with MSC.

mail1548074's method requires registry modification and a complete removal of MTP driver, then reinstall SE using MSC.

winwithben's alternative method allows you to switch between MTP and MSC.
