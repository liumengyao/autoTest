#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/15 下午2:08
#  @File : 08键盘操作.py
#  @Software : PyCharm
#  @Author : Anna
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    search_input = driver.find_element_by_id('kw')
    search_input.send_keys('selenium')
    sleep(5)
    search_input.send_keys(Keys.DOWN)
    sleep(5)
    search_input.send_keys(Keys.DOWN)
    sleep(5)
    search_input.send_keys(Keys.DOWN)
    sleep(5)
    search_input.send_keys(Keys.UP)
    sleep(5)
    search_input.send_keys(Keys.UP)
    driver.quit()

