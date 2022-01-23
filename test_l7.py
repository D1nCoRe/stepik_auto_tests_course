import unittest
import pytest
from selenium import webdriver
import time

import unittest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestInput(unittest.TestCase):
    browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_abs1(self):
        browser = self.browser
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        name = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        name.send_keys("text")
        last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        last_name.send_keys("text")
        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys("text")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_abs2(self):
        browser = self.browser
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        name = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        name.send_keys("text")
        last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        last_name.send_keys("text")
        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys("text")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    # assert("Congratulations! You have successfully registered!" == welcome_text)
if __name__ == "__main__":
    unittest.main()

