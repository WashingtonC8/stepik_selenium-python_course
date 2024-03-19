from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x, y):
    return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    a = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    b = y_element.text
    c = calc(a, b)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()



