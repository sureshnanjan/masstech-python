"""
This is not a valid test method by default
"""


def does_not_startwittest():
    assert ((1 + 2) == 3), "name<whatever>test pattern not recognised - Passes"


"""
This is not a valid test method by default
"""


def ends_with_test():
    assert ((1 + 2) == 3), "name_test pattern will not be recognised"

"""
Test methods should start with test_
"""
def test_simple_pass_file_starts():
    assert ((1 + 2) == 3), "test_name pattern recognised - Passes"


def test_simple_fail_file_starts():
    assert ((1 + 2) == 5), "test_name pattern recognises - Fails"
