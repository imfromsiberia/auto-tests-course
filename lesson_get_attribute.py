from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    image = browser.find_element_by_tag_name('img')
    image_valuex = image.get_attribute('valuex')
    y = calc(image_valuex)
    textform = browser.find_element_by_id("answer").send_keys(y)
    checkbox = browser.find_element_by_css_selector("[type='checkbox']")
    checkbox.click()
    radiobtn = browser.find_element_by_id("robotsRule")
    radiobtn.click()
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()




finally:
    time.sleep(30)
    browser.quit()

