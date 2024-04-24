from pages.heroku_app import HerokuApp
from selenium.webdriver.common.by import By


class AddRemovePage(HerokuApp):
    def __init__(self, browser_instance=None):
        self.__locators = {
            'add_element': {By.XPATH, '/html/body/div[2]/div/div/button'},
            'added_element': {By.CLASS_NAME, 'added-manually'},
            'heading': {By.TAG_NAME, "h3"}
        }
        super().__init__(browser_instance)

    def add_element(self):
        self._browser.find_element(*self.__locators['add_element']).click()

    def get_added_elements(self):
        return [elem.text for elem in self._browser.find_elements(*self.__locators['added_element'])]

