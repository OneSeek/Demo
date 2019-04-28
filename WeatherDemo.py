#encoding:utf-8
from bs4 import BeautifulSoup as bs
from urllib import request
import json
resp = request.urlopen("http://www.weather.com.cn/weather/101010100.shtml")
htm = resp.read().decode("utf-8")
#print(htm)
htmsoup = bs(htm, "lxml")
divsoup = htmsoup.find("div", id="7d")
ulsoup = divsoup.find("ul", class_="t clearfix")
#print(ulsoup)
lisoups = ulsoup.findAll("li")
'''
with open("D:/weatherdata.txt","w") as f:
    for li in lisoups:
        day=li.h1.text
        wea=li.select("p[class='wea']")[0].text
        weavals=li.find("p",class_="tem").text.strip()
        fl = li.find("p", class_="win").text.strip()
        f.write("时间：%s\t天气：%s\t温度：%s\t风力：%s\n" % (day,wea,weavals,fl))
'''
hours = divsoup.find("script").text.strip()[14:]
jsonobj = json.loads(hours)
d7obj = jsonobj["7d"]
#print(d7obj)
for ds in d7obj:
    for hs in ds:
        arr = hs.split(",")
        print("时间：%s\t天气：%s\t温度：%s\t风向：%s\t风力：%s\n" % (arr[0],arr[2],arr[3],arr[4],arr[5]))

