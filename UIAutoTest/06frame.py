#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/13 下午9:45
#  @File : frame.py
#  @Software : PyCharm
#  @Author : Anna
from selenium import webdriver
from time import  sleep
import os

'''
iframe:selenium每次只能处理一个页面，当页面嵌套iframe时，需要将页面跳转进iframe中才能继续处理
        driver.switch_to_frame(int index) 传入参数为iframe的序号，从零开始
        driver.switch_to_parent_frame() 切换为父级别 高版本selenium可用
        driver.switch_to_frame(String nameOrId) 传入参数为iframe的ID或者Name属性
        driver.switch_to_default_content()切换回默认
'''

if __name__ == "__main__":
    driver = webdriver.Chrome()
    frame_filePath = os.path.abspath('frame.html').replace('UIAutoTest', 'TestFiles')
    main_filePath = os.path.abspath('main.html').replace('UIAutoTest', 'TestFiles')
    # driver.get('file://' + frame_filePath)
    # input = driver.find_element_by_id('input1')
    # input.send_keys('selenium')
    # driver.close()

    # iframe
    driver.get('file://' + main_filePath)
    # 通过索引跳转
    # driver.switch_to.frame(0)
    # 通过id跳转
    # driver.switch_to.frame('frame')
    # 通过元素定位跳转  推荐
    frame = driver.find_element_by_id('frame')
    driver.switch_to.frame(frame)
    input2 = driver.find_element_by_id('input1')
    input2.send_keys('selenium')
    sleep(2)
    driver.quit()
