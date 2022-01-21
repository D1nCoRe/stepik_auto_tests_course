import math
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

browser = webdriver.Chrome(ChromeDriverManager().install())


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()

    # browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
    # from selenium.webdriver.common.keys import Keys
    # browser.find_element_by_tag_name('body').send_keys(Keys.END)

    # browser.execute_script("window.scrollBy(0, 150);")

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    num = calc(x)
    otvet = browser.find_element(By.ID, 'answer')
    otvet.send_keys(num)

    button1 = browser.find_element(By.ID, 'robotCheckbox')
    button1.location_once_scrolled_into_view
    button1.click()

    button2 = browser.find_element(By.ID, 'robotsRule')
    button2.location_once_scrolled_into_view
    button2.click()

    button3 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button3.location_once_scrolled_into_view
    button3.click()

    time.sleep(10)

finally:
    browser.quit()

