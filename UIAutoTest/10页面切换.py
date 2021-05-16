#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/16 下午10:39
#  @File : 10页面切换.py
#  @Software : PyCharm
#  @Author : Anna

from selenium import webdriver
import os
from time import sleep

'''
页面句柄：
        窗口句柄就相当于身份证号,每个窗口都有一个编号,操作系统用这个编号来发送消息的
        获取所有句柄：driver.window_handles()
        获取当前句柄：driver.current_window_handles()
        句柄切换：driver.switch_to.window(handle)
'''
def search():
    input = driver.find_element_by_id('sb_form_q')
    input.send_keys('selenium')


if __name__ == "__main__":
    driver = webdriver.Chrome()
    filePath = os.path.abspath('pop.html').replace('UIAutoTest', 'TestFiles')
    driver.get('file://'+filePath)
    baidu_url = driver.find_element_by_id('goo1')
    baidu_url.click()
    sleep(2)
    bing_url = driver.find_element_by_id('goo2')
    bing_url.click()
    sleep(2)
    csdn_url = driver.find_element_by_id('goo3')
    csdn_url.click()
    sleep(2)
    click_url = driver.find_element_by_id('goo4')
    csdn_url.click()
    sleep(2)
    handles = driver.window_handles
    for handle in handles:
        driver.switch_to.window(handle)
        print(driver.title)
        if 'Bing' in driver.title:
            search()
            break
    sleep(2)
    driver.quit()
