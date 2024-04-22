from pages.heroku_app import HerokuApp
from selenium.webdriver.common.by import By


class HomePage(HerokuApp):
    def __init__(self, browser_instance=None):
        self.__locators = {
            'heading': ("", "#username input"),
            'subheading': ('CSS', '#password input'),
            'example': ('ID', 'login-btn')
        }
        super().__init__(browser_instance)

    def get_heading(self):
        return self._browser.find_element(By.TAG_NAME, "h1").text

    def get_sub_heading(self):
        return self._browser.find_element(By.TAG_NAME, "h2").text
