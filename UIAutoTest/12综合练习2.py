# -*- coding: utf-8 -*-
# @Time : 2021/5/21 10:33
# @Author : Anna
# @Email : 734666093@qq.com
# @File : 12综合练习2.py
# @time :2021/05/21
# @Project : autoTest
# @Description :


from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from time import sleep
import os

'''
打开mtx系统：
1、登陆
2、
'''


class MTX(object):
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        driver.find_element_by_name("username").send_keys('shamo')
        driver.find_element_by_name("login_pwd").send_keys('123456')
        driver.find_element_by_xpath("//*[text()='登录']").click()

    def cookie_login(self):
        driver.delete_all_cookies()
        driver.add_cookie({'name': 'PHPSESSID', 'value': 'c9412087629ee8ef5ec9a07395c20beb'})

    def add_user(self):
        driver.find_element_by_xpath("//*[text()='用户管理']").click()
        # driver.find_element_by_xpath("//*[text()='用户列表']").click()
        driver.find_element_by_xpath("//*[@id=\"power-menu-126\"]/li/a").click()
        driver.switch_to.frame('ifcontent')
        driver.find_element_by_partial_link_text("新增").click()
        # table_list = driver.find_elements_by_class_name("am-radius")
        table_list = driver.find_elements_by_css_selector(".am-form-group > .am-radius")
        insert_list =["test1", "anna", "15200012345", "123456789@qq.com", "支付宝", "百度", "头条", "qq", "QQ", "微信1", "微信2", "微信3"]
        for i in range(0, 12):
            table_list[i].send_keys(insert_list[i])

        #日期输入框
        driver.execute_script("arguments[0].value='2021-5-25'", table_list[12])
        # driver.execute_script("arguments[0].value='1999-10-10'", driver.find_element_by_name("birthday"))
        #地址
        table_list[13].send_keys("北京市")
        #性别
        driver.find_elements_by_class_name("am-icon-checked")[2].click()
        #积分
        driver.find_element_by_name("integral").send_keys('100')
        #用户状态
        driver.find_elements_by_class_name("chosen-single")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://10.1.60.83/mtx/admin.php?s=/admin/logininfo.html")
    driver.maximize_window()
    mtx = MTX(driver)
    # mtx.login()
    mtx.cookie_login()
    driver.get("http://10.1.60.83/mtx/admin.php?s=/index/index.html")
    mtx.add_user()
    sleep(2)
    # driver.quit()
