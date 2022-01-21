import math
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

browser = webdriver.Chrome(ChromeDriverManager().install())

# first_window = browser.window_handles[0]
# new_window = browser.window_handles[1]
# browser.switch_to.window(window_name)
# current_window = browser.current_window_handle

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
    button1.click()

    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    num = calc(x)
    otvet = browser.find_element(By.ID, 'answer')
    otvet.send_keys(num)

    button2 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button2.click()

    time.sleep(10)

finally:
    browser.quit()

