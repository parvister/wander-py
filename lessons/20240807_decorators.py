"""
Using decorators in ML and data engineering.
"""

def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("decorator: before calling the function")
        func(*args, **kwargs)
        print("decorator: after calling the function")
    # return the wrapper
    return wrapper

@simple_decorator
def print_msg(msg):
    print(msg)

print_msg("hello decorators!")


"""
more advanced decorator example
"""

def repeat(n: int = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for x in range(n):
                print(f"call #{(x + 1):02}")
                result = func(*args, **kwargs)
            return result
        # return
        return wrapper
    return decorator


@repeat(5)
def say_hi(name):
    print(f"hi {name}")

say_hi('Alice')


"""
another example of performance timer decorator
"""

import time

def perf_timer(print_time: bool = True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"func time: {(end_time - start_time):.3f}") if print_time else None
            return result
        return wrapper
    return decorator

@perf_timer()
def sleep_for_a_while(sleep_time: int):
    time.sleep(sleep_time)

sleep_for_a_while(3)
