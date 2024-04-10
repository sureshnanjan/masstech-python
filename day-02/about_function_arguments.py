"""
default arguments
keyword arguments
positional arguments
arbitrary positional arguments
arbitrary keyword arguments
"""


def default_arguments_add(a=6, b=5, c=10):
    """
    Default values are evaluated only once at the point of the function definition
    in the defining scope. So, it makes a difference when we pass mutable objects like
    a list or dictionary as default values.
    :param a:
    :param b:
    :param c:
    :return:
    """
    return a + b + c

#Calling the function default_arguments_add by giving keyword arguments


# Variable-length arguments are also known as arbitrary arguments. If we don’t know
# the number of arguments needed for
# the function in advance, we can use arbitrary arguments

def arbitraty_positional_add(a,b,*arg):
    result = 0
    for item in arg:
        result = result + item
    return result

def arbitraty_keyword_add(**arg):
    for item in arg.items():
        print (item)

#arbitraty_positional_add(numbers=5,colors="blue",fruits="apple")

def positional_only(a,/,b,c,d):
    return a+b+c+d

def keyword_only(a,b,*,c,d):
    return a+b+c+d


#print(default_arguments_add())
#print(default_arguments_add(1))
#print(default_arguments_add(1,2))
#print(default_arguments_add(1,2,3))
#print(default_arguments_add(1,2,3,4))
#print(arbitraty_positional_add(1))
#print(arbitraty_positional_add(1,2))
#print(arbitraty_positional_add(1,2,3,4,5,6,7,8,9,10))
#print(arbitraty_positional_add())
#arbitraty_keyword_add(a=1,b=2,c=3,d=10)
#positional_only(1,2,3,4)
#positional_only(1,2,c=3,d=4)
#keyword_only(1,2,3,4)






