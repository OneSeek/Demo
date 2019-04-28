#encoding:utf-8

a=[15,15,2,6,7,3,3.14,"aa",True,[1,3]]
print(a)
a.append(20) #在列表的最后添加元素
a.insert(1,[5,4]) #在指定索引位置插入元素
a.pop(7)  #删除指定索引位置的元素
print(a,a[1][1],len(a),4 in a[1])
'''
for i in range(0,len(a)):
    print(a[i])

for t in a:
    print(t)
'''
lst=[45,7,23,4,1,5,89]
#lst.sort(reverse=True)
lst[4]=100  #根据索引修改元素
#lst[7]=21
print(lst,len(lst))
lst=[]  #声明一个空列表
print(bool(lst))
lst.append(45)
lst.append(57)
print(lst)
lst=[[2,3],[7,8],[4,5]]






