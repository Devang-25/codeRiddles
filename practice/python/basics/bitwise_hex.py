#!/bin/env python3

print(5)

# decimal to binary
in_binary = "{0:08b}".format(5)
print(in_binary)

# binary to decimal
in_decimal = int(in_binary, 2)
print(in_decimal)

# left shift
print("{0:08b}".format(5 << 1))
print(5 << 1)

# right shift
print("{0:08b}".format(5 >> 1))
print(5 >> 1)

# 2s compliment of N is -(N+1)
print(~44) # -45
print(~-44) #  43

# AND
print(3 & 4)
# In [16]: "{0:08b}".format(3)
# Out[16]: '00000011'
# In [17]: "{0:08b}".format(4)
# Out[17]: '00000100'
#
# In [20]: "{0:08b}".format(3 & 4)
# Out[20]: '00000000'

# OR 
print(3 | 4)
# In [16]: "{0:08b}".format(3)
# Out[16]: '00000011'
# In [17]: "{0:08b}".format(4)
# Out[17]: '00000100'
#
# In [19]: "{0:08b}".format(7)
# Out[19]: '00000111'

print(hex(16)) # 0x10


print(hex(42))
# In [42]: print(hex(42))
# 0x2a

##################################################################
# # hex() can't be consumed by bin() which requires int type
# In [62]: int(bin(hex(42)),2)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-62-0f65357f76a6> in <module>()
# ----> 1 int(bin(hex(42)),2)

# TypeError: 'str' object cannot be interpreted as an integer
###############################################################
# HEX -> DECIMAL -> BINARY -> DECIMAL

print(int(bin(int(hex(42), 16)), 2))
# In [75]: int(bin(int(hex(42), 16)), 2)
# Out[75]: 42
# 0. supply int [base 2] as input to hex()
# 1. convert output of hex() to int [base 16]
# 2. convert int [base 16] to binary
# 3. convert binary to int with base 2

# bin(0x2a) works
# bin('0x2a') doesn't work
# hex() gives '0x2a' not 0x2a
# hence the above conversions needed

###############
# In [80]: hex(42)
# Out[80]: '0x2a'

# In [81]: int(hex(42), 16)
# Out[81]: 42

# In [82]: bin(int(hex(42), 16))
# Out[82]: '0b101010'

# In [83]: int(bin(int(hex(42), 16)),2)
# Out[83]: 42

#################################################################
# hex to bin requires int, not str as opposed to output of hex() which is str
# In [40]: bin(0x2a)
# Out[40]: '0b101010'

# In [41]: int('101010',2)
# Out[41]: 42

# In [43]: int(bin(0x2a),2)
# Out[43]: 42

# In [60]: int(hex(42), 16)
# Out[60]: 42

#################################################################
# In [71]: int(hex(42))
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# <ipython-input-71-7c0e62e2f758> in <module>()
# ----> 1 int(hex(42))

# ValueError: invalid literal for int() with base 10: '0x2a'
##################################################################

# supply a base 16 for hex
# In [72]: int(hex(42), 16)
# Out[72]: 42

##################################################################
