from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first").send_keys("first name")

    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("last name")

    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("email")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(1)


    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text


    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)
    browser.quit()


