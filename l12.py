import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import os

browser = webdriver.Chrome(ChromeDriverManager().install())

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    field1 = browser.find_element(By.NAME, 'firstname')
    field1.send_keys('text')
    field2 = browser.find_element(By.NAME, 'lastname')
    field2.send_keys('text')
    field3 = browser.find_element(By.NAME, 'email')
    field3.send_keys('text')
    time.sleep(1)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    button1 = browser.find_element(By.ID, 'file')
    button1.send_keys(file_path)

    button2 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button2.click()
    time.sleep(10)

finally:
    browser.quit()
