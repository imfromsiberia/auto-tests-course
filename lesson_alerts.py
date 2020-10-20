from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element_by_css_selector("[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    number = browser.find_element_by_id('input_value')
    func = number.text
    y = calc(func)
    textform = browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()



finally:
    time.sleep(30)
    browser.quit()