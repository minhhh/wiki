# WRITING COMMAND-LINE PROGRAMS IN PYTHON
## Why
* Command line programs live forever (like vampires). You want to make good command line programs for future usage.
* Command line programs are easier to write (than GUI app)
* Command line programs are easily composable

## Command line parsing
* Lots of options

| In the box     | 3rd Party |
| -----------    | --------- |
| Do it yourself | docopt    |
| getopt         | clint     |
| optparse       | click     |
| argpass        | compago   |

## Input & Output
* `stdout` is for the output that your program produces
* `stderr` can be used for information on how the program is running, i.e. logging.

## Logging
* `logging` is a powerful library

## istty
* Indicate whether the `stdout`, `stdin` and `stderr` stream is attached to pipe.

## Color
* `click.secho`
* `clint.textui.puts`
* `colorama`

## Progress bar
* `progressbar2`

## Configuration
* Lots of choices

| In the box       | 3rd Party       |
| -----------      | ---------       |
| INI              | YAML            |
| environment vars | Java properties |
| JSON             |                 |
| CSV              |                 |
| XML              |                 |
| PLIST            |                 |
| Do-it-yourself   |                 |

* INI files. Use `ConfigParser` library

## Signals
* `import signal`
* KeyboardInterrupt: handle this and not throw a lot of stacktrace

## Exit code
* Normal termination exits with 0
* Uncaught exceptions exits with 1
* Use `errorno` for more exit codes




# REFERENCES
* [Writing Awesome Command-Line Programs in Python][writing_awesome_cli]



[click]: http://click.pocoo.org/4/
[docopt]: http://docopt.org/
[writing_awesome_cli]: https://www.youtube.com/watch?v=gR73nLbbgqY
