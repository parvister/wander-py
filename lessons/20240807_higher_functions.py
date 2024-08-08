"""
high order functions
"""

def add(x):
    """A function that returns another function. Each function takes another argument"""
    def adder(y):
        return x + y
    return adder

add_15 = add(15)
print(f"adding 25: {add_15(25)}")
