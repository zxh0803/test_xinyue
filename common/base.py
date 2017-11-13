# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base:

    def __init__(self,driver):
        '''默认启动火狐浏览器'''
        self.driver = driver

    def get(self,url):
        '''浏览器输入网址'''
        self.driver.get(url)
        self.driver.maximize_window()
    def close(self):
        self.driver.quit()

    def my_find_element(self,locator,timeout=10):
        '''定位元素'''
        # element = WebDriverWait(self.driver,10).until(lambda x:x.find_element(*locator))
        element =WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return element
    def my_find_elements(self,locator,timeout=10):
        '''定位一组元素'''
        elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def my_send_keys(self,locator,text):
        '''输入框输入数据'''
        element = self.my_find_element(locator)
        element.clear()
        element.send_keys(text)

    def my_click(self,locator):
        '''点击元素'''
        self.my_find_element(locator).click()

    def is_value(self,locator,value):
        '''判断元素是否存在value'''
        result = EC.text_to_be_present_in_element_value(locator,value)(self.driver)
        return result

    def is_text(self,locator,text):
        '''判断元素是否存在text'''
        result = EC.text_to_be_present_in_element(locator,text)(self.driver)
        return result

    def is_title(self,title,timeout=10):
        '''判断标题是否等于'''
        result = WebDriverWait(self.driver,timeout).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''判断标题是否包含'''
        result = WebDriverWait(self.driver,timeout).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        '''刞断元素被选中，迒回布尔值,'''
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_located_to_be_selected(locator))
        return result

    def mouse_to_element(self, locator):
        '''鼠标悬停'''
        element = self.my_find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def select_by_index(self, locator, index):
        '''通过索引,index是索引第几个，从0开始'''
        element = self.my_find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        '''通过value属性'''
        element = self.my_find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.my_find_element(locator)
        Select(element).select_by_value(text)

    def get_screenshot(self,fpath):
        self.driver.get_screenshot_as_file(fpath)

    def get_handls(self):
        handles = self.driver.window_handles
        return handles

    def to_window(self,h):
        self.driver.switch_to_window(h)

    def is_find_element(self,locator):
        r = EC.presence_of_element_located(locator)
        return r

    def mouse_perfrom(self,locator):
        mouse = self.my_find_element(locator)
        ActionChains(self.driver).move_to_element(mouse).perform()
        import time
        time.sleep(10)




if __name__ == '__main__':

    username_loc = ('id','textfield-1018-inputEl')
    pwd_loc = ('id','textfield-1020-inputEl')
    login_button_loc = ('id','loginBtn-btnInnerEl')
    forgot_pwd_loc = ('xpath',".//*[@id='forgotPass']/font")
    forgot_jump_loc = ('id',"resetButton-btnInnerEl")
    ass_name_loc = ('id',"topBtnUsername")
    driver = webdriver.Firefox()
    driver.get("http://192.168.3.200/AIO7/")
    driver.maximize_window()
    login = Base(driver)
    login.my_send_keys(username_loc,"zxhroute")
    login.my_send_keys(pwd_loc,"")
    login.my_click(login_button_loc)
    login.mouse_perfrom(pwd_loc)





