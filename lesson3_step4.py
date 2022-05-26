from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc (x):
  return str(math.log(abs(12*math.sin(int(x)))))

input1 = browser.find_element_by_id("input_value")
x = input1.text
y = calc(x)

input2 = browser.find_element_by_id("answer")
input2.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(10)
browser.quit()
