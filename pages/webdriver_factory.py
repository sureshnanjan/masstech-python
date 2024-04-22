from utilities.browser_utilities import BrowserUtil
import selenium.webdriver as wd


class WebdriverFactory:
    @staticmethod
    def get_browser():
        match BrowserUtil.get_browser():
            case "firefox":
                return wd.Firefox()
            case "chrome":
                return wd.Chrome()
            case _:
                return wd.Chrome()
    @staticmethod
    def get_element_from_selector(self, driver, selector:tuple):
        driver.get_element(selector[0],selector[1])

