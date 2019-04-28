import requests
from bs4 import BeautifulSoup
from lxml import etree



def get_movie(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}

    try:
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            print('成功获取源代码')
            # print(html.text)
    except Exception as e:
        print('获取源代码失败：%s' % e)

    return html.text


if __name__ == '__main__':

    movie_html = get_movie("http://v.duba.com/dianying/137326.htm")
    soup = BeautifulSoup(movie_html, "lxml")

    imageUrl = soup.find("img", "info-poster")
    print(imageUrl["src"])


