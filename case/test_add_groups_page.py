# coding=utf-8
from selenium import webdriver
from page.login_page import Login_Page
from page.management_page import Management_Page
from page.add_groups_page import Add_Groups_Page
import unittest
import time

class Test_Add_Groups(unittest.TestCase):
    u"测试正常添加设备组"
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
        cls.manage_driver.click_groups()
        cls.groups_driver = Add_Groups_Page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_groups01(self):
        self.groups_driver.click_groups_new()
        self.groups_driver.input_group_name("group20171113")
        time.sleep(2)
        self.groups_driver.click_groups_save()
        time.sleep(5)
        r = self.groups_driver.is_success_add_gourp("group20171113")
        self.assertTrue(r,msg=u"添加用户组失败")









if __name__ == '__main__':
    unittest.main()