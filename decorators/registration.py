'''
A key feature of decorators is that they run right after the decorated function is defined.
That is usually at import time (i.e., when a module is loaded by Python). Consider registration.py in Example 9-2.

'''
registry = []

def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func
@register
def f1():
    print('running f1()')
@register
def f2():
    print('running f2()')
def f3():
    print('running f3()')

def main():
    print('running main()')
    print('print registry -> ', registry)
    f1()
    f2()
    f3()
if __name__ == '__main__':
    main()
