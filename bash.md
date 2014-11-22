# BASH

## References
### General Documents, Books, Tutorials
* [Advanced Bash Scripting Guide][advanced_bash_scripting_guide]
* [Sample Bash files][sample_bash_files]
* [Community Bash Style Guide][community_bash_style_guide]

### Linting
* [Shellcheck][shellcheck]
* [Grunt Lint Bash][grunt_lint_bash]
* [SHLint][shlint]
* [checkbashisms][checkbashisms]

## Basics

### Run a bash script
There are two ways to run a bash script:
  * Forking a new shell

    # dot slash
    ./script.sh

    # specifying the shell interpreter
    bash script.sh


  * Executes the script in the current shell without forking a new shell

    # dot space dot slash
    . ./script.sh

    # source command : similar to dot space dot slash
    source script.sh


### Create custom command
Create sh file and put them in /usr/bin OR

Create sh file in ~/bin and symlink to them from /usr/bin

### Sample bash file

    #! /usr/bin/env bash
    : <<COMMENT
    Copyright (C) 2012 Tri Le <trile7 at gmail dot com>

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

    version="findtools v0.3.1"


Using #!/usr/bin/env in case bash is not located where we expected.

Use COMMENT as marker for block comment in Bash. Or we can use any string, just make sure it doesn't appear in the text.

### Looping in bash

    for i in {1..10}; do echo $i; done


### Exit on error with set -e
  * Call `set -e` in your bash and it will exit if any command returns any error. Good for test scripts.

### Change dir

    E_XCD = 86
    cd $DIR || {
    echo "Cannot change to necessary directory." >&2
    exit $E_XCD;
    }


### Get current bash file folder

    DIR="$( cd -P "$( dirname "$0" )" && pwd )"







[advanced_bash_scripting_guide]: http://tldp.org/LDP/abs/html/
[sample_bash_files]: https://code.google.com/p/bashscripts/downloads/list
[bash_for_loop]: http://www.thegeekstuff.com/2011/07/bash-for-loop-examples/
[debugging_bash]: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_02_03.html
[bash_debugger]: http://bashdb.sourceforge.net/bashdb.html
[basic_operator]: http://www.tutorialspoint.com/unix/unix-basic-operators.htm
[shellcheck]: (https://github.com/koalaman/shellcheck)
[grunt_lint_bash]: (https://www.npmjs.org/package/grunt-lint-bash)
[shlint]: (https://github.com/duggan/shlint)
[checkbashisms]: (http://manpages.ubuntu.com/manpages/natty/man1/checkbashisms.1.html)
[community_bash_style_guide]: (https://github.com/azet/community_bash_style_guide/blob/master/README.md)
