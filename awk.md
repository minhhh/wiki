AWK CHEATSHEET
==============
## Run
Call from command line

```bash
    awk 'pattern1 {action1}
    pattern2 {action2} ...' file1 file2 ..
```
<br/>

Call a script

```bash
    awk -f script file1 file2 ...
```
<br/>

Call without input files

```bash
    awk 'program'
```
<br/>


## Regular expression
Awk can use regular exrepssion as conditions

```bash
    awk '/foo/ {program}' file
```
<br/>

Awk supports Character class in POSIX standard such as [:alpha], [:alnum:]

### Case sensitivity
Either use function `tolower`

```bash
    tolower($1) ~ /foo/ {...}
```
<br/>

Or set variable `IGNORECASE` to non-zero


```bash
    IGNORECASE = 1
```
<br/>


### Dynamic regex
Awk provides facility to define dynamic regular expressions

```bash
    BEGIN { digits_regexp = "[[:digit:]]+" }
```
<br/>

You shouldn't use string constants for regex because it needs to be processed twice and hard to read.

### Startup and cleanup actions
In other words, do something even if there are no line to process

```bash
    awk 'BEGIN {do something}'
```
<br/>

`END`  specifies command to do at the end of loop.

### Change field seperator
`awk -F:` changes the field separator to colon.

Or it can be set in the BEGIN condition like this

```bash
    BEGIN {FS = "/"}
```
<br/>

### Quote and quoting
Awk support many standard escape sequence that can be use inside strings or regular expression

There are various way to escape single quote and double quotes.

Once nice way is to use octal escape:  `\42` is double quote and `\47` is single quote.

`\xhh` produces hexadecimal escape sequence

### Special Variables
* `$0` is the current line. $1 is the first field, $2 is the second field and so on
* Note that $NR is the first field in the first record, second in the second one, and so on
* $(2x2) is equivalent to $4
* $5 = something when the line has fewer than 5 fields will create the 5th field and change both $0 and NF
* you get the idea
* To force awk to rebuild the record,

```bash
    $1 = $1; # force record to be rebuilt
```
<br/>

* NF is the number of fields
* $NF is the last field.
* NR is the total of records read so far in all files.
* FNR is the number of records read so far in the current input files. This should be used instead of NR.
* RS is the record separator. It can be changed at BEGIN
* ORS is the output record separator.
* RT contains the actual text that match RS if RS is a regular expression. If RS is just a normal character, then RT and RS are the same.
* FS is the field separator
    * FS can be specified at the beginning as well
* OFS is output field separator
* FIELDWIDTHS is a string that specifies field widths separated by spaces.
    * For instance `9 10 6 3 4 ...`
    * If PROCINFO["FS"] "FS" then FS is being used, otherwise fixed width method is being used.

#### Operators
* `~` (tilde) used to match a string with a regular expression

```bash
    $ awk '$1 ~ /J/' file
    # matches line where the first field start with J
```
<br/>

* `!~` not match regular expression
* `==` is the equal operator

### Useful functions
* length() returns the string length.
* substr(s, m, n) produces substring of s beginning at position m and with length n
* tolower(s) , toupper(s) transform text s to all lower or upper cases
* sub("something", "withsomething")
* `getline` read the next line from input, returns 1 if it finds a record, 0 if end of file and -1 if there are any errors.
* `getline tmp` reads the next line from input to a variable named `tmp`, the variable `$0` is not affected by this getline. This function allows to skip one line ahead.
* `getlines var < 'file'` reads the next line from file to a variable named `var`

```bash
    # The following code copies all input files to the output, except for records that say @include filename
    # in this case it will replace such records with the content of the file `filename`
    if (NF 2 && $1 "@include") {
        while ((getline line < $2) > 0)
            print line
        close($2)
    } else
        print
```
<br/>

* `command | getline` . In this case the string `command` is run as a shell command and its output is piped to getline

```bash
    # line begins with @execute is replaced by the output of the command after that
    {
        if ($1 "@execute") {
            tmp = substr($0, 10)
            while ((tmp | getline) > 0)
                print
            close(tmp)
        } else
            print
    }
```
<br/>


* `command | getline var`, the output of `commands` is sent through a pipe to getline and into variable `var`.
* `print "some query" |& "db_server" ` sends a query to a process. (This maybe useful but we don't use it yet)
* Mathematical functions such as: sqrt(), atan2(), rand().
    * DO NOT put a space between the function name and the parentheses. It can be confused with string concatenation
    * Operator precedence.

### Printing and output
* print something, something, ...
* printf "format string", something, something .... Similar to C printf function
* OMFT contains the default format specification when print converts a number to a string
* OFS and ORS do not have any effects on printf
* The print and printf function can be redirected just as in the shell
    * print items > file
    * print items >> file
    * print items | command
    * print items |& command: the output from command can be read with `getline`
    * Some version of awk only allows one open pipe , so we can call print items > file multiple times to append more items to the file, unlike in the shell where we have to use >> the second time onwards.

### Standard descriptors
* Gawk supports special filenames for standard input, output and error streams
    * /dev/stdin
    * /dev/stdout
    * /dev/stderr
    * /dev/fd/N : file associated with descriptor N.

```bash
    print "serious error detected " > "/dev/stderr"
```
<br/>


### Special files for process-related information
* Gwak supports special file for accessing information about the running gawk process.

### Special files for network communication
* Gawk, awk can open two-way TCP-IP connection.

### Close input and output redirection
* `close(filename)` or `close(command)` close the input or output redirection pipe
* `filename` or `command` must `exactly match`

### Piping to sh
A good way to build command line and execute them in the shell is to pipe them to `sh`

```bash
    { printf("mv %s %s\n", $0, tolower($0)) | "sh" }
    END {close("sh")}
```
<br/>

### Change the content of a field
* The content of a field can be change during processing , like this

```bash
    awk '{$2=$2-10; print $0}'
    # will subtract 10 from the second field, and the second field should be
    # a number for this to work.
```
<br/>

#### Variables
* Custom variables can be created and default to zero

```bash
    {
        str = "hello";
    }
```
<br/>

* Variables can be assigned in the command line.
* Strings and number conversions.
* Arithmetic Operators.
* String concatenation is done by placing the operands next to each other
    * `()` should be used around concatenation in all but the most common context
* True and false in awk. Zero and null string is false, other values are true.
* Boolean expressions: `!`, `&&` and `||`. Tenary operator `condition?expression1:expression2`

### Patterns
* Patterns control the execution of rules, a rule is executed when its pattern matches the current input record (line).
* `Record range`  is specified in the form `beginpatter, endpattern`. Every record between inclusive is processed.
    * The range pattern can be turned on and off by the same record.
    * Range pattern cannot be combined with other patterns.

### Control Statements
if-else

```bash
    if (x % 2 0)
        print "x is even"
    else
        print "x is odd"
```
<br/>

while

```bash
    while (i <= 3) {
        print $i
        i++
    }
```
<br/>

do while

```bash
    do {
        print $0
        i++
    } while (i <= 10)
```
<br/>

for

```bash
    for (i = 1; i <= 3; i++)
        print $i
```
<br/>

switch: break

```bash
    switch (NR * 2 + 1) {
    case 3:
        break
    case "11":
        print NR - 1
        break
    case /2[[:digit:]]+/:
        print NR
        break
    default:
        print NR + 1
        break
    case -1:
        print NR * -1
        break
    }
```
<br/>

switch: continue

```bash
    BEGIN {
        for (x = 0; x <= 20; x++) {
            if (x 5)
                continue
            printf "%d ", x
        }
        print ""
    }
```
<br/>

* next: stop processing the current record and go on to the next record
* nextfile : stop processing the current file and go on to the next file
* exit n: stops execution for the current rule and execute the END rule if any.

```bash
    BEGIN {
    if (("date" | getline date_now) <= 0) {
    print "Can’t get system date" > "/dev/stderr"
    exit 1
    }
    print "current date is", date_now
    close("date")
    }
```
<br/>


### Functions
* Controlling output buffering with `system`
    * Use `system("")` to fflush output buffering instead of `fflush`




HOWTOS
======
## How to remove special characters from files
* Suppose you have a list of files starting with a certain number of special character that you want to remove
* The idea is to generate the new file name for each of the files then use the `mv` or `rename` command to change the orginal file name
* First, export the list of filenames to a first file test1

```bash
    # Suppose that the original files are in folder original_files and we want to copy them to
    # folder new_files
    ls original_files > list1 # generate list of files
    awk '{gsub(/[^a-zA-Z0-9 .]/, "", $0); print;}' list1 > list2 # removes all special characters and generate a second list

    # combine list1 and list2 to a list of shell command in list3
    # We will use strong quoting
    awk '{gsub(/\47/, "\47\\\47\47", $0); str = $0; getline < "list2"; print "cp -f \47original_files/"str "\47 \47new_files/"$0"\47" > "list3";}' list1

    sh list3 # run the list of commands in list3
    rm -frv list1 list2 list3 # remove all temporary files
```
<br/>

## Make each character a separate field
* By changing the field separtor to null string

```bash
    BEGIN {FS=""}
```
<br/>





# BOOKS
* [Gwak Effective awk programming](http://www.gnu.org/software/gawk/manual/gawk.pdf) - Free book, great for understanding details about awk and gawk programming.
* [Why you should learn just a little Awk - An Awk Tutorial by Example](http://gregable.com/2010/09/why-you-should-know-just-little-awk.html) 




# ARTICLES
* [Differences between different versions of awk](http://www.differencebetween.net/technology/software-technology/difference-between-gawk-and-awk/)
* [http://www.thegeekstuff.com/2011/06/awk-nawk-gawk/](http://www.thegeekstuff.com/2011/06/awk-nawk-gawk/).
