from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser , 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element_by_id('book').click()
    number = browser.find_element_by_id('input_value')
    func = number.text
    y = calc(func)
    textform = browser.find_element_by_id("answer").send_keys(y)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()


finally:
    time.sleep(60)
    browser.quit()
    