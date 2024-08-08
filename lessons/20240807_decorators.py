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
