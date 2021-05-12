#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/11 下午9:03
#  @File : base_operate.py
#  @Software : PyCharm
#  @Author : Anna
from selenium import webdriver
from time import  sleep

if __name__ == "__main__":
    driver = webdriver.Chrome()
    baidu_url = "https://www.baidu.com"
    biying_url = "https://cn.bing.com/"
    # 打开url
    driver.get(baidu_url)
    sleep(2)
    driver.get(biying_url)
    sleep(2)
    # 返回
    driver.back()
    # 前进
    driver.forward()

