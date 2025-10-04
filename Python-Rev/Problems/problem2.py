l1=input('Enter the elements')

l1=l1.split()

ele=[int(x) for x in l1]

res=[]

for i in ele:
    if(i not in res):
        res.append(i)

print(ele)
print(res)