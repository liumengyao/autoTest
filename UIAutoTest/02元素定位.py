#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/11 下午9:49
#  @File : 02元素定位.py
#  @Software : PyCharm
#  @Author : Anna
from selenium import webdriver
from time import  sleep

if __name__ == "__main__":
    driver = webdriver.Chrome()
    '''
    单元素定位：
            driver.find_element_by_id()
            driver.find_element_by_name()
            driver.find_element_by_class_name()
            find_element_by_tag_name()
    example:
    1.打开百度搜索，输入seleium，点击搜索
    '''
    url = "https://www.baidu.com/"
    driver.get(url)
    # id定位
    # select = driver.find_element_by_id("kw")
    # name 定位
    select = driver.find_element_by_name("wd")
    select.send_keys("selenium")
    # search_btn = driver.find_element_by_id("su")

    search_btn = driver.find_element_by_class_name("s_btn")
    search_btn.click()
    sleep(5)
    driver.back()

    '''
    多元素定位:
            driver.find_element_by_tag_name()
    example2:
            打开百度搜索，点击文本为"地图"的链接
    '''
    a_list = driver.find_elements_by_tag_name('a')
    flag = 1
    for i in a_list:
        if "地图" in i.text:
            print("find map")
            i.click()
        else:
            flag = 0
    if flag:
        print("no find map")
    sleep(5)
    driver.back()

    '''
    链接元素定位方法：
            driver.find_element_by_link_text()
            driver.find_element_by_partial_link_text()
    '''



    driver.quit()