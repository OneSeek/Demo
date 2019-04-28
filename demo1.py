import requests
import xlwt
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Host': 'movie.douban.com'
}
movie_list = []
director_list = []
time_list = []
star_list = []
for i in range(0, 10):
    link = 'https://movie.douban.com/top250?start=' + str(i * 25)
    res = requests.get(link, headers=headers, timeout=10)

    soup = BeautifulSoup(res.text, "lxml")
    div_list = soup.find_all('div', class_='hd')
    div1_list = soup.find_all('div', class_='bd')
    div2_list = soup.find_all('div', class_='star')

    for each in div_list:
        movie = each.a.span.text.strip()
        print(movie)
        movie_list.append(movie)

    for each in div1_list:
        info = each.p.text.strip()
        if len(info) < 3:
            continue
        time_start = info.find('20')
        if time_start < 0:
            time_start = info.find('19')
        end = info.find('...')
        time = info[end + 32:end + 36]
        time_list.append(time)

        end = info.find('主')
        director = info[4:end - 3]
        director_list.append(director)

    for each in div2_list:
        info = each.text.strip()
        star = info[0:3]
        star_list.append(star)

file = xlwt.Workbook()

table = file.add_sheet('sheet name')

table.write(0, 0, "排名")
table.write(0, 1, "电影")
table.write(0, 2, "时间")
table.write(0, 3, "导演")
table.write(0, 4, "评分")
for i in range(len(star_list)):
    table.write(i + 1, 0, i + 1)
    table.write(i + 1, 1, movie_list[i])
    table.write(i + 1, 2, time_list[i])
    table.write(i + 1, 3, director_list[i])
    table.write(i + 1, 4, star_list[i])

    # print("名称：%s"%movie_list[i])
    # print("时间：%s" % time_list[i])
    # print("导演：%s" % director_list[i])
    # print("评分：%s" % star_list[i])
    # print()
    # print()

file.save('data.xls')
