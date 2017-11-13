from common.base import Base
from selenium import webdriver
from page.management_page import Management_Page
from page.login_page import Login_Page
import time
import random

class Add_Alert_page(Base):

    alert_setting_loc = ("xpath",".//*[@id='menuAlertsBtnView-btnInnerEl']")
    alert_new_loc = ("xpath",".//*[@id='alertsBtnNew-btnInnerEl']")
    alert_name_loc = ("xpath",".//*[@id='textfield-1405-inputEl']")
    alert_xiala_loc = ("xpath",".//*[@id='treeview-1415-record-1271']/tbody/tr/td[2]/div/div")
    alert_units_loc = ("xpath",".//*[starts-with(@id,'treeview-1415-record')]/tbody/tr/td[1]/div/span")
    alert_maxspeed_loc = ("xpath",".//*[@id='speedMax']")
    alert_save_loc = ("xpath",".//*[@id='button-2076-btnInnerEl']")
    alert_alert_name_loc = ("xpath",".//*[starts-with(@id,'tableview-1399-record')]/tbody/tr/td[1]/div")

    def click_alert_setting(self):
        self.my_click(self.alert_setting_loc)

    def click_alert_new(self):
        self.my_click(self.alert_new_loc)

    def input_alert_name(self,text):
        self.my_send_keys(self.alert_name_loc,text)

    def cilck_alert_xiala(self):
        self.my_click(self.alert_xiala_loc)

    def select_units(self):
        elements = self.my_find_elements(self.alert_units_loc)
        elements[0].click()
    def input_maxspeed(self,text):
        self.my_send_keys(self.alert_maxspeed_loc,text)

    def click_alert_save(self):
        self.my_click(self.alert_save_loc)

    def is_success_add_alert(self,text):
        r = self.is_text(self.alert_alert_name_loc,text)
        return r

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.3.200/AIO7/")
    driver.maximize_window()
    login_driver = Login_Page(driver)
    login_driver.input_uername("zxhroute")
    login_driver.input_pwd("123456")
    login_driver.login_click()
    time.sleep(10)
    alert = Add_Alert_page(driver)
    alert.click_alert_setting()
    alert.click_alert_new()
    alert.input_alert_name("zidonghuaalert")
    alert.cilck_alert_xiala()
    alert.select_units()
    alert.input_maxspeed("90")
    alert.click_alert_save()
    time.sleep(5)
    print alert.is_success_add_alert("zidonghuaalert")
