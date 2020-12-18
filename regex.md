# PRACTICES
## Meta characters
* `^` (caret) and `$` (dollar) represent the start and the end of a line, respectively.
* Matching any one of several characters: use square brackets `[...]`. This is called a character class.
    * Dash `-` indicates a range of characters, e.g. [0-9] matches digits, [-a-z] matches lowercase characters.
    * Dash at the beginning of a character class means dash , e.g. [-123] matches dash and 1,2,3.
* Not match any one of several characters: use negate at the beginning of a character class: [^...]
* `.` (dot) matches any character.
* `|` (bar) means `or` within parentheses. e.g., (first|1st) matches first or 1st.
* Match word boundary: use meta sequences `\<` and `\>` . e.g., \<cat\> matches the word cat.

## Quantifiers
* Optional item: use `?` (question mark) , e.g., colou?r matches color or colour. It can match a long expression in parentheses, e.g. 4(th)? matches 4 or 4th
* `+` means one or more preceding items.
* `*` means any number of preceding items. So `helll`o +world` matches `hello world`, `hellllo     world` and similar sentences.

## Lazy quantifiers
* Some tools allow lazy quantifiers **,?, +?, ??, {num,num}?**
* This means try to match as little as possible

## Positive quantifiers
* Only supported by Java
* Try to match as much as possible and never giveup.

## Backreference
* Backreferencing is the regex feature that allows you to match new text that is the same as some text matched earlier in the expression.
* `\1`, `\2`, `\3` refers to the first, second, third matched sets. For instance

```
    # for detecting repeated word we can use
    \<([A-Za-z]+) +\1\>
```
<br/>

## Character short hand
* `\a` alert character
* `\b` backspace inside character class.
* `\e` escape character
* `\f` form feed, ASCII FF
* `\n` newline
* `\r` return
* `\t` tab
* `\v` vertical tab

## Octal escape
* From `\000` to `\377`
* `\033` for `ESC`
* `\015\012` for `CR/LF`

## Hex and unicode sequence
* Some version allows `\x` to escape hexadecimal values such as `\x0D\x0A` matches `CR/LF`
* Sometimes use `\u`

## Control character
* `\cchar` maybe used to match control character sequence in some flavors.
* `\cH` matches `Control-H`

## Unicode combining character sequence
* `\X` is a short hand for `\P{M}\p{M}`, which matches a base character possibly followed by several combining characters.

## Unicode properties, scripts and blocks
* `\p{quality}` matches a character with quality while `\P{quality}` matches a chracter that does not.
* `\p{L}` - `\p{Letter}` - things considered letters.
* `\p{M}` `\p{Mark}` – Various characters that are not meant to appear by themselves,
* `\p{Z}` `\p{Separator}` – Characters that separate things, but have no visual representation (various kinds of spaces . . . ).
* `\p{S}`  `\p{Symbol}` – Various types of Dingbats and symbols.
* `\p{N}`  `\p{Number}` – Any kind of numeric character.
* `\p{P}`  `\p{Punctuation}` – Punctuation characters.
* `\p{C}`  `\p{Other}` – Catch-all for everything else (rarely used for normal characters).
* `\p{Script}` matches characters from specific writing system. For instance, `\p{Hebrew}`

## Class shorthands
* `\s` is the generic whitespace which match space, tab, newline, carriage return.
* `\S` is anything but \s
* `\w` matches [a-zA-Z0-9R]
* `\W` anything not ! \w , i.e., ![ˆa-zA-Z0-9R]
* `\d` matches [0-9]", i.e., a digit
* `\D` anything not ! \d , i.e., ![ˆ0-9]

## Class operation
* `.Net` and `Java` offers class subtraction in different flavors
    * `[[a-z]-[aeiou]]` in .net
    * `[[a-z]&&[^aeiou]]` in Java
* Class set operation can be mimicked with look around
    * `(?!\p{Cn})\p{InThai}` is the same as `[p{InThai}` && `[^p{Cn}]]`

## Posix character class
* `[:alnum:]` alphabetic characters and numberic characters
* `[:alpha:]` is alphabetic characters
* `[:blank:]` space and tab
* `[:cntrl:]` control characters
* `[:digit:]` digits
* `[:graph:]` non-blank characters
* and so on
* The advantage of Posix character class is they are locale dependent.
* There is also Posix "collating sequence" for sorting sequence of characters
* There is also Posix "character euquivalents" to indicate certain characters should be considered identical for sorting and such.

## Popular modifier
* `i` modifier comes after `m/patter/i` to do match in case-insensitive manner.
* `g` modifier comes after **s/pattern1/pattern2/g** to do global replace.
* `s` modifier replace pattern1 by pattern 2 in **s/pattern1/pattern2/**
    * Example: get 3 digits after the decimal point if the third is not a zero, otherwise just take 2

```
    $fraction =~ s/(\.\d\d[1-9]?)\d*/$1/
```
<br/>

* **m** modifier:**enhanced line anchor** match mode
* **x** modifier: free format

## Look around: positive look ahead look behind
* Look ahead is done with **(?=..)** and **(?<=..)** is look behind. Look around does not consume text, instead they mark positions.
* For instance, to match Jeff only if it is part of Jeffrey

```
    (?=Jeffrey)Jeff will match 'by Jeffrey Friedl' but not 'by Jefferson Friedl'

    # insert ' to Jeffs
    s/(?<=\bJeff)(?=s\b)/'/g

    # insert , to group of 3 digits such as 123,456,789
    $pop =~  s/\b(?<=\d)(?=(\d\d\d)+\b)/,/g;
```
<br/>


## Look around: negative look ahead and look behind
* Negative look ahead: `?!` successful if cannot match to the right
* Negative look behind **?<!** successful if cannot match to the left

## Enhanced line anchor
* Logical line oriented can be matched by enhanced line anchor mode. In Perl this is the **m** modifier, like this `s/pattern1/pattern2/mg`

## Anchors and other zero-width assertions
* Start of line/string: `^, \A`
* End of line/string: `$, \z, \Z`
* Start of match or end of previous match `\G`. If a match is not successful, the location at which ! \G" matches is reset back to the beginning of the string.

## Word boundary
* `\b, \<, \>, ...` are word boundary. If `\b` is supported, maybe `\B` not word boundary is also supported too.
* Note that \w and \b maynot agree if there are Unicode. In that case, use \p{L} to detect word.

## Mode modifier
* In the form `(?modifier)`, such as (?i)or (?-i)
* (?i) turns on case insensitivity and (?-i) turns it off.
* `x` free spacing adn comment regex mode
* `s` dot matches all match mode
* `m` enhanced line-anchor match mode

## Literal text span
* `\Q` , `\E`  turns off all regex character between them except for \E

## Grouping
* Grouping and capturing by `(...)`
* `?:` groups but do not capture. For instance,

```
    (?:[0-9]*)
    # groups but do not capture a group of digits
```
<br/>

* Some supports name capture. such as
    * `(?P<name>...)` in Python and PHP and can be refered to as (?P=Area)
    * `(?<name>...)` in .NET and can be refered by \k<name>.
* Atomic grouping (?>...) means once the subexpression matches, what it matches become fixed.

## Conditional matching
* `(?if then | else)`
* Match a word optional wrapped in `<>`

```
    (<)?\w+(?(1)>)
```
<br/>

* It can use lookaround as test

```
    # look for a digit after NUM:
    (?(?<=NUM:)\d+<\w+)
```
<br/>


## Mechanics of regular expressions processing
* Types of engine: NFA, POSIX NFA, DFA, Hybrid NFA/DFA
* How they work? TODO

## egrep
* egrep: do regular expressions on a list of files like this

```
    egrep 'regex' file1 file2 ...
```
<br/>


## sed
* sed is perhaps faster than awk but not as powerful. awk can do what sed can and more

## Awk
* Good for one liner task, but a full awk program may not be worth it since you already have Perl or Python

## Perl
* See [[programming:perl]] for the Perl programming language
* Do what sed does

```
    perl -p -e "s/pattern1/pattern2/g" file
```
<br/>

* `qr` operator defines regex object

```
    # match a host name
    $HostnameRegex = qr/[-a-z0-9]+(\.[-a-z0-9]+)+\.(com;edu;info)/i;
```
<br/>

* ASCII escape sequence **\e[7m** and **\e[m** to hilight

```
    \e[7m$1\e[m  then $1 will be hilighted
```
<br/>

* `\N{name}` accesses an unicode by its name, e.g. \N{INVERTED EXCLAMATION MARK}
* `$/` is a variable defining chunk mode ending. Undefine it with `undef $/`.
* `$ARGV` is the file name




# HOWTOS
## Removing the leading path from filename

```
    # for unix file name
    s{^.*/}{}

    # for windows filename, may need aditional slash in Java or PHP
    s{^.*\\}{}
```
<br/>


## Get the file name from a path

```
    # everything at the end that is not a backslash or forward slash
    ([^/]*$)

    # windows
    ([^\\]*$)
```
<br/>


## Get both filename and path

```
    ˆ(.*)/(.*)$

    # or a more verbose version
    ˆ(.*)/([ˆ/]*)$

    # note that if these don't match, it means there is only the filename and no leading path, we should take care of that in the code
```
<br/>


## Replace leading and trailing spaces

```
    s/ˆ\s+//;
    s/\s+$//;
```
<br/>


## Match HTML tags

```
    < # Opening "<"
    ( # Any amount of . . .
        "[ˆ"]+"     # double-quoted string,
        |           # or . . .
        ’[ˆ’]+’     # single-quoted string,
        |           # or . . .
        [ˆ’">] # "other stuff"
        )*
    > # Closing ">"
```
<br/>


## Perl howto
### Check if a regex matches digits

```
    if ($reply =~ m/^\d+$/) {
        print "only digits\n";
    } else {
        print "not only digits\n";
    }
```
<br/>



### Prepend append something to a line

```
    s/^/something/
    s/$/something/
```
<br/>


## egrep howto
### Match case insensitive in egrep

```
    egrep -i ...
```
<br/>


### Match a string within double quotes, but not including those that have ecaped double quotes

```
    "[^"]*"
```
<br/>


### Match html

```
    egrep -i ’\<http://[-a-z0-9R.:]+/[-a-z0-9R:@&?=+,.!/ ̃+%$]+\.html?\>’ files
```
<br/>


### Match html tag

```
    <[^>]*>
```
<br/>


### Match hour representation

```
    egrep '([01]?[0-9]|2[0-3]):[0-5][0-9] (am|pm)'
```
<br/>




# BOOKS
* MASTERING REGULAR EXPRESSIONS
* [Regular expression and sed and awk](http://www.cs.umsl.edu/~sanjiv/classes/cs2750/lectures/re.pdf)
* [Regexcrossword](http://regexcrossword.com) A great website where programmer can play Regex game for fun.


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/minhhh/regex/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

