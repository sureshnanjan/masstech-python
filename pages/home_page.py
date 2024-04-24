from pages.heroku_app import HerokuApp
from pages.add_remove_page import AddRemovePage
from selenium.webdriver.common.by import By


class HomePage(HerokuApp):
    def __init__(self, browser_instance=None):
        self.__locators = {
            'heading': (By.TAG_NAME, "h1"),
            'subheading': (By.TAG_NAME, "h2"),
            'example': (By.TAG_NAME, 'li')

        }
        super().__init__(browser_instance)

    def get_heading(self):
        #self._browser.find_element(by=self.__locators['heading'][0],value=self.__locators['heading'][1]).text
        return self._browser.find_element(*self.__locators['heading']).text


    def get_sub_heading(self):
        return self._browser.find_element(By.TAG_NAME, "h2").text

    def get_available_examples(self):
        collection = self._browser.find_elements(*self.__locators['example'])
        # list comprehension
        return [elem.text for elem in collection]


    def go_to_example(self, name:str):
        match name.lower():
            case "addremove":
                return AddRemovePage(self._browser)
            case _:
                return self

