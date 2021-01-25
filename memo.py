import functools

# 0: Naive, non-memoized


def fib(n):
    """ original function"""

    if n < 2:
        return n

    # else
    result = fib(n-1) + fib(n-2)
    return result


# 1: Simple memoization of 1 function
"""why does it works? the dict d is actually common to all f calls.
It's a lesser known python quirk that often causes issue, but here it's
very useful & powerful, as any subsequent call to f will also
benefit from the memoization"""


def fib_memo(n, d=dict()):
    # check if argument (or tuple of arguments) memoized
    if n in d:
        return d[n]

    # else, compute the value
    if n < 2:
        return n
    result = fib_memo(n-1) + fib_memo(n-2)

    d[n] = result
    return result


# 2: Another simple solution, but needs an import (functools)
@functools.lru_cache(maxsize=None)
def fib_memo2(n):
    """ original function"""

    if n < 2:
        return n

    # else
    result = fib_memo2(n-1) + fib_memo2(n-2)
    return result


# 3: More complex, but cleaner, especially if you need to memoize multiple functions
def memoize(function):
    from functools import wraps

    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


@memoize
def fib_memo3(n):
    if n < 2:
        return n
    return fib_memo3(n - 1) + fib_memo3(n - 2)


# 3 bis : if you don't have access to source code
# but WILL have trouble with recursive (to non-memoized function)
# calls if you change its name to re define the function

fib_memo4 = memoize(fib)  # doesn't work


def fib_memo4(n):
    if n < 2:
        return n
    return fib_memo4(n - 1) + fib_memo4(n - 2)


fib_memo4 = memoize(fib_memo4)

print("memoized calls:")
print("fib_memo(35) = ", fib_memo(35))
print("fib_memo2(35) = ", fib_memo2(35))
print("fib_memo3(35) = ", fib_memo3(35))
print("fib_memo4(35) = ", fib_memo4(35))
print("non memoized(notice how it's much longer):")
print("fib(35) = ", fib(35))
