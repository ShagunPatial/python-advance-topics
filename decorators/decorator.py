import time
import math
"""
Decorators:
Decorators allow us to wrap another function in order to extend 
the behaviour of the wrapped function, without permanently modifying it.
link : https://www.geeksforgeeks.org/decorators-in-python/
"""
"""
First Class Objects:
functions are first class objects which means that functions in Python can be 
used or passed as arguments.

Properties of first class functions:
A function is an instance of the Object type.
-You can store the function in a variable.
-You can pass the function as a parameter to another function.
-You can return the function from a function.
-You can store them in data structures such as hash tables, lists
"""

# Returning functions from another function


def create_adder(x):
    def adder(y):
        return x+y

    return adder


add_1244 = create_adder(1244)

print(add_1244(10))

# decorator to calculate duration
# taken by any function.

print("\nCalculate time taken by function:")


def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        func(*args, **kwargs)      
        # storing time after function execution
        end = time.time()
        time_taken = end - begin
        print(f"Total time taken in exec {func.__name__}: {time_taken} sec")

    return inner1

# this can be added to any function present,
# in this case to calculate a factorial


@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(0.5)
    print(math.factorial(num))

# calling the function.
factorial(10)

"""
Chaining Decorators:
decorating a function with multiple decorators:

"""
# code for testing decorator chaining
print("\nCHAINING DECORATOR: ")


def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10


print(num())
print(num2())
