"""
This example demonstrated cookies management with webdriver
"""
from pages.heroku_app import HerokuApp
from selenium.webdriver.common.by import By


class ABTestingPage(HerokuApp):
    def __init__(self, browser_instance=None):
        self.__locators = {'heading': (By.TAG_NAME, 'h3'),
                           'description_text': (By.TAG_NAME, 'p')}

        super().__init__(browser_instance)

    def disable_abtesting(self):
        #self._browser.add_cookie({"cookie":{"optimizelyOptOut":"true"}})
        self._browser.add_cookie({"name": "optimizelyOptOut", "value": "true"})

    def get_heading(self):
        return self._browser.find_element(*self.__locators['heading']).text


