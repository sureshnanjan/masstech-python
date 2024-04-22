"""Heroku Web app Demo features feature tests."""
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

home_page = None

@scenario('heroku_app.feature', 'Home Page heading is matching')
def test_home_page_heading_is_matching():
    """Home Page heading is matching."""


@given('I Have Heroku app opened')
def _():
    """I Have Heroku app opened."""
    print("Opened Heroku app")

@when('I check the main heading')
def _():
    """I check the main heading."""
    print("Checking Main Heading")

@then('it should match "Welcome to the-internet"')
def _():
    """it should match "Welcome to the-internet"."""
    print("Matching the Title")
