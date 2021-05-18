#!/usr/bin/env python
# -*-coding:utf-8 -*-
#  @Time : 2021/5/14 下午9:05
#  @File : 07综合练习2.py
#  @Software : PyCharm
#  @Author : Anna

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#2.1、打开百度页面，定位更多，定位任意一个图标

def morebtn():
    a_btn = driver.find_element_by_link_text('更多')
    ActionChains(driver).move_to_element(a_btn).perform()
    sleep(4)
    pan_btn = driver.find_element_by_name('tj_wangpan')
    pan_btn.click()


#2.2、打开百度页面，定位高级搜索
def advancedsearch():
    setting = driver.find_element_by_id('s-usersetting-top')
    ActionChains(driver).move_to_element(setting).perform()
    a_advanced_search = driver.find_element_by_link_text('搜索设置')
    a_advanced_search.click()
    # 定位搜索结果
    search_result_all_key = driver.find_element_by_name('q1')
    search_result_intact_key = driver.find_element_by_name('q2')
    search_result_angway_key = driver.find_element_by_name('q3')
    search_result_not_in = driver.find_element_by_name('q4')
    # input = driver.find_elements_by_class_name('adv-ipt7')
    # input.send_keys('selenium')
    # sleep(4)
    # searhch_btn = driver.find_elements_by_class_name('advanced-search-btn')
    # searhch_btn.click()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    url = 'https://www.baidu.com'
    driver.get(url)
    # morebtn()
    advancedsearch()
    # driver.quit()

