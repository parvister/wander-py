"""
iterators and generators
"""

# iterator example

class CounterIterator:
    def __init__(self, initValue: int = 1, stopValue: int = 10) -> None:
        self.count = initValue
        self.end = stopValue

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.end:
            raise StopIteration
        else:
            self.count = self.count + 1
            return self.count - 1


c1 = CounterIterator(100, 115)
for x in c1:
    print(x)


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count = count + 1

up10 = count_up_to(10)
for x in up10:
    print(x)

import math

# generators with ()
power_of_trees = (math.floor(math.pow(x, 3)) for x in range(5))
for x in power_of_trees:
    print(f"power of 3: {x}")


"""
efficient pipelines
"""

def generate_numbers(max):
    for i in range(max):
        yield i

def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

def square(numbers):
    for num in numbers:
        yield num * num

pipeline = square(filter_even(generate_numbers(10)))

for result in pipeline:
    print(f"pipeline: {result}")


sonnet = """For thy sweet love remembered such wealth brings
That then I scorn to change my state with kings.
When to the sessions of sweet silent thought
I summon up remembrance of things past,
I sigh the lack of many a thing I sought,"""

import re

def process_sonnet(sonnet: str):
    pattern = r"([\w ])+[\n.,]"
    r = re.compile(pattern)
    for chunk in r.finditer(sonnet):
        yield chunk.group().strip()

for chunk in process_sonnet(sonnet):
    print(f"sonnet chunk: {chunk}")

