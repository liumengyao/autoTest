#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/12 下午10:11
#  @File : 03常用元素处理.py
#  @Software : PyCharm
#  @Author : Anna

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import  sleep
import os

if __name__ == "__main__":
    '''
    常用元素处理：
    输入框：
            内容清空：element.clear() 一般用在正式测试之前
            获取某个属性值：  element.get_attribute() 一般用于debug时确定元素
    按钮：
            btn.click()点击按钮
            btn.is_enabled() 判断按钮是否可以点击
            btn.is_displayed() 判断按钮是否可见
            btn.is_selected() 判断是否被选中
    下拉选择框：selenium中的select库，必须是标准select（外面是select 里面是option标签）
              使用时需要先引入
             select.select_by_value('') 根据值选择
             select.select_by_index() 根据索引选择元素
             select.select_by_visible_text()  根据可见元素文本
    单选框：
    复选框：
    文件上传：btn.sendkes(文件路径) 普通表单上传文件：tag为input type为file
    
    example:打开TestFiles/autotest.html文件，定位username和password 
    '''
    # 文件路径拼接
    autest_path = os.path.abspath('autotest.html').replace('UIAutoTest', 'TestFiles')

    driver = webdriver.Chrome()
    driver.get('file://'+autest_path)
    username = driver.find_element_by_id('accountID')
    username.send_keys('admin')
    username.clear()
    username.send_keys('admin')
    password = driver.find_element_by_id('passwordID')
    password.send_keys('123456')
    print(username.get_attribute('id'))


    # 下拉选择框

    select = Select(driver.find_element_by_id('areaID'))
    select.select_by_value('beijing')
    sleep(1)
    select.select_by_index(2)
    sleep(1)
    select.select_by_visible_text('陕西省')
    sleep(5)
    # 单选按钮
    btn1 = driver.find_element_by_id('sexID1')
    print("点击前：", btn1.is_selected())
    btn1.click()
    print("点击后：", btn1.is_selected())
    # 复选按钮
    btn2 = driver.find_element_by_id('u1')
    print("点击前：", btn2.is_selected())
    btn2.click()
    print("点击后：", btn2.is_selected())

    btn3 = driver.find_element_by_id('u2')
    print("点击前：", btn3.is_selected())
    # 点击两次可取消点击
    btn3.click()
    btn3.click()
    print("点击后：", btn3.is_selected())
    # 文件上传
    upload_btn = driver.find_element_by_name('file')
    upload_btn.send_keys(autest_path)
    sleep(5)

    driver.quit()
