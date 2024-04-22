import selenium.webdriver as wd
import selenium.types as wd_types
from utilities.browser_utilities import BrowserUtil
from utilities.app_utilities import ApplicationUtil
from pages.webdriver_factory import WebdriverFactory


class HerokuApp:
    def __init__(self, browser_page=None):
        self._url = ApplicationUtil.get_app_url()
        #self._testpage = wd.Chrome()
        if not browser_page:
            self._browser = WebdriverFactory.get_browser()
        else:
            self._browser = browser_page

    def go_to_homepage(self):
        self._browser.get(self._url)
        #self._testpa

    def close_browser(self):
        try:
            self._browser.close()
        except Exception:
            pass

    def take_screenshot(self):
        self._browser.take_screenshot()

    def _get_element_from_selector(self,selector):
        pass

