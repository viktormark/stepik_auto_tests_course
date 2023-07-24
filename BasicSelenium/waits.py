from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# link = ""
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#
#     browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']").click()
#
#     new_window = browser.window_handles[1]
#
#     browser.switch_to.window(new_window)
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#     browser.find_element(By.ID, "answer").send_keys(y)
#
#     browser.find_element(By.XPATH, "//button[text()='Submit']").click()
#
# finally:
#     time.sleep(19)
#     browser.quit()

#---------

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:



    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    browser.find_element(By.ID, "book").click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(20)
    browser.quit()