# coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("file:///C:/Users/water/Desktop/test1.html")
driver.maximize_window()
print(driver.title)

print("默认选中male，2秒后选择female")
time.sleep(5)
driver.find_element_by_id("female").click()

