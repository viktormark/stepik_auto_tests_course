from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)
print(x)

browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.ID, "robotCheckbox").click()

browser.find_element(By.ID, "robotsRule").click()

browser.find_element(By.XPATH, "//button[text()='Submit']").click()