# coding=utf-8
from common.base import Base
from selenium import webdriver

class Login_Page(Base):

    username_loc = ('id','textfield-1018-inputEl')
    pwd_loc = ('id','textfield-1020-inputEl')
    login_button_loc = ('id','loginBtn-btnInnerEl')
    forgot_pwd_loc = ('xpath',".//*[@id='forgotPass']/font")
    forgot_jump_loc = ('id',"resetButton-btnInnerEl")
    select_language_loc = ('id',"combo-1016-trigger-picker")
    login_result_loc = ("id","topBtnUsername")
    remember_user_loc = ("xpath",".//*[@id='checkbox-1022-boxLabelEl']")
    select_language_loc1 = ("id","combo-1016-trigger-picker")
    select_language_loc2 = ("css selector","ul.x-list-plain>li:nth-child(2)")
    login_username_loc = ("id","topBtnUsername")
    user_pwd_wrong_loc = ("xpath",".//*[@id='errortip']")


    def input_uername(self,username):
        self.my_send_keys(self.username_loc,username)

    def input_pwd(self,pwd):

        self.my_send_keys(self.pwd_loc,pwd)

    def login_click(self):
        self.my_click(self.login_button_loc)

    def forgot_pwd(self):
        self.my_click(self.forgot_pwd_loc)

    def forgot_jump(self):
        text = 'commit'
        return self.is_text(self.forgot_jump_loc,text)

    def select_language(self):
        # self.driver.find_element_by_css_selector("#combo-1016-trigger-picker").click()
        # self.driver.find_element_by_css_selector("ul.x-list-plain>li:nth-child(2)").click()
        self.my_click(self.select_language_loc1) #此处直接定位失败，先定位父级元素
        self.my_click(self.select_language_loc2)

    def remember_user(self):
        if self.my_find_element(self.remember_user_loc).is_selected():
            pass
        else:
            self.my_find_element(self.remember_user_loc).click()

    def is_succeed_login(self,text):
        r = self.is_text(self.login_username_loc,text)
        return r

    def is_succeed_select_language(self,text):
        r = self.is_text(self.forgot_pwd_loc,text)
        return r

    def is_user_pwd_wrong(self,text):
        r = self.is_text(self.user_pwd_wrong_loc,text)
        return r

if __name__ == '__main__':

    driver = webdriver.Firefox()
    login = Login_Page(driver)
    # login.get('http://192.168.3.200/AIO7/')
    # login.select_language()
