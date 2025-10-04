str1='paper'
str2='titlt'

flag=True

if(len(str1)!=len(str2)):
    flag=False
else:
    map1,map2={},{}
    
    for c1,c2 in zip(str1,str2):
        if(c1 not in map1):
            map1[c1]=c2
        else:
            if(map1[c1]!=c2):
                flag=False
        
        if(c2 not in map2):
            map2[c2]=c1
        else:
            if(map2[c2]!=c1):
                flag=False


print(flag)