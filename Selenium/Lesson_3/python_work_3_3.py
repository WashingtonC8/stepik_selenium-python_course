from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

with open("test.txt", "w") as file:
    content = file.write("automationbypython")  # create test.txt file

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Test")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Testov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@test.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
