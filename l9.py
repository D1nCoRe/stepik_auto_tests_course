import math
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    x_el = browser.find_element(By.ID, 'treasure')
    x = x_el.get_attribute('valuex')
    num = calc(x)
    qwer = browser.find_element(By.ID, 'answer')
    qwer.send_keys(num)

    button1 = browser.find_element(By.ID, 'robotCheckbox')
    button1.click()

    button2 = browser.find_element(By.ID, 'robotsRule')
    button2.click()

    button3 = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button3.click()

    time.sleep(10)

finally:
    browser.quit()
