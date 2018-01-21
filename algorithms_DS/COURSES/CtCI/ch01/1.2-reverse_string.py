# Implement a function void reverse(char* str) in C or C++
# which reverses a null-terminated string.

def rec_rev(tmp):
    if len(tmp) == 0:
        return ''
    return rec_rev(tmp[1:]) + tmp[0]

assert rec_rev('abcde') == 'edcba'
assert rec_rev('andds') == 'sddna'
