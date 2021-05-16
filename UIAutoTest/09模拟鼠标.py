#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/16 上午11:23
#  @File : 模拟鼠标.py
#  @Software : PyCharm
#  @Author : Anna

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    click_filePath = os.path.abspath('Clicks.html').replace('UIAutoTest', 'TestFiles')
    driver.get('file://'+click_filePath)
    sleep(5)
    button1 = driver.find_element_by_id('button1')
    print(button1.get_attribute('value'))
    # 双击
    ActionChains(driver).double_click(button1).perform()
    sleep(5)
    button2 = driver.find_element_by_id('button2')
    button2.click()
    button3 = driver.find_element_by_id('button3')
    ActionChains(driver).context_click(button3).perform()
    sleep(5)
    driver.quit()
