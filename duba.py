import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Host': 'http://v.duba.com'
}
# # 电影名称，主演，类型，地区，年代，电影描述，电影图片路径等
# Movie title, starring, type, region, age, movie description, movie picture path
movie_title_list = []
starring_list = []
type_list = []
region_list = []
age_list = []
movie_description_list = []
movie_picture_path = []
for i in range(0, 67):
    link = 'http://v.duba.com/movie/list/filter-true+complete-%E6%AD%A3%E7%89%87+order-pubtime+pn-' \
           + str(i) + '+channel-movie'
    res = requests.get(link, headers=headers, timeout=10)
    print(res.text)
    # htmsoup = BeautifulSoup(htm, "lxml")

