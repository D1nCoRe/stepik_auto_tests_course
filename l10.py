import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

browser = webdriver.Chrome(ChromeDriverManager().install())

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)
    a_el = browser.find_element(By.ID, 'num1')
    a = a_el.text
    b_el = browser.find_element(By.ID, 'num2')
    b = b_el.text
    c = int(a) + int(b)
    c = str(c)

    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{c}']").click()
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()
    time.sleep(10)

finally:
    browser.quit()
