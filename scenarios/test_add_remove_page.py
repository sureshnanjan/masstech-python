from pages.home_page import HomePage
from pages.heroku_app import HerokuApp
from pages.add_remove_page import AddRemovePage


def test_adding_elements_work():
    aut = HomePage()
    aut.go_to_homepage()
    add_rem = aut.go_to_example("addremove")
    expected_count = 1
    add_rem.add_element()
    actual_count = len(add_rem.get_added_elements())
    assert actual_count == expected_count, "Adding elements is not correct"
