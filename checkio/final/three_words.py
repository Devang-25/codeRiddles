import re 
 
def checkio(words):
    ''' to distinguish words and numbers.'''
    pattern = re.compile('[a-z][\d]', re.IGNORECASE)
    assert pattern.findall(words) == []    
    # No Mixed (i.e., letters+digits) words were found
    count = 0 #for counting of patterns
    for word in words.split():
        # If it continues to be pure letters, then count+1, else count=0
        count +=1 if word.isalpha() else -count
        if count==3:
            #break out if target achieved
            return True
    # control still here? means, no such pattern found
    return False
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
