# coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://xdclass.net/#/index")

print(driver.title)
time.sleep(5)

driver.add_cookie({"name":"name","value":"jack"})
driver.add_cookie({"name":"token","value":""})