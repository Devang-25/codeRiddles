# http://www.pythonchallenge.com/pc/return/sequence.txt
# http://www.pythonchallenge.com/pc/return/bull.html

a = [1, 11, 21, 1211, 111221]

# eg: define function to sum up the digits of 1211
z = lambda x: sum([int(i) for i in list(str(x))])

print(a)
print([z(i) for i in a])
# [1, 11, 21, 1211, 111221]
# [1, 2, 3, 5, 8]

# this is a fibonacci

# so we need to write a convertor for fibonacci digit 

# judging by the pattern, next number is series is
# divide latest by 2 (length wise). Let's say it's 1211.
# Then divide by 2, we get -> 12 and 11.
# Now append first half to second half, i.e,
# (symmetrically reverse the divided substrings). So we get:
# 11 and 12
# Now concatenate latest-1 index to this. We get 11 12 21

# Here, latest -> 1211 and latest-1'th number is -> 21

# # latest => a[-1]
# # latest -1 => a[-2]

# # so dry run gives the next number to be -> 2211111211 (adds upto 13)


# # of course since the quesiton only cares about the length, all we gotta 
# # do is find the 30th number.

# # 2 ways to do this: either iterative, or mathematically.


def find_next(a,b):
    b = str(b)
    a = str(a)
    l = len(b)
    return b[l//2:] + b[:l//2] + a

# https://en.wikipedia.org/wiki/Look-and-say_sequence
def find_next_cuckoo_egg(item):
    item = list(str(item))
    last = item.pop(0)
    c=1
    new = ''
    while item:
        # print(item)
        curr = item.pop(0)
        if curr == last:
            c += 1
        else:
            new += str(c)
            new += last
            last = curr
            c = 1
    new += str(c)
    new += last

    return new


# while(len(a) <= 30):
#     a.append(find_next(a[-2], a[-1]))

while(len(a) <= 30):
    a.append(find_next_cuckoo_egg(a[-1]))

print(len(a[30]))

# http://users.monash.edu/~normd/documents/Constant-Curiosity-Melbourne.pdf
