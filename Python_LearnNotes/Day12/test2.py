# coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("file:///C:/Users/water/Desktop/test2.html")
driver.maximize_window()
print(driver.title)

"""
弹窗常用方法 accept, dismiss
"""
time.sleep(5)
driver.find_element_by_id("alert").click()
# 切换到弹窗
Window1 = driver.switch_to_alert()
time.sleep(5)
Window1.accept()

driver.find_element_by_id("confirm").click()
# 切换到弹窗
Window2 = driver.switch_to_alert()
time.sleep(5)
Window2.dismiss()


