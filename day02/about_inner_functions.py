def top_level_function():
    """
    the inner functions aren’t defined until the parent function is called.
    They’re locally scoped to parent(), meaning they only exist inside the parent() function
    as local variables.
    :return:
    """
    print("Printing from parent()")

    def inner_func1():
        print("Printing from inner_func1()")

    def inner_func2():
        print("Printing from inner_func2()")

    inner_func2()
    inner_func1()


def function_returning_function(num):
    def first_child():
        return "Hi, I'm First"

    def second_child():
        return "Call me Second"

    if num == 1:
        return first_child
    else:
        return second_child

get_one = function_returning_function(1)
get_two = function_returning_function(2)