from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    input1 = browser.find_element(By.CSS_SELECTOR, "body > div.container > form > div > input:nth-child(2)").send_keys("first name")

    input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[2]").send_keys("last name")

    input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div/input[3]").send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)


    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(10)
    browser.quit()