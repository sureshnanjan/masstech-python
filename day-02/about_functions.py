"""
[decorators] "def" funcname "(" [parameter_list] ")" ["->" expression] ":" suite
"""
print(dir())


def simple_decorator():
    pass


def decorator_with_args(arg1):
    pass

#Callable  Functions - methods
def basic_function():
    # "def" funcname "(" ")"
    print("Hello Friends")




def basic_function_with_args(argument1):
    # "def" funcname "(" [parameter_list] ")"
    argument1()


# Bad Code (Not Pythonic Code)
def addNumber(a, b):
    return a + b


# Pythonic Code
def add_number(a, b):
    return a + b


#@simple_decorator
def decorated_function():
    pass


#basic_function_with_args(basic_function)
#print(len("Suresh"))
#basic_function_with_args(100)
#print(len(100))
decorator_with_args()