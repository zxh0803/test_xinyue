# coding=utf-8
from selenium import webdriver
from common.base import Base
from page.login_page import Login_Page
from page.management_page import Management_Page
import time

class Add_Units_Page(Base):

    unit_new_loc = ("xpath",".//*[@id='unitsNew-btnInnerEl']")
    unit_name_loc = ("xpath",".//*[@id='textfield-1684-inputEl']")
    unit_IMEI_loc = ("xpath",".//*[@id='textfield-1686-inputEl']")
    unit_SIM_loc = ("xpath",".//*[@id='textfield-1687-inputEl']")
    unit_save_loc = ("xpath",".//*[@id='button-1775-btnInnerEl']")
    units_name_text_loc = ("xpath",".//*[starts-with(@id,'tableview-1675-record')]/tbody/tr/td[3]/div")
    def click_units_new(self):
        self.my_click(self.unit_new_loc)

    def input_unit_name(self,text):
        self.my_send_keys(self.unit_name_loc,text)

    def input_IMEI(self,text):
        self.my_send_keys(self.unit_IMEI_loc,text)

    def input_SIM(self,text):
        self.my_send_keys(self.unit_SIM_loc,text)

    def click_unit_save(self):
        self.my_click(self.unit_save_loc)

    def is_success_add_unit(self,text):

        elements = self.my_find_elements(self.units_name_text_loc)
        for i in elements:
            if i.text == text:
                return True


if __name__ == '__main__':

    driver = webdriver.Firefox()
    driver.get("http://192.168.3.200/AIO7/")
    driver.maximize_window()
    login_driver = Login_Page(driver)
    login_driver.input_uername("zxhroute")
    login_driver.input_pwd("123456")
    login_driver.login_click()
    time.sleep(10)
    manage_driver = Management_Page(driver)
    manage_driver.click_management()
    time.sleep(3)
    manage_driver.click_units()
    time.sleep(2)
    unit_driver = Add_Units_Page(driver)
    time.sleep(2)
    unit_driver.click_units_new()
    unit_driver.input_unit_name("zxhtest20171110")
    unit_driver.input_IMEI("201711101115001")
    unit_driver.input_SIM("13512345678")
    time.sleep(2)
    unit_driver.click_unit_save()
    time.sleep(5)
    print unit_driver.is_success_add_unit("201711101115001")




