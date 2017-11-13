# coding=utf-8
from common.base import Base
from selenium import webdriver
from page.login_page import Login_Page

class Management_Page(Base):

    management_loc = ("id","menuManagementBtnView")
    users_loc = ("xpath",".//*[@id='button-1953-btnInnerEl']")
    units_loc = ("xpath",".//*[@id='button-1954-btnInnerEl']")
    groups_loc = ("xpath",".//*[@id='button-1955-btnInnerEl']")
    owners_loc = ("xpath",".//*[@id='button-1956-btnInnerEl']")
    drivers_loc = ("xpath",".//*[@id='button-1957-btnInnerEl']")

    account_text_loc = ('xpath',".//*[@id='gridcolumn-1627-textInnerEl']")
    IMEI_text_loc = ("xpath",".//*[@id='gridcolumn-1672-textInnerEl']")
    creator_text_loc = ("xpath",".//*[@id='gridcolumn-1779-textInnerEl']")
    email_text_loc = ("xpath",".//*[@id='gridcolumn-1819-textInnerEl']")
    code_text_loc = ("xpath",".//*[@id='gridcolumn-1854-textInnerEl']")

    def click_management(self):
        self.my_click(self.management_loc)

    def click_users(self):
        self.my_click(self.users_loc)

    def click_units(self):
        self.my_click(self.units_loc)

    def click_groups(self):
        self.my_click(self.groups_loc)

    def click_owners(self):
        self.my_click(self.owners_loc)

    def click_drivers(self):
        self.my_click(self.drivers_loc)

    def is_success_click_users(self,text="Account"):
        r =  self.is_text(self.account_text_loc,text)
        return r

    def is_success_click_units(self,text="IMEI"):
        r = self.is_text(self.IMEI_text_loc,text)
        return r

    def is_success_click_groups(self,text="Creator"):
        r = self.is_text(self.creator_text_loc,text)
        return r

    def is_success_click_owners(self,text="Email"):
        r = self.is_text(self.email_text_loc,text)
        return r

    def is_success_click_drivers(self,text="Code"):
        r = self.is_text(self.code_text_loc,text)
        return r

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.3.200/AIO7/")
    driver.maximize_window()
    login_driver = Login_Page(driver)
    login_driver.input_uername("zxhroute")
    login_driver.input_pwd("123456")
    login_driver.login_click()
    import time
    time.sleep(10)
    manage_driver = Management_Page(driver)
    time.sleep(3)
    manage_driver.click_management()
    time.sleep(3)
    manage_driver.click_users()
    print manage_driver.is_success_click_users()
    time.sleep(3)
    manage_driver.click_units()
    print manage_driver.is_success_click_units()
    time.sleep(3)
    manage_driver.click_groups()
    print manage_driver.is_success_click_groups()
    time.sleep(3)
    manage_driver.click_owners()
    print manage_driver.is_success_click_owners()
    time.sleep(3)
    manage_driver.click_drivers()
    print manage_driver.is_success_click_drivers()
