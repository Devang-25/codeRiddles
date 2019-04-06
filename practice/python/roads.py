import json
from pprint import pprint
from collections import defaultdict
# class Node(object):
#     def __init__(self, label):
#         self.label = label
#         self.neighbours = []
        
#     def add_path(self, b):
#         self.neighbours.append(b)

#     def __str__(self):
#         return self.label

        
class CityPlanner:

    def __init__(self, points):
        self.points = points
        self.paths = defaultdict(list)
    
    def build_road(self, a, b):
        # if a not in self.paths:
        #     # self.paths.append(Node(a))
        #     self.paths[a] = []
        self.paths[a].append(b)
            
    def exists(self, a, b):
        # 0/1
        if b in self.paths[a]:
            return 1
        else:
            for i in self.paths[a]:
                if self.exists(i, b) is 1:
                    return 1
            return 0

    
# def __str__(self):
#     # return json.dumps(self.paths)
#     pprint(self.paths)

cp = CityPlanner(10)

cp.build_road(0, 1)
cp.build_road(0, 2)
cp.build_road(1, 2)
cp.build_road(2, 4)
cp.build_road(3, 5)
cp.build_road(5, 6)
cp.build_road(4, 6)
cp.build_road(2,7)

pprint(dict(cp.paths))

print(cp.exists(0, 5))
print(cp.exists(0,6))
print(cp.exists(0,7))
