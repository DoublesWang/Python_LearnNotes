# coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://xdclass.net/#/index")
driver.maximize_window()

time.sleep(5)
# 点击登录按钮
# driver.find_element_by_xpath('//span[contains(.,登录)]').click()
# driver.find_element_by_xpath('//span[@text="登录"]').click()
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[4]/div[1]/span[1]').click()

try:
    # 输入用户名和密码信息
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[1]/input').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[1]/input').send_keys(123456)

    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[2]/input').click()
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div/div[2]/input').send_keys(123456)

    # 点击登录
    driver.find_element_by_xpath('//button[contains(.,"登录")]')

    # 尝试执行搜索
    driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[2]/input').click()

except:
    driver.get_screenshot_as_file("./error.png")