from bs4 import BeautifulSoup

htm = '''

<!DOCTYPE html>
<html>
    <head>
          <title>国内外海量热门电影大全。高清、流畅大片免费看</title>
          <meta name='keywords' id="bbb" content='免费电影，在线观看，在线看电影，热播大片，高清电影，高分大片' />
          <meta name="description" id="aaa" content="金山电影大全--国内外海量免费高清热门电影大全。高清、流畅大片免费看" />
    </head>
    <body>
         <div class="area area-last area4"> 
            <div class="inner"> 
                <h3>热搜</h3> 
                <input type="text" class="yhm" name="yhm" id="yhmid" value="wwww"/>
                <input type="text" class="tel" name="tel" id="telid" value="dddd"/>
                <a href="http://v.baidu.com/movie/128212.html" target="_blank" class="title" static="stp=ti">妖猫传</a>
                <a href="http://v.baidu.com/movie/128212.html" target="_blank" class="sub-title" static="stp=ti">张雨绮变最美猫妖</a>
                <div class="links"> 
                     <a href="http://v.duba.com/dianying/135770.htm" target="_blank">无名之辈</a> 
                     <a href="http://v.duba.com/dianying/135509.htm" target="_blank">无双</a> 
                     <a href="http://v.duba.com/dianying/117164.htm" target="_blank">狗十三</a> 
                     <a href="http://v.duba.com/dianying/134804.htm" target="_blank">爱情公寓</a> 
                     <a href="http://v.duba.com/dianying/133893.htm" target="_blank">复仇者联盟3(无限战争)</a> 
                     <a href="http://v.duba.com/dianying/135511.htm" target="_blank">悲伤逆流成河</a> 
                </div> 
            </div>
            <div class="price fr"> 
                <p class="seat"><em class="dollar">￥</em><em class="num">87</em>起</p> 
            </div> 
         </div>
    </body>
</html>

'''

htmsoup = BeautifulSoup(htm, "lxml")
asoups=htmsoup.select("div[class='links'] a")
# asoups=htmsoup.select("body > div > div > div > a")

# inputsoups = htmsoup.select("#yhmid")[0]
# print(inputsoups)
# asoups = htmsoup.select(".links a")

for a in asoups:
    textval = a.text
    hrefval = a["href"]
    print(textval, hrefval)

'''
print(htmsoup.title.string)
print(htmsoup.title.text)

print(htmsoup.p.string)
print(htmsoup.p.text)
print(htmsoup.meta.get("content"))
print(htmsoup.meta.attrs["content"])
print(htmsoup.meta["content"])


print(htmsoup.findAll("meta")[1]["content"])
metasoup=htmsoup.findAll("meta")[1]
print(metasoup["content"])
divsoup=htmsoup.find("div",class_="inner")
divsoup2=htmsoup.findAll("div",class_="inner")[0]
print(divsoup2)

print(htmsoup.find("input",id="telid")["value"])
print(htmsoup.find("input",{"name":"tel"})["value"])
print(htmsoup.find("input",{"class":"tel"})["value"])
asoups = htmsoup.findAll("a")
for a in asoups:
    textval=a.text
    hrefval=a["href"]
    print(textval,hrefval)

divsoup=htmsoup.find("div",{"class":"links"})
asoups=divsoup.findAll("a")
for a in asoups:
    textval=a.text
    hrefval=a["href"]
    print(textval,hrefval)
'''



