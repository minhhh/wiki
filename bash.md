BASH
====

References
----------
### General Documents, Books, Tutorials
* [Advanced Bash Scripting Guide][advanced_bash_scripting_guide]
* [Sample Bash files][sample_bash_files]
* [Community Bash Style Guide][community_bash_style_guide]

### Linting
* [Shellcheck][shellcheck]
* [Grunt Lint Bash][grunt_lint_bash]
* [SHLint][shlint]
* [checkbashisms][checkbashisms]

### Unit Testing
* [bats][bats]
* [shunit2][shunit2]
* [sharness][sharness]

### Profiling
* [bashprof][bashprof]

### Debugging
* [Debugging Bash][debugging_bash]
* [bashdb][bash_debugger]



Basics
------

### Shell variables

* PS1 stands for "Prompt String One" or "Prompt Statement One", the first prompt string (that you see at a command line).
* PS2 The secondary prompt string. ie for continued commands (those taking more than one line). The default value is ‘> ’.

### Run a bash script
Forking a new shell

```bash
    # dot slash
    ./script.sh

    # specifying the shell interpreter
    bash script.sh
```

Executes the script in the current shell without forking a new shell

```bash
    # dot space dot slash
    . ./script.sh

    # source command : similar to dot space dot slash
    source script.sh
```

### Block Comment

```bash
    #! /usr/bin/env bash
    : <<COMMENT
    Copyright (C) 2012 Author <author at gmail dot com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation version 3.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    COMMENT

    version="v0.1.1"
```

### Looping in bash
* [Bash for loop example][bash_for_loop]


### Exit on error with set -e
* Call `set -e` in your bash and it will exit if any command returns any error.
* Call `set -evx` or `bash -evx script.sh` to debug script.

### Get current bash file folder

```bash
    DIR="$( cd -P "$( dirname "$0" )" && pwd )"
```




[advanced_bash_scripting_guide]: http://tldp.org/LDP/abs/html/
[sample_bash_files]: https://code.google.com/p/bashscripts/downloads/list
[bash_for_loop]: http://www.thegeekstuff.com/2011/07/bash-for-loop-examples/
[debugging_bash]: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_02_03.html
[bash_debugger]: http://bashdb.sourceforge.net/bashdb.html
[basic_operator]: http://www.tutorialspoint.com/unix/unix-basic-operators.htm
[shellcheck]: https://github.com/koalaman/shellcheck
[grunt_lint_bash]: https://www.npmjs.org/package/grunt-lint-bash
[shlint]:  https://github.com/duggan/shlint
[checkbashisms]: http://manpages.ubuntu.com/manpages/natty/man1/checkbashisms.1.html
[community_bash_style_guide]: https://github.com/azet/community_bash_style_guide/blob/master/README.md
[bashprof]: https://github.com/sstephenson/bashprof
[bats]: https://github.com/sstephenson/bats
[shunit2]: https://code.google.com/p/shunit2/
[sharness]: https://github.com/mlafeldt/sharness
