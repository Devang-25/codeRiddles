import random

random_list = random.sample(range(random.randint(500,1000)), (random.randint(10,500)))

print(random_list)

print("Length: ", len(random_list))

# WAP..
# to find the kth smallest number in the list
# ..that works in O(nlog(n))

k = 4
print("4th smallest: ", sorted(random_list)[k])
