# set(5,12)
# set(2,3)

# get(5)
# 12

# set(6,9)
# pushes out 5 (recently accessed)

# get(5)
# -1

# get(6)
# 9

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        self.recent = None

    def set(self, key, value):
        if len(self.store) == self.capacity:
            self.store.pop(self.recent[-1])
        self.store[key] = value

    def get(self, key):
        return self.store.get(key, -1)
