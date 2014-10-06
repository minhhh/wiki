# PYTHON DECORATOR TUTORIAL
Decorators are a powerful tool for getting rid of code duplication, aka following DRY principle. It also helps with standardization of code in a project without forcing developers to remember predefined snippets or patters. In this tutorial, we'll discover how to create and use them.

Another important point to note is I'm aiming for practical value of the decorators so there will be no `foo`, `bar` examples, all examples must solve real world problem and/or taken from good source.

## First level
We all know memoization and probably implement it as a function that takes an arbitrary function and return a memoized function:

```python
    memoized_factorial = construct_memoize(factorial)
```

This is extremely cumbersome if `factorial` is a method of some class because then we have to use temporary variable to store the memoized function and somehow reassign it to the method. We want some way to elegantly do all the manual things to make a memoized version of a function, this is where `decorator` comes in.

In its simplest form, a decorator is a function that takes the original function and returns a `decorated function`

```python
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
```

The `@` is a special syntax that applies the decorator function to the underneath function or class. Here, `cache(func)` is called, passing original `func` to the decorator, then replace `func` with whatever function is returned from `cache(func)`.

Using global cache object `cache_obj` is not a great idea, because different functions can have the same arguments, then your cache is overwritten. It's better to assign the cache object directly to the original function

```python
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
```

This decorator is nice, but in practice nobody does this, and it's too bad that a lot of tutorials keep giving these non-working examples. The reason is the new decorated function lose all its original information such as name, docstring, module name and so on.

```python
    print multiply.__doc__ # None
```

To keep these information, we use `functools.wrapper`

```python
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
```

Now the decorated function also retain important information from the original functions, that's neat!

## Higher level
The `memoize` decorator doesn't need any customization, but there are a lot of pattern that requires some kind of customization. For instance, we want to apply a retry pattern to a function that follows special protocol. Obviously, we have to specify the number of retries, the delay between retry, and maybe a backoff factor to scale up the delay between failed attempts. This is how we do it:


```python
    import time, math

    def retry(tries, delay=3, backoff=2):
        '''Retries a function or method until it returns True.
        delay sets the initial delay in seconds, and backoff sets the factor by which
        the delay should lengthen after each failure. backoff must be greater than 1,
        or else it isn't really a backoff. tries must be at least 0, and delay
        greater than 0.'''

        if backoff <= 1:
            raise ValueError("backoff must be greater than 1")

        if tries < 0:
            raise ValueError("tries must be 0 or greater")

        if delay <= 0:
            raise ValueError("delay must be greater than 0")

        def deco_retry(f):
            def f_retry(*args, **kwargs):
                mtries, mdelay = tries, delay

                rv = f(*args, **kwargs)
                while mtries > 0:
                    if rv is True:
                        return True

                    mtries -= 1
                    time.sleep(mdelay)
                    mdelay *= backoff

                    rv = f(*args, **kwargs)

                return False
            return f_retry
        return deco_retry

    @retry(1, delay=1, backoff=2)
    def get_data():
        return False
```

Here, we define `retry` as a function that returns a `decorator` which will do the actual decoration of our original function with the parameters provided by `retry`. We consider that `retry(1, delay=1, backoff=2)` is called first, returning a function, then the decorator syntax `@` is applied. This is just an addition of another layer on the decoration stack. In theory, you can have unlimited number of nested layer, but in practice, most of the time you only use 2.

## Decorator class
Using function as decorators is straight forward, and for storing persistent information we use closures over temporary variables. It'd be nice if the persistent information are class members.

```python
    import collections
    class memoized(object):
        '''Decorator. Caches a function's return value each time it is called.
        If called later with the same arguments, the cached value is returned
        (not reevaluated).
        '''
        def __init__(self, func):
            self.func = func
            self.__doc__ = func.__doc__
            self.cache = {}
        def __call__(self, *args, **kwargs):
            if not isinstance(args, collections.Hashable):
                # uncacheable. a list, for instance.
                # better to not cache than blow up.
                return self.func(*args, **kwargs)
            if args in self.cache:
                return self.cache[args]
            else:
                value = self.func(*args, **kwargs)
                self.cache[args] = value
                return value
        def __repr__(self):
            '''Return the function's docstring.'''
            return self.func.__doc__
        def __get__(self, obj, objtype):
            '''Support instance methods.'''
            return functools.partial(self.__call__, obj)
```

Here, the decorator is an object of class `memoized` and you can store all sort of information like you would a normal object.

## Class decorator
Up to now we're working with function decorator, what if we want to operate at class level? It's actually quite simple, we only have to define a function that takes a class instead of a function as the parameter.

Let's have a look at [functool.total_ordering](https://hg.python.org/cpython/file/8e838598eed1/Lib/functools.py). This decorator makes it so that you only have to define one of the four functions `__lt__`, `__le__`, `__gt__`, `__ge__`, and the other three will be defined based on the provided function.

```python
    def total_ordering(cls):
        """Class decorator that fills in missing ordering methods"""
        convert = {
            '__lt__': [('__gt__', lambda self, other: not (self < other or self == other)),
                    ('__le__', lambda self, other: self < other or self == other),
                    ('__ge__', lambda self, other: not self < other)],
            '__le__': [('__ge__', lambda self, other: not self <= other or self == other),
                    ('__lt__', lambda self, other: self <= other and not self == other),
                    ('__gt__', lambda self, other: not self <= other)],
            '__gt__': [('__lt__', lambda self, other: not (self > other or self == other)),
                    ('__ge__', lambda self, other: self > other or self == other),
                    ('__le__', lambda self, other: not self > other)],
            '__ge__': [('__le__', lambda self, other: (not self >= other) or self == other),
                    ('__gt__', lambda self, other: self >= other and not self == other),
                    ('__lt__', lambda self, other: not self >= other)]
        }
        # Find user-defined comparisons (not those inherited from object).
        roots = [op for op in convert if getattr(cls, op, None) is not getattr(object, op, None)]
        if not roots:
            raise ValueError('must define at least one ordering operation: < > <= >=')
        root = max(roots)       # prefer __lt__ to __le__ to __gt__ to __ge__
        for opname, opfunc in convert[root]:
            if opname not in roots:
                opfunc.__name__ = opname
                opfunc.__doc__ = getattr(int, opname).__doc__
                setattr(cls, opname, opfunc)
        return cls
```

This code is pretty simple. It defines 3 other operators based on 2 operators: `__eq__` and one of the four functions `__lt__`, `__le__`, `__gt__`, `__ge__`.


## Useful decorators
* property - used to quickly create a field from appropriate getter, setter and deleter.


# REFERENCES
[Python Decorator Library][python_decorator]

[python_decorator]: https://wiki.python.org/moin/PythonDecoratorLibrary  "Python Decorator Library"
