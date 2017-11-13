from common.base import Base
from selenium import webdriver
from page.management_page import Management_Page
from page.login_page import Login_Page
import time

class Add_Groups_Page(Base):

    groups_new_loc = ("xpath",".//*[@id='button-2101-btnInnerEl']")
    groups_name_loc = ("xpath",".//*[@id='textfield-1788-inputEl']")
    groups_save_loc = ("xpath",".//*[@id='button-1815-btnInnerEl']")
    groups_name_text_loc = ("xpath",".//*[starts-with(@id,'tableview-1782-record')]/tbody/tr/td[1]/div")

    def click_groups_new(self):
        self.my_click(self.groups_new_loc)

    def input_group_name(self,text):
        self.my_send_keys(self.groups_name_loc,text)

    def click_groups_save(self):
        self.my_click(self.groups_save_loc)

    def is_success_add_gourp(self,text):
        elements = self.my_find_elements(self.groups_name_text_loc)
        for i in elements:
            if i.text==text:
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
    manage_driver.click_groups()
    time.sleep(2)
    group = Add_Groups_Page(driver)

    group.click_groups_new()
    time.sleep(2)
    group.input_group_name("zxh1110")
    group.click_groups_save()
    time.sleep(3)
    print group.is_success_add_gourp("zxh1110")
