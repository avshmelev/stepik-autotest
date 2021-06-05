import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    number1 = browser.find_element_by_id("num1").text
    number2 = browser.find_element_by_id("num2").text
    result = int(number1) + int(number2)
    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_value(str(result))
    button_submit = browser.find_element_by_css_selector("button[type='submit']")
    button_submit.click()
finally:
    time.sleep(10)
    browser.quit()
