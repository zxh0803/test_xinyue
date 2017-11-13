# coding=utf-8
from selenium import webdriver
from page.login_page import Login_Page
from page.management_page import Management_Page
from page.add_users_page import Add_Users_Page
import unittest
import time

class Test_Add_Users(unittest.TestCase):
    u"测试正常添加用户"
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://192.168.3.200/AIO7/')
        cls.driver.maximize_window()
        cls.login_driver = Login_Page(cls.driver)
        cls.login_driver.input_uername("zxhroute")
        cls.login_driver.input_pwd("123456")
        cls.login_driver.login_click()
        cls.manage_driver = Management_Page(cls.driver)
        time.sleep(10)
        cls.manage_driver.click_management()
        cls.manage_driver.click_users()
        cls.users_driver = Add_Users_Page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_user01(self):
        time.sleep(10)
        self.users_driver.click_users_new()
        self.users_driver.input_name_new("zxh20171113")
        self.users_driver.input_pwd_new("123456")
        self.users_driver.input_confirm_pwd("123456")
        time.sleep(2)
        self.users_driver.save_users()
        time.sleep(2)
        r = self.users_driver.is_succeed_add_users("zxh20171113")
        self.assertTrue(r,msg=u"添加用户失败")






if __name__ == '__main__':
    unittest.main()