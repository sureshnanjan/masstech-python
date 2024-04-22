"""
Decorator is a way to dynamically add some new behavior to some objects.
We achieve the same in Python by using closures.
"""


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result

    return wrapper


@my_decorator
def my_function(input1, input2):
    print("Processing: " + str(input1))
    print("Processing: " + str(input2))


# call without decorating

my_function(10, 20)

# call after decorating
"""
result = my_function(10,20)
if int(result) > 10:
    print("pass")
"""
