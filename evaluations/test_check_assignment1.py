from day01.assignments.string_operations import make_list_from_string


def test_assignment_day01():
    # TDD
    name = "hello"

    assert [*name] == make_list_from_string("hello")
