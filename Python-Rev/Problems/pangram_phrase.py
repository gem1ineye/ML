import re

def pangrams(phrase):
    letters=re.sub(r'[^a-zA-Z]','',phrase)
    letter_set=set(letters.lower())
    
    if(len(letter_set)==26):
        return True
    else:
        return False

    
    