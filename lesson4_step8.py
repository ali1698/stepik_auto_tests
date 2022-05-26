from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)



element = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

button = browser.find_element_by_id("book")
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

element2 = browser.find_element_by_id("input_value")
x = element2.text
y = calc(x)

element3 = browser.find_element_by_id("answer")
element3.send_keys(y)

button = browser.find_element_by_id ("solve")
button.click()


