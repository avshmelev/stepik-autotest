import math
import time
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = browser.find_element_by_id("input_value").text
    result = calc(x_value)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()
    button_submit = browser.find_element_by_css_selector("button[type='submit']")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
