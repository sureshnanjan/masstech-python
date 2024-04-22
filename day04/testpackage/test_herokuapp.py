import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self):
        self.title = "TEst Titke"

    def get_title(self):
        pass

    def get_sub_title(self):
        pass

    def get_available_examples(self):
        pass

    def go_to_example(self, example_name):
        pass


@pytest.mark.skip
def test_heroku_title_is_correct():
    page = HomePage()
    expected = "Welcome To Internet"
    actual = page.get_title();
    assert actual == expected

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title
    elem = driver.find_element(By.TAG_NAME, "h1")
    actual_heading = elem.text
    assert "Welcome to the-internetNOT" == actual_heading
    driver.close()


def test_page_subheading():
    page = HomePage()
    expected = "Available Examples"
    actual = page.get_sub_title();
    assert actual == expected


def test_navigating_to_abtestpage():
    page = HomePage()
    expected = "A/B Test Variation 1"
    page.go_to_example("ABtestpage")
    actual = page.get_title();
    assert actual == expected
