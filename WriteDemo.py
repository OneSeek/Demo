#encoding:utf-8
'''
with open("D:/welcome.txt",'a',encoding="utf-8") as f:
    f.write("山东泰安欢迎您\n")
    f.write("山东农业大学欢迎您")
'''
with open("D:/五岳至尊.jpg",'rb') as f:
    img=f.read()
    with open("../img/五岳至尊.jpg","wb") as f2:
        f2.write(img)







