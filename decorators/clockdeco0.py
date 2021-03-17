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
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f'{k}={repr(v)}' for k, v in kwargs.items()]
            arg_lst.append(', '.join(pairs))

        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {repr(result)}')
        return result
    return clocked

