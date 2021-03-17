import time
from clockdeco0 import clock

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__ == '__main__':
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))