from pages.home_page import HomePage


def test_home_page_title():
    aut = HomePage()
    aut.go_to_homepage()
    assert aut.get_heading() == "Welcome to the-internet"


def test_home_page_subtitle():
    aut = HomePage()
    aut.go_to_homepage()
    assert aut.get_sub_heading() == "Available Examples"
