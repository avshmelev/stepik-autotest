import math
import os
import time
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x_value = browser.find_element_by_id("input_value").text
    result = calc(int(x_value))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    button_submit = browser.find_element_by_tag_name("button[type='submit']")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
