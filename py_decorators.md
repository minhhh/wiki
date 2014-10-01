# PYTHON DECORATOR TUTORIAL
Decorators are a powerful tool for getting rid of code duplication, aka following DRY principle. It also helps with standardization of code in a project without forcing developers to remember predefined snippets or patters. In this tutorial, we'll discover how to create and use them.

Another important point to note is I'm aiming for practical value of the decorators so there will be no `foo`, `bar` examples, all examples must solve real world problem and/or taken from good source.

## First level
We all know memoization and probably implement it as a function that takes an arbitrary function and return a memoized function:

    memoized_factorial = construct_memoize(factorial)

This is extremely cumbersome if `factorial` is a method of some class because then we have to use temporary variable to store the memoized function and somehow reassign it to the method. We want some way to elegantly do all the manual things to make a memoized version of a function, this is where `decorator` comes in.

In its simplest form, a decorator is a function that takes the original function and returns a `decorated function`

    cache_obj = {}

    def cache(func):
        def inner(*args, **kwargs):
            global cache_obj
            key = str(args) + str(kwargs)
            if key not in cache_obj:
                cache_obj[key] = func(*args, **kwargs)
            else:
                print "Get from cache {}".format(key)
            return cache_obj[key]
        return inner

    @cache
    def sum(a, b):
        """Sum 2 numbers
        """
        return a + b

Here, `cache(func)` is called, passing original `func` to the decorator, then replace `func` with whatever function is returned from `cache(func)`.

Using global cache object `cache_obj` is not a great idea, because different functions can have the same arguments, then your cache is overwritten. It's better to assign the cache object directly to the original function

    def memoize_2(func):
        if not hasattr(func, 'cache'):
            func.cache = {}
        def inner(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in func.cache:
                func.cache[key] = func(*args, **kwargs)
            else:
                print "Get from cache {}".format(key)
            return func.cache[key]
        return inner

    @memoize_2
    def multiply(a, b):
        """Multiply 2 numbers
        """
        return a * b

    multiply(1,2)
    multiply(1,2)

This decorator is nice, but in practice nobody does this, and it's too bad that a lot of tutorials keep giving these non-working examples. The reason is the new decorated function lose all its original information such as name, docstring, module name.

    print multiply.__doc__ # None

To keep these information, we use `functools.wrapper`

    import functools
    def memoize(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = str(args) + str(kwargs)
            if not hasattr(func, 'cache'):
                func.cache = {}
            if key not in func.cache:
                func.cache[key] = func(*args, **kwargs)
            else:
                print "Get from cache {}".format(key)
            return func.cache[key]
        return inner

    print multiply.__doc__ # Multiply 2 numbers



memoization
https://speakerdeck.com/pablito56/python-decorators-demystified

## Class decorators


# REFERENCES
[Python Decorator Library][python_decorator]

[python_decorator]: https://wiki.python.org/moin/PythonDecoratorLibrary  "Python Decorator Library"
