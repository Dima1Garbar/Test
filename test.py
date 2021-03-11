import os
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
    return math.log(abs(12*math.sin(x)))

browser_link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(r"C:\Users\Dimon\chromedriver\chromedriver.exe")
browser.get(browser_link)
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
browser.find_element_by_xpath("//button[text()='Book']").click()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
x = browser.find_element_by_id("input_value")
answer = calc(int(x.text))
form = browser.find_element_by_id("answer")
form.send_keys(str(answer))
browser.find_element_by_xpath("//button[text()='Submit']").click()