import os
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element_by_css_selector("[name='firstname']")
    first_name.send_keys("firstName")
    last_name = browser.find_element_by_css_selector("[name='lastname']")
    last_name.send_keys("secondName")
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("Email")
    file_button = browser.find_element_by_id("file")
    file_name = 'example'
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)
    file_button.send_keys(file_path)
    button_submit = browser.find_element_by_tag_name("button[type='submit']")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
