import math
import time
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = browser.find_element_by_id("input_value").text
    result = calc(int(x_value))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button_submit = browser.find_element_by_tag_name("button[type='submit']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
