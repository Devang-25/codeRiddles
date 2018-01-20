'''
2. Form higher number using digits of number
Give a number, find a next higher number using same digits.

1234 -> 1243
4132-> 4213
4321-> None
32876->36278
32841->34128

'''


def get_higher(num):
    """
    The approach is to convert the number to string,
    then start from 2nd last digit and move up until the MSB is found.
    In the process, see if the reversed subset of digits are greater than the current subset
    (we start from -2 index and do a loop until sum of i and len(num) form -1 (0 indexed search)
    Example:
    - 1234 -> compare '34' to '43', if found higher, return the higher number
    - 1154 -> compare '54' to '45', not greater, so decrease i by 1.
              compare '154' to '451', found greater, return 1451

    we're assuming to no re use any digit.

    possible edge case: repetitive digits
    """
    """
    Wouldn't this return the highest number?
    @ highest for 1154 would then be 5411. the current solution return 1451. (oh this should be 1415) @exactly. Yeah logic is wrong
    Let me get back to this problem after solving 1st to see if i missed a logic.

    @ Okay.
    """bl
    i = -2
    num = str(num)
    while i + len(num) != -1:
        tmp = num[i:]
        if tmp[::-1] > tmp:
            return int(num[:i] + tmp[::-1])
        else:
            i -= 1
    return None

assert get_higher(1251) == 1521
assert get_higher(1154) == 1451
assert get_higher(1234) == 1243
assert get_higher(12) == 21
assert get_higher(21) == None
