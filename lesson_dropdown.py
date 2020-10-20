from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def f(x):
    return

link = "http://suninjuly.github.io/selects2.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id('num1')
    x = num1.text
    num2 = browser.find_element_by_id('num2')
    y = num2.text
    z = str(int(x) + int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z).click()
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
