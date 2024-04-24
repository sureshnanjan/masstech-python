"""Heroku Web app Demo features feature tests."""
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from pages.home_page import HomePage

home_page = None
page_heading = None

@scenario('heroku_app.feature', 'Home Page heading is matching')
def test_home_page_heading_is_matching():
    """Home Page heading is matching."""


@given('I Have Heroku app opened')
def _():
    """I Have Heroku app opened."""
    print("Opened Heroku app")
    global home_page
    home_page = HomePage()
    home_page.go_to_homepage()

@when('I check the main heading')
def _():
    """I check the main heading."""
    print("Checking Main Heading")
    global home_page
    global page_heading
    page_heading = home_page.get_heading()

@then('it should match "Welcome to the-internet"')
def _():
    """it should match "Welcome to the-internet"."""
    print("Matching the Title")
    global page_heading
    assert page_heading == "Welcome to the-internet", "The Heading does not match"
