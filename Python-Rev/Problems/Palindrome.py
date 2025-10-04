s1=input("Enter the String")

s1=s1.replace(' ','')
s1=s1.lower()

s2=s1[-1::-1]
if(s1==s2):
    print("Its alredy palindrome")
else:
    s1=s1+s2
    print(s1)