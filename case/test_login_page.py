# coding=utf-8
from selenium import webdriver
from page.login_page import Login_Page
import unittest
import time

class Test_Login_Page(unittest.TestCase):
    u"测试登陆页面"
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Firefox()
    #     cls.driver.get('http://192.168.3.200/AIO7/')
    #     cls.driver.maximize_window()
    #     cls.login_driver = Login_Page(cls.driver)

    def setUp(self):
         self.driver = webdriver.Firefox()
         self.driver.get('http://192.168.3.200/AIO7/')
         self.driver.maximize_window()
         self.login_driver = Login_Page(self.driver)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    def tearDown(self):
        self.driver.quit()

    def test_login01(self):
        u'''输入正确的用户名和密码'''
        self.login_driver.input_uername("zxhroute")
        self.login_driver.input_pwd("123456")
        self.login_driver.login_click()
        time.sleep(10)
        r = self.login_driver.is_succeed_login("zxhroute")
        self.assertTrue(r,msg=u"输入正确的用户名和密码，登陆失败")

    def test_login02(self):
        u'''输入错误的密码'''
        self.login_driver.input_uername("zxhroute")
        self.login_driver.input_pwd("789123")
        self.login_driver.login_click()
        time.sleep(5)
        r = self.login_driver.is_user_pwd_wrong("User name or password is wrong111") #为了演示效果，加上111使其断言失败
        self.assertTrue(r,msg=u"输入错误的密码")

if __name__ == '__main__':
    unittest.main()