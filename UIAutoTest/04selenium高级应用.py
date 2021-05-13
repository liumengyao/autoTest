#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/13 下午8:47
#  @File : 04selenium高级应用.py
#  @Software : PyCharm
#  @Author : Anna
from selenium import webdriver
from time import  sleep
import os

'''
模态框处理：模态对话框与普通对话框区别：1）用F12无法定位 2）不处理掉无法进行下一步操作
        1、警告消息框（alert）
        2、确认消息框（confirm）
        3、提示消息对话（prompt）
'''
if __name__ == "__main__":
    driver = webdriver.Chrome()
    filePath = os.path.abspath('dialogs.html').replace('UIAutoTest', 'TestFiles')
    driver.get('file://'+filePath)
    # alert
    btn1 = driver.find_element_by_id('alert')
    btn1.click()
    sleep(1)
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    sleep(2)
    btn1.click()
    alert.dismiss()
    # confirm
    btn2 = driver.find_element_by_id('confirm')
    btn2.click()
    confirm = driver.switch_to.alert
    sleep(3)
    confirm.accept()
    sleep(3)
    btn2.click()
    print(confirm.text)
    sleep(3)
    confirm.dismiss()

    # prompt
    promptFile = os.path.abspath('testprompt2.html').replace('UIAutoTest', 'TestFiles')
    driver.get('file://'+promptFile)
    btn3 = driver.find_element_by_name('button1')
    btn3.click()
    prompt =  driver.switch_to.alert
    prompt.send_keys('accept')
    sleep(2)
    prompt.accept()
    sleep(2)
    btn3.click()
    sleep(2)
    prompt.send_keys('dismiss')
    sleep(2)
    prompt.dismiss()
    sleep(2)
    driver.quit()


