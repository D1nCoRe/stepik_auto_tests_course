import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('numberlink', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, numberlink):
    link = f"https://stepik.org/lesson/{numberlink}/step/1"
    browser.get(link)
    answer = browser.find_element(By.XPATH, '//textarea[@placeholder="Напишите ваш ответ здесь..."]')
    number = math.log(int(time.time()))
    answer.send_keys(number)
    button = browser.find_element(By.CLASS_NAME, 'submit-submission')
    button.click()
    word_t = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    word = word_t.text
    print(word)
