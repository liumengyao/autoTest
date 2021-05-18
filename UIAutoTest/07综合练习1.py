#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/13 下午10:32
#  @File : 06综合练习1.py
#  @Software : PyCharm
#  @Author : Anna
from selenium import webdriver
from time import sleep

'''
1、打开建行页面，登陆后，定位左上角4个链接并打印链接文本
'''

def login(username, password):
    frame = driver.find_element_by_id('fQRLGIN')
    driver.switch_to.frame(frame)
    username_input = driver.find_element_by_id('USERID')
    password_input = driver.find_element_by_id('LOGPASS')
    username_input.send_keys(username)
    password_input.send_keys(password)
    sleep(2)
    driver.switch_to.default_content()


def print_link_text():
    div = driver.find_elements_by_class_name('info_leftli')
    for i in div:
        print(i.text)


if __name__ == '__main__':
    username = 'anna'
    password = '123456'
    driver = webdriver.Chrome()
    url = 'https://ibsbjstar.ccb.com.cn/CCBIS/V6/common/login.jsp'
    driver.get(url)
    login(username, password)
    print_link_text()
    driver.quit()
