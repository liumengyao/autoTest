
# -*- coding: utf-8 -*-
# @Time : 2021/5/21 10:33
# @Author : Anna
# @Email : 734666093@qq.com
# @File : 12综合练习2.py
# @time :2021/05/21
# @Project : autoTest
# @Description :


from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.select import  Select
from time import sleep
import os

'''
打开mtx系统：
1、登陆
2、
'''


class MTX(object):
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        driver.find_element_by_name("username").send_keys('shamo')
        driver.find_element_by_name("login_pwd").send_keys('123456')
        driver.find_element_by_xpath("//*[text()='登录']").click()

    def cookie_login(self):
        driver.delete_all_cookies()
        driver.add_cookie({'name': 'PHPSESSID', 'value': 'c9412087629ee8ef5ec9a07395c20beb'})

    def add_user(self):
        driver.find_element_by_xpath("//*[text()='用户管理']").click()
        sleep(3)
        # driver.find_element_by_xpath("//*[text()='用户列表']").click()
        driver.find_element_by_xpath("//*[@id=\"power-menu-126\"]/li/a").click()
        driver.switch_to.frame('ifcontent')
        driver.find_element_by_partial_link_text("新增").click()
        # table_list = driver.find_elements_by_class_name("am-radius")
        table_list = driver.find_elements_by_css_selector(".am-form-group > .am-radius")
        insert_list =["test1", "anna", "15200012345", "123456789@qq.com", "支付宝", "百度", "头条", "qq", "QQ", "微信1", "微信2", "微信3"]
        for i in range(0, 12):
            table_list[i].send_keys(insert_list[i])

        #日期输入框
        driver.execute_script("arguments[0].value='2021-05-25'", table_list[12])
        # driver.execute_script("arguments[0].value='1999-10-10'", driver.find_element_by_name("birthday"))
        #地址
        table_list[13].send_keys("北京市")
        #性别
        driver.find_elements_by_class_name("am-icon-checked")[2].click()
        #积分
        driver.find_element_by_name("integral").send_keys('100')
        #用户状态
        status = driver.find_element_by_name("status")
        driver.execute_script("arguments[0].style.display='block';", status)
        Select(status).select_by_visible_text('待审核')
        driver.find_element_by_name('pwd').send_keys('123456')
        driver.find_element_by_xpath("//button[text()='保存']").click()
        driver.switch_to.default_content()

    def add_goods(self):
        # driver.get(url)
        driver.find_element_by_css_selector(".common-left-menu > li:nth-child(4)").click()
        driver.find_element_by_css_selector("#power-menu-38 > li:nth-child(1) > a ").click()
        driver.switch_to.frame("ifcontent")
        # 点击新增按钮
        driver.find_element_by_partial_link_text("新增").click()
        goods_name = driver.find_element_by_xpath("// *[ @ id = \"goods-nav-base\"] / div[1] / div / input[2]")
        driver.execute_script("arguments[0].style=\"color: rgb(255, 102, 51);\"", goods_name)
        # 商品名称
        goods_name.send_keys("SKII神仙水")
        # 商品简述
        driver.find_element_by_css_selector("#goods-nav-base > div:nth-child(3) > input").send_keys("SKII神仙水")
        # 商品型号
        driver.find_element_by_css_selector("#goods-nav-base > div:nth-child(4) > input").send_keys("SKII神仙水")
        # 商品分类
        category_id_select = driver.find_element_by_name("category_id")
        driver.execute_script("arguments[0].style.display='block';", category_id_select)
        Select(category_id_select).select_by_value("488")
        # 品牌
        brand_select = driver.find_element_by_name("brand_id")
        driver.execute_script("arguments[0].style.display='block';", brand_select)
        Select(brand_select).select_by_value("2")
        # 生产地
        place_origin_select = driver.find_element_by_name("place_origin")
        driver.execute_script("arguments[0].style.display='block';", place_origin_select)
        Select(place_origin_select).select_by_value("3")
        # 库存单位
        driver.find_element_by_name("inventory_unit").send_keys("JD")
        # 积分
        driver.execute_script("arguments[0].value=''", driver.find_element_by_name("give_integral"))
        driver.find_element_by_name("give_integral").send_keys('10')

        driver.execute_script("arguments[0].value=''", driver.find_element_by_name("buy_min_number"))
        driver.find_element_by_name("buy_min_number").send_keys('1')
        # 上传图片
        driver.find_element_by_css_selector("#goods-nav-base > div.am-form-group.am-form-file > div").click()
        driver.switch_to.frame(driver.find_element_by_id("edui325_iframe"))
        driver.find_element_by_css_selector("#rt_rt_1f6jsduo0mml1plj1f53qgeq391 > label").send_keys("D:\08learn\autoTest\img\main1.jpg")



if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://10.1.60.83/mtx/admin.php?s=/admin/logininfo.html")
    driver.maximize_window()
    mtx = MTX(driver)
    # mtx.login()
    mtx.cookie_login()
    driver.get("http://10.1.60.83/mtx/admin.php?s=/index/index.html")
    # mtx.add_user()
    mtx.add_goods()
    sleep(2)
    # driver.quit()

