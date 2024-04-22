"""
This assignment is a knowledge check to use string operations
"""
import pytest


#@pytest.mark.prametrize("arg1", ["Tester"])
def make_list_from_string(arg1):
    """This method breaks the input string and returns a list with its characters"""
    val_list = []
    for char in arg1:
        val_list.append(char)
    print(val_list)
    assert val_list == ['D', 'e', 'e', 'p', 'a', 'n']  # Example assertion to ensure correctness

print(make_list_from_string("Deepan"))