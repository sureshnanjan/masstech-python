from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from  selenium.webdriver.chrome.options import Options as copt
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
"""
#content > h1 - CSS
//*[@id="content"]/h1 -XPATH
browser = selenium.webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/")
print(browser.title)
#browser.quit()

DesiredCapabilities.FIREFOX
browser = WebDriver("http://localhost:7070",DesiredCapabilities.FIREFOX)
browser.get("https://the-internet.herokuapp.com/")
print(browser.title)
//*[@id="content"]/h1
"""

options = Options() # ff options
choptions = copt() # chrome options
driver = WebDriver(command_executor="http://localhost:6060", options=choptions)
driver.get("https://the-internet.herokuapp.com/")
print(driver.title)
actual_title = driver.find_element(By.TAG_NAME,"h1").text
print(actual_title)
assert actual_title == "Matched Title"
driver.add_cookie({"optimizelyOptOut":"true"})
driver.quit()

