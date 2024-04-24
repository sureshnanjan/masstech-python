from pages.home_page import HomePage


def test_home_page_title():
    aut = HomePage()
    aut.go_to_homepage()
    assert aut.get_heading() == "Welcome to the-internet"


def test_home_page_subtitle():
    aut = HomePage()
    aut.go_to_homepage()
    assert aut.get_sub_heading() == "Available Examples"


def test_home_page_has_all_examples():
    aut = HomePage()
    aut.go_to_homepage()
    expected_count = 44
    actual_count = len(aut.get_available_examples())
    assert actual_count == expected_count, "The available examples does not match"
