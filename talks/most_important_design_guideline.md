# SUMMARY

    Title: The Most Important Design Guideline
    Date: 2014-11-19
    Speaker: Scott Meyers
    Conference: Confu
    Tags: design

Url: https://www.youtube.com/watch?v=5tg1ONG18H8

Pdf: http://martinfowler.com/ieeeSoftware/designGuideline.pdf

What’s the single most important design guideline for the creation of high-quality software? For Scott Meyers, it’s all about interface design

# THE MOST IMPORTANT DESIGN GUIDELINE
## Interface types
* Encountered by everyone
    * GUI/gestures interfaces
    * cmdline interfaces
    * speech interfaces
* Encountered by software developers
    * Library interfaces
    * Module interfaces
    * Class interfaces
    * Method interfaces
    * Generics and template interfaces

## Interface users
* Experienced with software
* Willing to read documentation
* Motivated
* Want to succeed

## Make interfaces easy to use correctly and hard to use incorrectly
* If an action is possible, it should almost always do the right thing
* If an action is unlikely to do the right thing, it should generally be impossible.
* Shoot for the "pit of success"

## Adhere to the principle of least atonishment
* Strive to maximize the likelihood that the user expectation about the interface are correct
    * Sometimes expectations are just guesses: your job is to maximize the odds that the guesses are correct
    * If users can do something, it should do what they expect
        * Applies both to GUI and API
    * If users know what they want to do, they should be able to guess how to do it
        * If they can't, it should seem sensible after they learn how
* Counter-example
    * Windows Start button
    * Eject CD/DVD on Mac
    * Large fonts in Windows XP don't work at all
    * QT installation on Windows
        * Path cannot contains spaces?!
    * Expedia
    * Pocket Informant
* General techniques
    * Avoid gratuitous incompatibilities with the surrounding environment
        * Take advantage of what peole already know
    * Offer natural syntax
        * E.g. In APIs, use the expected operators and function names
    * Offer intuitive semantics
        * In APIs, when in doubt, do as the built-in or standard libraries do
        * In GUIs, try to have mouse, shortcuts and gestures mean the "usual things"
* Choose good names
    * libraries, modules, namespaces, etc.
    * classes, enums, typedefs etc.
    * members, attributes, properties etc.
    * constants, objects, variables, etc.
    * messages
    * menu entries, dialog options
    * environment variables
* Better button labels reduce the "gulf of execution"
    * Distance from what you want to do to how to do it
* API counter example
    * `equal_range` is based on equivalence, not equality

## Be consitent
* GUICounterExample
    * From Bank of America
* Cross-platform counter example
    * Mail:IPad
* Cross-device counterexample
    * Marriot rewards
* Java counter example
    * array.length
    * string.length()
    * List.size()
* .NET framework library
    * Array.Length
    * ArrayList.Count
* From the C Standard library
    * fscanf, fgetpos, fseek have `FILE*` as the first parameter
    * fgets, fputc have `FILE*` as the last parameter
* From the C++ standard library
    * function to eliminate all container elements with a given value: `erase`
    * For `list`, `forward_list` use `remove`
* From the C++ standard library
    * sort runs in `nlgn` time or won't compile
        * if it can't run quickly, it won't run at all
    * `binary_search` runs in `lgn` time if it can, linear time if it can't
        * if it can run at all, it does, even if it's not fast
* From the C++ standard library
    * `std::sort` not guaranteed to be stable
    * `std::stable_sort` guaranteed to be stable
    * `std::list::sort` guaranteed to be stable

## Use progressive disclosure
* Distinguish `normal` from `expert` level controls
    * Avoid overwhelming users with choices
* Applicable to API design
    * Bundled advanced functionality into separate objects
        * Functionality hidden unless such objects are requested
* Example: JButton

## Document before implementing
* Proven way to discover interface problem
    * Unpleasant to explain -> unpleasant to use
* Issues discussed often become obvious
    * Surprising or underspecified behavior
    * Bad names
    * Inconsistencies in names, conventions, layouts, etc
* Consistent with TDD

## Introduce new Types
* Assume the existence of static type checking
* Many errors can be prevented through stronger typing
* `Date` example
    * `Date(int, int, int)` vs `Date(Day, Month, Year)`
* Constrain values
    * Justifies effort vs cost of mistake

## Avoid overreliance on string
* Naked string is a type sink
* Different types facilitate type-specific formatting and validation code

