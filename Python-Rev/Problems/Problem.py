l1=list()

for i in range(0,7):
    x=int(input(f"Enter hours for Day {i}"))
    l1.append(x)

wages=int(input("Enter the wage for Per hour"))

sum=0
hrs=0
for i in range(0,7):
    if(i!=5 and i!=6):
        hrs=hrs+l1[i]
    else:
     sum=sum+(l1[i]*wages*1.5)


if(hrs>40):
    hrs=hrs-40
    sum=sum+(40*wages)
    sum=sum+(hrs*wages*1.5)
else:
    sum=sum+(40*wages)
    

print("Your income for this is week is",sum)
 