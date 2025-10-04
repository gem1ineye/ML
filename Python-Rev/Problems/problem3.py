#Rotating a List

lst=[1,2,4,5,6]

n=int(input("Enter the roatation"))

temp1=lst[0:n]

temp2=lst[n:]
rot=temp2+temp1

print(rot)
