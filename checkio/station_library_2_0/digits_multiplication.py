# python 3
from functools import reduce

def checkio(number):
    number = map(int, list(str(number)))
    number = [y for y in number if y != 0]
    return reduce(lambda x, y: x*y, number)
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

