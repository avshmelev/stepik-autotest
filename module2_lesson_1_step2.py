import math
import time
from selenium import webdriver


#  --------   Пример работы с get_attribute    ------------

link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # Если атрибута нет, то метод get_attribute вернёт значение None. Применим метод get_attribute ко
    # второму radiobutton, и убедимся, что атрибут отсутствует.
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    # Так же мы можем проверять наличие атрибута disabled, который определяет, может ли пользователь
    # взаимодействовать с элементом. Например, в предыдущем задании на странице с капчей для роботов
    # JavaScript устанавливает атрибут disabled у кнопки Submit, когда истекает время, отведенное на решение задачи.
    # <button type = "submit" class ="btn btn-default" disabled> Submit </button>
finally:
    time.sleep(10)
    browser.quit()
