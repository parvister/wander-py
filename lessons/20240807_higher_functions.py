
def add(x):
    def adder(y):
        return x + y
    return adder

add_15 = add(15)
print(f"adding 25: {add_15(25)}")
