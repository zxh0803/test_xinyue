# coding=utf-8
from selenium import webdriver
from common.base import Base
from page.login_page import Login_Page
from page.management_page import Management_Page
import time

class Add_Owners_Page(Base):
    owners_new_loc = ("xpath",".//*[@id='button-2111-btnInnerEl']")
    owner_name_loc = ("xpath",".//*[@id='textfield-1832-inputEl']")
    owner_save_loc = ("xpath",".//*[@id='button-1851-btnInnerEl']")
    owner_name_text_loc = ("xpath",".//*[starts-with(@id,'tableview-1823-record-')]/tbody/tr/td[1]/div")

    def click_owners_new(self):
        self.my_click(self.owners_new_loc)

    def input_owner_name(self,text):
        self.my_send_keys(self.owner_name_loc,text)

    def click_owner_save(self):
        self.my_click(self.owner_save_loc)

    def is_success_add_owner(self,text):
        elements = self.my_find_elements(self.owner_name_text_loc)
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
    manage_driver.click_owners()
    time.sleep(2)
    owner = Add_Owners_Page(driver)
    owner.click_owners_new()
    time.sleep(2)
    owner.input_owner_name("zxh1110")
    owner.click_owner_save()
    time.sleep(3)
    print owner.is_success_add_owner("zxh1110")
