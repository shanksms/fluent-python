import time
'''
Remember that this code:
@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
Actually does this:
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
factorial = clock(factorial)

'''
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked

