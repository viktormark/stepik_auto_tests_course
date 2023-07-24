from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    n1 = browser.find_element(By.ID, "num1")
    x1 = n1.text

    n2 = browser.find_element(By.ID, "num2")
    x2 = n2.text

    x = int(x1) + int(x2)

    select = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
    select.select_by_value(str(x))


    b = browser.find_element(By.XPATH, "//button[text()='Submit']")
    b.click()
finally:
    time.sleep(10)
    browser.quit()

#---------


#------------

