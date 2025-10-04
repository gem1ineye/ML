user=['john','bob','alex','alex','bob']

dic=dict()

for i in user:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i] +=1

print(dic)