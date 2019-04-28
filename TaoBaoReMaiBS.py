#encoding:utf-8
from bs4 import BeautifulSoup
from urllib import request
import os
headerinfo={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
url="https://mosaic.re.taobao.com/search?clk1=&p4pTags=&ismall=&buckid=&refpos=&refpid=mm_14507511_3485205_11375261&keyword=%E7%94%B7%E9%9E%8B&_input_charset=utf-8&isinner=0"
req=request.Request(url,headers=headerinfo)
resp=request.urlopen(req)
htm=resp.read().decode("utf-8")
#print(htm)
htmsoup=BeautifulSoup(htm,"lxml")
divsoup=htmsoup.find("div",id="J_waterfallWrapper")
items=divsoup.select("div[class='item']",limit=10)
for t in items:
    price=t.select("span[class='pricedetail']")[0].text
    title=t.select("span[class='title']")[0].text
    imgurl=t.img["data-ks-lazyload"]
    imgname=os.path.basename(imgurl)
    imgresp = request.urlopen(imgurl)
    imgs=imgresp.read()
    with open("../img/"+imgname,'wb') as f:
        f.write(imgs)

    print(title,price,imgurl)











