#!env python
#coding=utf-8
# Author:  joshua_zero@outlook.com

import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        f = func(*args)
        elpased = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[{:0.8f}] {}({})->{}'.format(elpased, name, arg_str, f))
        return f
    return clocked


@clock 
def snooze(seconds):
    time.sleep(seconds)

@clock 
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)



#test demo 2

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock_m2(fmt=DEFAULT_FMT):
    def decorate(func): 
        def clocked(*_args): 
            t0 = time.time() 
            _result = func(*_args) 
            elapsed = time.time() - t0 
            name = func.__name__ 
            args = ', '.join(repr(arg) for arg in _args) 
            result = repr(_result) 
            print(fmt.format(**locals())) 
            return _result 
        return clocked 
    return decorate


if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123)') 
    snooze(.123) 
    print('*' * 40, 'Calling factorial(6)') 
    print('6! =', factorial(6))
    
    print("########***demo2***########")
    @clock_m2() 
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(.123)
