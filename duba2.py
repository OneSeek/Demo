#!/usr/bin/python
#coding=utf-8

"""
start python 项目
"""
import time

from bs4 import BeautifulSoup
from lxml import etree

from selenium import webdriver


def get_html(url):

    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(executable_path='D:\Downloads\chromedriver_win32\chromedriver.exe'
                                   , options=chrome_options)

        # Get local session of firefox
        browser.get(url)
        # Load page
        # print(browser.page_source)
        html = browser.page_source

    except Exception as e :
        print('获取源代码失败：%s' % e)

    return html


if __name__ == '__main__':
    url = "http://v.duba.com/movie/list/filter-true+complete-%E6%AD%A3%E7%89%87+order-pubtime+pn-1+channel-movie"
    html = get_html(url)
    soup = BeautifulSoup(html, "lxml")

    selector = etree.HTML(html)

    divs = selector.xpath('//*[@id="bd-video-list"]')

    for div in divs:
        movieName = div.xpath('li[1]/div[3]/h4/a/@href')
        print(movieName)







