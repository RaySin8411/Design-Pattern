import math
from timing import waste_some_time
from debugging import debug, make_greeting
from slowing_down import countdown
from registering_plugins import PLUGINS, randomly_greet

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


if __name__ == '__main__':
    waste_some_time(1)
    waste_some_time(999)
    make_greeting("Benjamin")
    make_greeting("Richard", age=112)
    make_greeting(name="Dorrisile", age=116)
    approximate_e(5)
    countdown(3)
    print(PLUGINS)
    randomly_greet("Alice")
