#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/16 下午11:19
#  @File : 11xpath定位.py
#  @Software : PyCharm
#  @Author : Anna
from selenium import webdriver
import os
from time import sleep

'''
xpath定位：扫dom树
    xpath中的索引从1开始
    以/开始为绝对路径
    以//开始为相对路径
cssSelector：基于css装饰器 比xpath效率高
    
'''

if __name__ == "__main__":
    driver = webdriver.Chrome()
    filePath = os.path.abspath('css.html').replace('UIAutoTest', 'TestFiles')
    driver.get('file://' + filePath)
    # xpath定位 /html/body/div/form/input[6]
    input_btn = driver.find_element_by_xpath('//input[@value="ks10cf6d6"] ')
    # 定位Cat元素
    cat = driver.find_element_by_xpath("//*[@id='recordlist']/li[1]").text
    # text函数
    print(driver.find_element_by_xpath("//*[text()='Heading']").text)
    # print(driver.find_element_by_xpath("//*[@text='Heading']")) #浏览器兼容性不好,app中经常使用
    print(cat)

    # css定位
    print(driver.find_element_by_css_selector("input[value=ks10cf6d6]").text)
    print(driver.find_element_by_css_selector("#recordlist > p").text)
    print(driver.find_element_by_css_selector("#recordlist > p+li").text)
    print(driver.find_element_by_css_selector("#recordlist > p+li+li").text)
    # li的第五个
    print(driver.find_element_by_css_selector("#recordlist > li:nth-child(5)").text)

    driver.quit()
