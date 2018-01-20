def check_unique(ip):
    # make sure if it is just ASCII we're dealing wiht
    # then make a table with index as ASCII number itself
    # then update that with True for every char encountered.
    # if already True, string is not unique
    char_set = [False for _ in range(128)]
    for i in ip:
        if char_set[ord(i)]:
            return False
        char_set[ord(i)] = True
        
    return True

def check_unique_optimized(ip):
    '''
    - Use bit vector to compare 2 numbers. Init checker = 0000000
    - For every char found in a-z, left shift 
      by parity. Example:
        parity of a -> 0, b -> 1, c -> 2, etc..
    - Keep a checker updated with OR operation of 
      current left shifted val and last checker value
    - Compare: checker AND left shifted value of current val (i.e, 1<<val)
    - If result is greater than 1, it means we've just AND'ed 1 & 1 somewhere in the 
      bit vector, meaning somewhere in the past, checker was updated at that position
      for a character that was just encountered, hence given string is not unique.
    '''
    # checker        -- 00000
    # val ('a')      -- 00010
    # & = 00000
    
    # checker        -- 00010
    # val ('b')      -- 00100
    # & = 00000
    
    # checker        -- 00110
    # val ('a')      -- 00010
    # & = 00010 --> gt 1
    
    checker = 0
    for current in ip:
        val = ord(current) - ord('a')

        print("\n...compare & for: ")
        print("{0:b}".format(checker))
        print("{0:b}".format(1 << val))

        check_val = checker & (1 << val)
        if (check_val > 0):
            print("..NOT UNIQUE\n")
            return False
        checker |= (1 << val)
    return True

assert check_unique('Ab3kc0A') == False
assert check_unique('abc') == True

# works only for a-z
assert check_unique_optimized('abkca') == False
assert check_unique_optimized('abc') == True

# ...compare & for: 
# 0
# 1

# ...compare & for: 
# 1
# 10

# ...compare & for: 
# 11
# 10000000000

# ...compare & for: 
# 10000000011
# 100

# ...compare & for: 
# 10000000111
# 1
# ..NOT UNIQUE


# ...compare & for: 
# 0
# 1

# ...compare & for: 
# 1
# 10

# ...compare & for: 
# 11
# 100
