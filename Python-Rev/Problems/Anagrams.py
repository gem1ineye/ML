s1='snooze alarms'
s2="alas , no more Z's  " 

s1=s1.lower()
s2=s2.lower()

for x in s1:
    if x.isalpha():
        if s1.count(x) != s2.count(x):
            print('not anagrams')
            break
else:
    print('Anagrams')
    

# This is for else loop here when for-loop is completed successfully else 
# is work if some how for loop is uncompleted due to reason like break else part didn't work


class a:
    def __init__(self,name):
        self.name=name
    
obj=a('kamina')

print(obj.name)