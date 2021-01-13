def fib(n):
    """ original function"""

    if n == 0 or n == 1:
        return 1

    # else
    result = fib(n-1) + fib(n-2)
    return result


"""why does it works? the dict d is actually common to all f calls.
It's a lesser known python quirk that often causes issue, but here it's
very useful & powerful, as any subsequent call to f will also
benefit from the memoization"""


def fib_memo(n, d=dict()):
    # check if value memoized
    if n in d:
        return d[n]

    # else, compute the value
    if n == 0 or n == 1:
        return 1
    result = fib_memo(n-1) + fib_memo(n-2)

    d[n] = result
    return result


print("memoized call:")
print("fib_memo(35) = ", fib_memo(35))
print("non memoized(notice how it's much longer):")
print("fib(35) = ", fib(35))
