#encoding:utf-8
'''
for i in range(0,11,2):
    print(i)
    #if i%2==0:
    #    print(i)
'''
"""
for x in range(1,6):
    for y in range(2,5):
        print(x,y)

a=0
while a<10:
    print(a)
    a+=1  #a=a+1


a=0
sum=0
while a<10:
    sum+=a  #sum=sum+a
    print(a,sum)
    a+=1
print(sum)

sum=0
for a in range(0,10):
    sum+=a
print(sum)

for i in range(1,101):
    if i%2!=0:
        print(i)

count=0
for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if x!=y and x!=z and y!=z:
                print(x*100+y*10+z)
                count+=1
print("count=%d" % count)
"""
a=12345
r=0
while a:
    b=a%10
    r=r*10+b
    a//=10
    print(a,b,r)