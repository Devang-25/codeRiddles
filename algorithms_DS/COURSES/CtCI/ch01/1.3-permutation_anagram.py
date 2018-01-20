# approach 1
assert sorted('dog') == sorted('god')

# approach 2
from collections import Counter

def check_anagram(a, b):
    """
    ignore spaces
    case sensitive
    """
    a1 = Counter(a.replace(' ', ''))
    a2 = Counter(b.replace(' ', ''))
    
    for k,v in a1.items():
        try:
            assert a2[k] == v
        except:
            return False
    return True
        
check_anagram('aim','mai') == True
check_anagram('Afdd ','Af d') == True
