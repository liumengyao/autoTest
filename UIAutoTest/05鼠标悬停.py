#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/13 下午10:31
#  @File : 05鼠标悬停.py
#  @Software : PyCharm
#  @Author : Anna
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import  sleep
import os

if __name__ == "__main__":
    driver = webdriver.Chrome()
    url = "https://www.baidu.com"
    driver.get(url)
    driver.maximize_window()
    settings = driver.find_element_by_id('s-usersetting-top')
    ActionChains(driver).move_to_element(settings).perform()
    sleep(10)
    driver.quit()