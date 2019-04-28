a="Hello world,Mark"
print(a[a.find("world"):(a.find("world")+5)])
a="how do you do"
print(a.replace(" ","*"))
print("*".join(a.split(" ")))
print(" Good night,Tom  ".strip())
'''
a="Hello World"
b="http://www.baidu.com"
a="Tom"
b=21
c="boy"
d=75.45
print("姓名："+a+"    年龄:"+str(b)+"   性别："+c+"   体重："+str(d))
print("姓名：%s     年龄:%d     性别：%s     体重：%.1f" % (a,b,c,d))

a=["where","are","you"]
print(" ".join(a))
'''

#print(b[11:16],b[:4],b[17:],b[:],b[::-1],b[-3:])
#print(a.replace("o","e"))
#print(a.upper(),a,a.lower()) #upper()将字符串全部转换为大写.lower()将字符串全部转换为小写
#print(len(a),b.startswith("https"),b.endswith("com"))
#print("baiduw" in b)
#print(len(b),b.index("baidu")) #如果能找到则返回字符串在父字符串中的索引位置，否则报错
#print(len(b),b.find("baiduw"))#如果能找到则返回字符串在父字符串中的索引位置，否则返回-1
'''
b="how do you do"
c=b.split(" ")
c="****hello world****"
#print("["+c.strip("*")+"]")
'''




