import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.implicitly_wait(10)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button2 = browser.find_element(By.ID, 'book')
    button2.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    num = calc(x)
    otvet = browser.find_element(By.ID, 'answer')
    otvet.send_keys(num)
    button3 = browser.find_element(By.ID, 'solve')
    button3.click()

    time.sleep(10)

finally:
    browser.quit()
