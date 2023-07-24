from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
print(y)

browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.ID, "robotCheckbox").click()

browser.find_element(By.ID, "robotsRule").click()

browser.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(5)



