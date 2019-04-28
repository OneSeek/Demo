#encoding:utf-8

lst = ['bajie ', 'axlzC', ' AbC ', '  gsssq  ', '  bobo  ', ' dongdong ', ' aqc']
newlst=[]

for a in lst:
    a=a.strip()
    #print(a)
    if a.endswith("c") and a.lower().startswith("a"):
        newlst.append(a)
#print(newlst)
lst = [11, 22, 33, 44, 55, 77, 88, 99, 90]
dic={"大于等于66的值":[],"小于66的值":[]}
for a in lst:
    if a>=66:
        dic["大于等于66的值"].append(a)
    else:
        dic["小于66的值"].append(a)
#print(dic)
dic = {'k1': 'v1', 'k2': ['sb', 'aa'], (1, 2, 3, 4, 5): {'k3': ['2', 100, 'wer']}}
print(dic)
dic["k2"].append(33)
print(dic)
dic["k2"].insert(0,"s")
print(dic)
dic[(1,2,3,4,5)]["k4"]="v4"
print(dic)
dic[(1,2,3,4)]={(1,2,3):"ok"}
print(dic)
dic[(1,2,3,4,5)]["k3"][2]="qq"
print(dic)

