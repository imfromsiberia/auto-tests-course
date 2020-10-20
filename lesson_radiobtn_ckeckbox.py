from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:


    browser = webdriver.Chrome()
    browser.get(link)  
    number = browser.find_element_by_id("input_value")
    x = number.text
    z = calc(x)
    textform = browser.find_element_by_id("answer").send_keys(z)
    checkbox = browser.find_element_by_css_selector("[type='checkbox']")
    checkbox.click()
    radiobtn = browser.find_element_by_id("robotsRule")
    radiobtn.click()
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
