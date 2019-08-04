# coding:utf-8

import unittest
import time
import HTMLTestRunnerCN
from selenium import webdriver


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.base_url = 'http:www.baidu.com'
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        driver.find_element_by_id('kw').send_keys('cnblogs')
        driver.find_element_by_id('su').click()

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
        print(132)
        suite=unittest.TestSuite()
        suite.addTest(Baidu("test_search"))
         # suite.addTest(Baidu("test_login"))
         # runner=unittest.TextTestRunner()

        file_name = time.strftime("%Y-%m-%d %H_%m_%S", time.localtime())
        print(file_name)
        fp = open("./" + file_name + "_result.html", "wb")
        runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title="测试报告", description="测试执行情况")
        runner.run(suite)