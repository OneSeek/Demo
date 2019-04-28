
import re

import requests
import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver


def get_movie(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}

    try:
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        # print(html.text)
    except Exception as e:
        print('获取源代码失败：%s' % e)

    return html.text


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

    except Exception as e:
        print('获取源代码失败：%s' % e)

    return html


def to_str(tag):
    line1 = soup.select(tag)
    line2 = str(line1)
    m = re.sub("[A-Za-z0-9\!\%\[\]\,\。\<\>\=\"\/\+\-\_]", "", line2)
    return m


if __name__ == '__main__':

    movie_title_list = []
    starring_list = []
    type_list = []
    region_list = []
    years_list = []
    movie_description_list = []
    imageUrl_list = []

    for i in range(1, 3):  # range(1, 68) 1到67页
        try:
            url = "http://v.duba.com/movie/list/filter-true+" \
                  "complete-%E6%AD%A3%E7%89%87+order-pubtime+pn-"+str(i)+"+channel-movie"
            html = get_html(url)
            soup = BeautifulSoup(html, "lxml")
            # list = soup.select('.bd-video-list')
            # print(list)

            # links = soup.find_all('a')
            # i = 0
            # for link in links:
            #     print(i)
            #     i = i + 1
            #     print(link)

            soups = soup.select("body > div > div > div > ul > li > div > h4 > a")
            # 电影名称，主演，类型，地区，年代，电影描述，电影图片路径

            for a in soups:

                movie_html = get_movie("http://v.duba.com" + a["href"])

                soup = BeautifulSoup(movie_html, "lxml")

                movie_title = soup.find("span", "str-tt")
                print(movie_title.text)
                movie_title_list.append(movie_title.text)

                imageUrl = soup.find("img", "info-poster")
                try:
                    imageUrl_ = imageUrl['src']
                except Exception as e:
                    print(imageUrl)
                    print(imageUrl_)
                    print('imageUrl异常：%s' % e)
                imageUrl_list.append(imageUrl_)

                movie_description = to_str('.j-data-intro')
                # print(movie_description)
                movie_description_list.append(movie_description)

                type_ = to_str(".sp-apend-line")
                # print(type_)
                type_list.append(type_)

                # region = to_str(".intro-area")
                # # print(region)
                # region_list.append(region)
                try:
                    region = soup.find("a", class_="intro-area")
                    region_list.append(region.text)
                except Exception as e:
                    print(movie_title.text)
                    region = to_str("intro-area-disable")
                    region_list.append(region)

                # years = soup.select(".str-year")
                # years_ = str(years)
                # m = re.sub("[A-Za-z\!\%\[\]\,\。\<\>\=\"\/\-]", "", years_)
                # # print(m)
                # years_list.append(m)
                years = soup.find("span", class_="str-year")
                years_list.append(years.text)

                starring = soup.find_all("a", class_="intro-role")
                starring_ = ""
                for each in starring:
                    starring_ = starring_ + each.text + " "
                #     print(starring)
                # print(starring_)
                starring_list.append(starring_)
        except Exception as e:
            print(movie_title.text+"获取异常")
            print(e)
# 电影名称，主演，类型，地区，年代，电影描述，电影图片路径
file = xlwt.Workbook()

table = file.add_sheet('sheet name')

table.write(0, 0, "序号")
table.write(0, 1, "电影名称")
table.write(0, 2, "主演")
table.write(0, 3, "类型")
table.write(0, 4, "地区")
table.write(0, 5, "年代")
table.write(0, 6, "电影描述")
table.write(0, 7, "电影图片路径")

for i in range(len(movie_title_list)):
    table.write(i + 1, 0, i + 1)
    table.write(i + 1, 1, movie_title_list[i])
    table.write(i + 1, 2, starring_list[i])
    table.write(i + 1, 3, type_list[i])
    table.write(i + 1, 4, region_list[i])
    table.write(i + 1, 5, years_list[i])
    table.write(i + 1, 6, movie_description_list[i])
    table.write(i + 1, 7, imageUrl_list[i])

file.save('movie_data.xls')


