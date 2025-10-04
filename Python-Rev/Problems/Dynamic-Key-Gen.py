import uuid

l1=[['mouse',4000],['monitor',20000],['Headphones',20000]]

dic={}

for item in l1:
    id=uuid.uuid5(uuid.NAMESPACE_OID,item[0])
    key=id.hex[0:7]
    dic[key]=item

print(dic)