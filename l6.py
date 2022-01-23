from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

link = "http://suninjuly.github.io/registration1.html"

try:
    browser.get(link)

    name = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    name.send_keys("text")
    last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    last_name.send_keys("text")
    email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    email.send_keys("text")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
