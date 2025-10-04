lt=[1,2,[3,4,[5,6,7],8],9,[10,11]]

def flatten(L):
    for x in L:
        if(hasattr(x,'__iter__')):
            yield from flatten(x)
        else:
            yield x


k=flatten(lt)
kl=list(k)
print(kl)