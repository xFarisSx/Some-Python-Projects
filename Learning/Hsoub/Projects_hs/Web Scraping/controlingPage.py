from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_Page')

try:
    # elem = browser.find_element(By.CSS_SELECTOR, '#ca-viewsource > a > span')
    # elem.click()
    # time.sleep(5)

    elem = browser.find_element(By.CSS_SELECTOR, '#searchInput')
    elem.send_keys('python')
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, "#searchButton")
    button.click()
    time.sleep(5)

    time.sleep(3)
    htmlElem = browser.find_element(By.TAG_NAME, 'html')
    htmlElem.send_keys(Keys.END)
    time.sleep(3)
    htmlElem.send_keys(Keys.HOME)
    time.sleep(3)

except:
    print('error')