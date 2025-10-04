original={
    'a':1,
    'b':2,
    'c':1,
    'd':2,
    'e':3,
    'f':2
}

inverted=dict()

for keys,item in original.items():
    if(item not in inverted):
        inverted[item]={keys,}
    else:
        inverted[item]=inverted[item] | {keys}

print(inverted)