#encoding:utf-8
from urllib import request
from bs4 import BeautifulSoup as bs
import json
headerinfo={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
url="http://dianying.nuomi.com/movie/getmovielist?pagelets[]=pageletMovielist&reqID=0&type=hot&cityId=325&pageNum=0&pageSize=10&needMovieNews=false&isHomePage=false&needSliceAdSpace=false&t=1555833069966"
req=request.Request(url,headers=headerinfo)
resp=request.urlopen(req)
jsonstr=resp.read().decode("utf-8")
jsonstr=jsonstr.strip("BigPipe.onPageletArrive(")[:-2]
jsonobj=json.loads(jsonstr)
htm=jsonobj["html"]
htmsoup=bs(htm,"lxml")
pageCount=htmsoup.find("div",id="pagerInfo")["data-pagecount"]
#print(pageCount)
pagenum=0
movielist=[]
for i in range(0,int(pageCount)):
    url = "http://dianying.nuomi.com/movie/getmovielist?pagelets[]=pageletMovielist&reqID=0&type=hot&cityId=325&pageNum="+str(pagenum)+"&pageSize=10&needMovieNews=false&isHomePage=false&needSliceAdSpace=false&t=1555833069966"
    req = request.Request(url, headers=headerinfo)
    resp = request.urlopen(req)
    jsonstr = resp.read().decode("utf-8")
    jsonstr = jsonstr.strip("BigPipe.onPageletArrive(")[:-2]
    jsonobj = json.loads(jsonstr)
    htm = jsonobj["html"]
    htmsoup = bs(htm, "lxml")
    divsoup=htmsoup.findAll("div",class_="movie-info")
    for d in divsoup:
        moviename=d.find("p",class_="movie-name").text.strip()
        moviename=moviename.replace("\n","").replace("   ","")
        pf=d.find("span",class_="num nuomi-red").text
        movieType=d.findAll("li")[0].text
        movieLong = d.findAll("li")[1].text
        movieTime = d.findAll("li")[2].text
        imgsrc=d.find("img")["src"]
        movielist.append("电影名称：%s\t电影评分：%s\t%s\t%s\t%s\t电影图片路径：%s\t\n" % (moviename,pf,movieType,movieLong,movieTime,imgsrc))
with open("files/moviedata.txt","w",encoding="utf-8") as f:
    for m in movielist:
        f.write(m)
print("执行完成")








