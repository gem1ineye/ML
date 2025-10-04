'''
m1=[]
m1p=[]

for i in range(4):
    val1=input("Enter the menu name")
    val2=input("Enter the menu price")
    m1.append(val1)
    m1p.append(val2)



for i in range(4):
    print(m1[i], '-'*(20-len(m1[i])-len(m1p[i])),m1p[i])
    
'''

card_num = input("Enter card number")  
val = card_num[12:16]  # slicing from index 13 to 16
print(val)
