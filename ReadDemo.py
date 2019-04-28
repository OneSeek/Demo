#encoding:utf-8
#r表示读，w表示写，a表示追加，b表示使用二进制
with open("D:/hello.txt",'r',encoding="utf-8") as f:
    print(f.read())
