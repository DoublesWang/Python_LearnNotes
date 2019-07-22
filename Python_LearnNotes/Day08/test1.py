# coding:utf-8

import unittest
import time
from selenium import webdriver

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def testSearch(self):
        driver = self.driver
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(5)
        expectvalue = "selenium_百度搜索"
        realvalue = driver.title
        self.assertEqual(expectvalue,realvalue)
        # print(realvalue)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()