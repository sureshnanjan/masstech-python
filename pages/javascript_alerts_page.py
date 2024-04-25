from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions

from pages.heroku_app import HerokuApp


class JavaScriptAlertsPage(HerokuApp):
    def __init__(self, browser_instance):
        self.__locators = {
            'heading': (By.TAG_NAME, "h3"),
            'description':(By.TAG_NAME, "p"),
            'invoke_jsalert':(By.XPATH, ""),
            'invoke_jsprompt':(),
            'invoke_jsconfirm':(),
            'page_result':()
        }
        self.__page_alert= None
        super().__init__(browser_instance)

    def invoke_simple_alert(self):
        self._browser.find_element(*self.__locators['invoke_jsalert']).click()

    def invoke_confirm_alert(self):
        self._browser.find_element(*self.__locators['invoke_jsconfirm']).click()

    def invoke_prompt_alert(self):
        self._browser.find_element(*self.__locators['invoke_jsprompt']).click()

    def get_message(self):
        wait.until(expected_conditions.alert_is_present())
        self.__page_alert = Alert(self._browser)

    def accept_message(self):
        self.__page_alert.accept()

    def dismiss_message(self):
        self.__page_alert.dimiss()

    def input_text_in_prompt(self, input_text):
        self.__page_alert.send_keys(input_text)

    def get_result(self):
        pass

