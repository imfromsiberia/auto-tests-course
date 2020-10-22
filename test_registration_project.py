from selenium import webdriver
import time
import unittest


class TestReg(unittest.TestCase):

    def test_reg1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(
            '[placeholder="Input your first name"]').send_keys('Sashok')
        input2 = browser.find_element_by_css_selector(
            '[placeholder="Input your last name"]').send_keys('Furs')
        input3 = browser.find_element_by_css_selector(
            '[placeholder="Input your email"]').send_keys('Sashok@Furs')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        time.sleep(10)
        browser.quit()
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text)

    def test_reg2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(
            '[placeholder="Input your first name"]').send_keys('Sashok')
        input2 = browser.find_element_by_css_selector(
            '[placeholder="Input your last name"]').send_keys('Furs')
        input3 = browser.find_element_by_css_selector(
            '[placeholder="Input your email"]').send_keys('Sashok@Furs')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        time.sleep(10)
        browser.quit()
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
