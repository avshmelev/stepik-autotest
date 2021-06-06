from selenium import webdriver
import time
import unittest


class RegistrationTestCase(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_css_selector(".first_block input.first")
        first_name.send_keys("First name")
        second_name = browser.find_element_by_css_selector(".first_block input.second")
        second_name.send_keys("Second name")
        email = browser.find_element_by_css_selector(".first_block input.third")
        email.send_keys("Email")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "expected welcome text not equals actual")
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_css_selector(".first_block input.first")
        first_name.send_keys("First name")
        second_name = browser.find_element_by_css_selector(".first_block input.second")
        second_name.send_keys("Second name")
        email = browser.find_element_by_css_selector(".first_block input.third")
        email.send_keys("Email")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "expected welcome text not equals actual")
        browser.quit()


if __name__ == '__main__':
    unittest.main()
