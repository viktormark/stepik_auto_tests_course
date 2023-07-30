from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']").click()

    alert = browser.switch_to.alert
    alert.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(19)
    browser.quit()






