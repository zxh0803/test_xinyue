# coding=utf-8
from selenium import webdriver
from page.login_page import Login_Page
from page.management_page import Management_Page
from page.add_units_page import Add_Units_Page
import unittest
import time

class Test_Add_Units(unittest.TestCase):
    u"测试正常添加设备"
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
        cls.manage_driver.click_units()
        cls.units_driver = Add_Units_Page(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_user01(self):
        time.sleep(10)
        self.units_driver.click_units_new()
        self.units_driver.input_unit_name("unit20171113")
        self.units_driver.input_IMEI("201711131115001")
        time.sleep(2)
        self.units_driver.click_unit_save()
        time.sleep(5)
        r = self.units_driver.is_success_add_unit("201711131115001")
        self.assertTrue(r,msg=u"添加设备失败")







if __name__ == '__main__':
    unittest.main()