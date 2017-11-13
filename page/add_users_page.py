from common.base import Base
from selenium import webdriver
from page.management_page import Management_Page
from page.login_page import Login_Page
import time


class Add_Users_Page(Base):


    users_new_loc = ("id","button-2080-btnInnerEl")
    users_name_loc = ("id","textfield-1638-inputEl")
    users_pwd_loc = ("id","textfield-1639-inputEl")
    users_confirm_pwd_loc = ("id","textfield-1640-inputEl")
    save_users_loc = ("id","button-1668-btnInnerEl")
    name_text_loc = ("xpath",".//*[starts-with(@id,'tableview')]/tbody/tr/td[1]/div")



    def click_users_new(self):
        self.my_click(self.users_new_loc)

    def input_name_new(self,text):
        self.my_send_keys(self.users_name_loc,text)

    def input_pwd_new(self,text):
        self.my_send_keys(self.users_pwd_loc,text)

    def input_confirm_pwd(self,text):
        self.my_send_keys(self.users_confirm_pwd_loc,text)

    def save_users(self):
        self.my_click(self.save_users_loc)

    def is_succeed_add_users(self,text):
        elements = self.my_find_elements(self.name_text_loc)
        for i in elements:
            if i.text == text:
                return True


if __name__ == '__main__':

    driver = webdriver.Firefox()
    login_driver = Login_Page(driver)

    login_driver.get("http://192.168.3.200/AIO7/")
    login_driver.input_uername("zxhroute")
    login_driver.input_pwd("123456")
    login_driver.login_click()
    time.sleep(10)
    manage_driver = Management_Page(driver)

    adduser_driver = Add_Users_Page(driver)

    manage_driver.click_management()
    manage_driver.click_users()
    adduser_driver.click_users_new()
    adduser_driver.input_name_new("test123456")
    adduser_driver.input_pwd_new("123456")
    time.sleep(5)
    adduser_driver.input_confirm_pwd("123456")
    time.sleep(2)
    adduser_driver.save_users()
    time.sleep(5)
    adduser_driver.is_succeed_add_users("test123456")

