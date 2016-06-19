# BOOKS
* [Easily installing third-party .el files](http://edward.oconnor.cx/2005/09/installing-elisp-files)
* [http://www.saltycrane.com/blog/2010/05/my-emacs-python-environment/](http://www.saltycrane.com/blog/2010/05/my-emacs-python-environment/)
* [Speed up your emacs skill](http://sites.google.com/site/steveyegge2/effective-emacs)
* [Basic emacs setup](http://www.yilmazhuseyin.com/blog/dev/basic-emacs-setup/)

### Keys and shortcut
Starting and Closing Emacs

    |emacs -nw| Start emacs in terminal mode |
    |C-z| Suspend emacs |
    |C-x C-c| Kill emacs |
    |C-x ESC ESC| Repeat command |
    |C-g| Cancel command |
    |M-x| Execute a command |
    |C-u| Universal argument |
    |M-number command|Execute a command a number of times|

Files

    |C-x C-f| Find files |
    |C-x C-s| Save file |
    |C-x C-d| Open directory |
    |C-x s| Save all file |
    |C-x C-w| Save file as |
    |C-x i| Insert file |

Using help

    |C-h f| Describe function |
    |C-h c| Describe key briefly |
    |C-h a| Search for a command |
    |C-h k| Describe key |
    |C-h b| Describe bindings |
    |C-h i| Top level info |
    |C-h r| Read emacs manual |
    |C-h t| Read emacs tutorial |

Navigating between buffer

    |C-x C-b| List buffer |
    |C-x b| Switch to another buffer |
    |C-x 0| Delete window |
    |C-x 1| Delete other window |
    |C-x o| Switch cursor to the other window |
    |C-x C-right| Next buffer |
    |C-x C-left| Last buffer |
    |C-x 2| Split window vertically |

Moving around

    |C-a| To line beginning |
    |C-e| To line end |
    |C-w| Delete word backward |
    |C-q| Delete word forward |
    |M-g g| Go to line |
    |C-SPC| Set mark here |
    |C-x C-x| Exchange point and mark |
    |C-x h| Mark entire buffer |
    |ESC <| Go to the beginning of the buffer|
    |ESC >| Go to the end of the buffer|
    |C-v| view next screen |
    |M-v view previous screen |
    |C-M-h| Mark function |
    |C-l| Center line |
    |C-M-a| Move a function backwards |
    |C-M-a| Move a function forwards |
    |M-h| Mark paragraph |
    |C-u C-SPC| Cycle through mark ring|
    |M-x savehist-save | Save history |
    |M-x savehist-mode | Turn on save history mode |
    |M-x imenu | Search for a function |
    |M-x imenu-add-to-menubar | Add function lists to menu bar |
    |M-x speedbar| Outline the files in current folder |  <- VERY USEFUL |

Search and replace

    |C-s| Search forward |
    |C-r| Search backward |
    |M-%| Query replace |
    |SPC| Replace this one, go on to

### Setup Emacs
Put the `.el` files in your `~/.emacs.d/` directory. Then add the line below to your `~/.emacs`

    ;; Tell emacs where is your personal elisp lib dir
    ;; this is default dir for extra packages
    (add-to-list 'load-path "~/.emacs.d/")

### Autocomplete mode
    ;; Enable autocomplete mode
    (add-to-list 'load-path "~/.emacs.d/auto-complete/")
    (require 'auto-complete-config)
    (add-to-list 'ac-dictionary-directories "~/.emacs.d/auto-complete/ac-dict/")
    (ac-config-default)
    (auto-complete-mode t)
    (setq ac-auto-show-menu 0.0) ;; show completion menu immediately

### Open anything


### Open directory navigation bar

    ;; Speedbar
    (speedbar)

### Save/load history

    ;; Reopen last files and keep recent files
    (desktop-save-mode 1)
    (defun my-desktop-save ()
        (interactive)
        ;; Don't call desktop-save-in-desktop-dir, as it prints a message.
        (if (eq (desktop-owner) (emacs-pid))
            (desktop-save desktop-dirname)))
    (add-hook 'auto-save-hook 'my-desktop-save)

### Search replaces in files
* [http://stackoverflow.com/questions/270930/using-emacs-to-recursively-find-and-replace-in-text-files-not-already-open](http://stackoverflow.com/questions/270930/using-emacs-to-recursively-find-and-replace-in-text-files-not-already-open)
* [http://emacsredux.com/blog/2013/04/28/switch-to-previous-buffer/](http://emacsredux.com/blog/2013/04/28/switch-to-previous-buffer/)

    (eval-after-load "helm-regexp"
    '(helm-attrset 'follow 1 helm-source-moccur))

    (defun my-helm-multi-all ()
    "multi-occur in all buffers backed by files."
    (interactive)
    (helm-multi-occur
    (delq nil
            (mapcar (lambda (b)
                    (when (buffer-file-name b) (buffer-name b)))
                    (buffer-list)))))

    (global-set-key (kbd "C-O") 'my-helm-multi-all)

### Line manipulation

### Multicusor

### General stuff

    ;; Set window title to full filename
    (setq frame-title-format '("Emacs @ " system-name ": %b % %  %f"))

    ;; show paren mode
    (show-paren-mode t)

    ;; show column
    (setq column-number-mode t)

    ;; change tab to 4 spaces
    (setq tab-width 4)
    (setq-default indent-tabs-mode nil)

    ;; Enable whitespace
    (global-whitespace-mode t)

#### Install
* cperl-mode for Perl
* autopair
* slime for LISP
* ido
* autocomplete mode
* show-paren-mode

#### Useful functions
Untabify
  * Use `M-x untabify`, `tab-width` should be modified according to your reference first.
  * Use `whitespace-mode` to show tab, space, and special characters.

delete-trailing-whitespace



### Your recommended .emacs
Note: tab-to-tab-stop works with tab-stop-list. It has nothing to do with the key TAB, unless TAB is bound to tab-to-tab-stop. In many modes, TAB is bound to code completion or `indent-relative`.

    (load "~/elisp/autoloads" 'install)
    (add-to-list 'load-path "~/elisp") ; directory of .el files

    ;slime mode
    (add-to-list 'load-path "~/elisp/slime")
    (require 'slime)
    (add-hook 'lisp-mod-hook (lambda () (slime-mode t)))
    (add-hook 'inferior-lisp-mod-hook (lambda () (inferior-slime-mode t)))
    (setq inferior-lisp-program "clisp")

    ; enable IDO mode
    (require 'ido)
    (ido-mode t)
    (setq ido-enable-flex-matching t) ;; enable fuzzy matching

    ; enable auto-complete mode
    (add-to-list 'load-path "~/elisp/auto-complete/")
    (require 'auto-complete-config)
    (add-to-list 'ac-dictionary-directories "~/elisp/auto-complete/ac-dict/")
    (ac-config-default)
    (auto-complete-mode t)

    ; Set window title to full filename
    (setq frame-title-format '("Emacs @ " system-name ": %b %+%+ %f"))

    ; Use Ctr-x Ctrl-m for Alt-x
    (global-set-key "\C-x\C-m" 'execute-extended-command)
    (global-set-key "\C-x\C-m" 'execute-extended-command)

    ; C-w for killing word backword, C-q for killing forward
    ; C-x C-k for kill region
    (global-set-key "\C-w" 'backward-kill-word)
    (global-set-key "\C-q" 'kill-word)
    (global-set-key "\C-x\C-k" 'kill-region)
    (global-set-key "\C-c\C-k" 'kill-region)

    ;; C ; for backward delete
    (global-set-key (kbd "C-;") 'delete-backward-char)

    ;; show paren mode
    (show-paren-mode t)

    ;; show column
    (setq column-number-mode t)

    ;; change tab to 4 spaces
    (setq tab-width 4)
    (setq-default indent-tabs-mode nil)

Use the recommended `Makefile` and compile your `el` files.
