import math
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

browser = webdriver.Chrome(ChromeDriverManager().install())


# alert = browser.switch_to.alert
# alert_text = alert.text
# alert.accept()

# confirm = browser.switch_to.alert
# confirm.accept()
# confirm.dismiss()

# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()

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
