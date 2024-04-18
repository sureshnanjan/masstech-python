def this_is_valid_test():
    assert ((1 + 2) == 3), "This pattern in test name <whatever_>test pattern"


def test_simple_pass_file_starts():
    assert ((1 + 2) == 3), "This is a Passing test that starts with test_ pattern"


def test_simple_fail_file_starts():
    assert ((1 + 2) == 5), "This is a Failing test that starts with test_ pattern"
