# coding:utf-8

import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试")
        self.name = "小D课堂"
        self.age  = 28
    def test_name(self):
        print("调用test_name")
        self.assertEqual(self.name,"小D课堂",msg = "名字不对")

    def test_isupper(self):
        print("调用test_isupper")
        self.assertTrue("xdclass".isupper(),msg = "不是大写")

    def test_age(self):
        print("调用test_age")
        self.assertFalse(self.age,28)

    def tearDown(self):
        print("测试完毕")


if __name__ == '__main__':
    unittest.main()
