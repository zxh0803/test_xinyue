from common.base import Base
from selenium import webdriver
from page.management_page import Management_Page
from page.login_page import Login_Page
import time

class Add_Drivers_Page(Base):

    drivers_new_loc = ("xpath",".//*[@id='driversNew-btnInnerEl']")
    drivers_name_loc = ("xpath",".//*[@id='textfield-1865-inputEl']")
    drivers_code_loc = ("xpath",".//*[@id='textfield-1866-inputEl']")
    drivers_phone_loc = ("xpath",".//*[@id='textfield-1867-inputEl']")
    drivers_remark_loc = ("xpath",".//*[@id='textarea-1868-inputEl']")
    drivers_save_loc = ("xpath",".//*[@id='button-1875-btnInnerEl']")
    drivers_name_text_loc = ("xpath",".//*[starts-with(@id,'ext-element')]/td[1]/div")

    def click_drivers_new(self):
        self.my_click(self.drivers_new_loc)

    def input_drivers_name(self,text):
        self.my_send_keys(self.drivers_name_loc,text)

    def input_drivers_code(self,text):
        self.my_send_keys(self.drivers_code_loc,text)

    def input_driver_phone(self,text):
        self.my_send_keys(self.drivers_phone_loc,text)

    def input_drivers_remark(self,text):
        self.my_send_keys(self.drivers_remark_loc,text)

    def click_drivers_save(self):
        self.my_click(self.drivers_save_loc)

    def is_success_add_driver(self,text):
        elements = self.my_find_elements(self.drivers_name_text_loc)
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
    manage_driver.click_drivers()
    time.sleep(2)
    drivers = Add_Drivers_Page(driver)
    drivers.click_drivers_new()
    time.sleep(2)
    drivers.input_drivers_name("driver1110")
    drivers.input_drivers_code("127444646")
    drivers.input_driver_phone("13512345678")
    drivers.input_drivers_remark("testdriver")
    drivers.click_drivers_save()
    time.sleep(3)
    print drivers.is_success_add_driver("driver1110")

