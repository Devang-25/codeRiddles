nums = range(2, int(raw_input("Enter range limit: ")))
for i in range(2, 8): 
    nums = filter(lambda x: x == i or x % i, nums)
print nums
