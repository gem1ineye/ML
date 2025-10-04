import itertools as it 
lst=['A','B','C','D']

params=it.permutations(lst,4)

params_lst=list(params)

for t in params_lst:
    print(t)