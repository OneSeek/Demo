#encoding:utf-8
#键值对 key:value
d={"zhangsan":89,"lisi":70,"wangwu":90}
d["xiaoming"]=97
d["lisi"]=80  #如果key已经存在则进行覆盖，否则添加键值对
d.pop("wangwu")  #根据key值进行删除键值对操作
print(d)
print(d["lisi"],d.get("lisi"))
print(d.get("xiaobai"))  #如果key不存在则返回None，否则返回key所对应的value值
#print(d["xiaobai"])  #如果key不存在则报错，否则返回key所对应的value值

for a in d:
    print(a,d[a])

print("-----------")
for t in d.items():
    print(t[0],t[1])

#t=("zhangsan",89)
dic={}
dic["aa"]=56
dic[34]="df"
dic[4.5]=4.23
dic[(1,2,3)]=["dd",56]
print(bool(dic),dic)


