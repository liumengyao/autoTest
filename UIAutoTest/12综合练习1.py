# -*- coding: utf-8 -*-
# @Time : 2021/5/19 10:38
# @Author : Anna
# @Email : 734666093@qq.com
# @File : 12综合练习1.py
# @time :2021/05/19
# @Project : autoTest
# @Description :

from selenium import webdriver
from time import sleep
import os

'''
使用xpath表格定位方式定位表格
'''


class Table(object):
    def __init__(self, driver, table_css):
        self.driver = driver
        self.table_css = table_css

    def get_table_head_tail(self, row, column):
        css_selector = self.table_css+">tbody>tr:nth-child("+str(row)+")>th:nth-child("+str(column)+")"
        return self.driver.find_element_by_css_selector(css_selector).text

    def get_table_cell(self, row, column):

        css_selector = self.table_css+">tbody>tr:nth-child("+str(row)+")>td:nth-child("+str(column)+")"
        print(row, column, css_selector)
        return self.driver.find_element_by_css_selector(css_selector).text


# def select_table(row, column):
#     # table = driver.find_element_by_xpath('//*[@id="table"]')
#     for tmp_row in range(1, row+1):
#         for tmp_column in range(1, column+1):
#             # 第一行和最后一行需要特殊处理
#             if tmp_row == 1 or tmp_row == row:
#                 item = 'th'
#             else:
#                 item = 'td'
#             print(driver.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(tmp_row)+']/'+item+'['+str(tmp_column)+']').text)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    filePath = os.path.abspath('testtable.html').replace('UIAutoTest', 'TestFiles')
    driver.get(filePath)
    table = Table(driver, "#table")

    for i in range(2, 4):
        sum = 0
        for j in range(2, 5):
            sum +=int(table.get_table_cell(j, i))
        if sum !=int(table.get_table_head_tail(5, i)):
            print("第%d列，表格中的总计为：%s，实际应该是：%d" % (i, table.get_table_head_tail(5, i), sum))


    # select_table(5, 3)
    # # 分别计算表格中2,3列的第2,3,4行的总和，分别与2,3列的第5行做比较，若不相等则输出相关信息
    driver.quit()
