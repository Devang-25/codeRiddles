#!/usr/bin/env python3

import itertools

class MatrixPatternSearch(object):
    def __init__(self, ip_mx, word_string):
        '''
        m,n -> dimensions (rows, columns)
        '''
        self.matrix = ip_mx
        self.pattern = word_string
        self.m = len(self.matrix) # rows
        self.n = len(self.matrix[0]) # columns
        self.visited_mx = [list(itertools.repeat(0, self.m)) for x in range(self.n)]
        self.map_representation = {
                                1: (-1,-1),
                                2: (-1, 0),
                                3: (-1, 1),
                                4: (0, 1),
                                5: (1, 1),
                                6: (1, 0),
                                7: (1, -1),
                                8: (0, -1)}

    def find_nearby(self, i, j):
        '''
        @(i,j) : For current element's position:
          ->  == (row,col)

        @nearby : For current position X, nearby elements are:
          -> [1,2,3]
          -> [8,X,4]
          -> [7,6,5]
          A value of -1 would denote outside boundary [matrix dimensions]
        '''
        nearby = dict.fromkeys(range(1,9), -1)
        if i != 0:
            if j !=0:
                nearby[1] = self.matrix[i-1][j-1]
            nearby[2] = self.matrix[i-1][j]
            if j != self.n-1:
                nearby[3] = self.matrix[i-1][j+1]

        if i != self.m-1:
            if j !=0:
                nearby[7] = self.matrix[i+1][j-1]
            nearby[6] = self.matrix[i+1][j]
            if j != self.n-1:
                nearby[5] = self.matrix[i+1][j+1]

        if j != 0:
            nearby[8] = self.matrix[i][j-1]
        if j != self.n-1:
            nearby[4] = self.matrix[i][j+1]

        return nearby

    def get_coordinates(self, pos, p):
        '''
        given a set of coordinates 'pos' -> (i,j), this
        finds out the position to be traversed next,
        based on a reference 'p' from nearby elements mapping.
        '''
        mods = self.map_representation[p]
        return (pos[0]+mods[0], pos[1]+mods[1])

    def search_pattern(self, pos, word=''):
        '''
        recursively calls itself to search for pattern in
        given matrix.
        '''
        if word:
            proximity_mx = self.find_nearby(*pos)
            found_pos = []
            print("looking for pattern '%s' starting from %d,%d" %
                                        (word, pos[0], pos[1]))
            # print(proximity_mx)
            for k,v in proximity_mx.items():
                if v != -1:
                    new_pos = self.get_coordinates(pos, k)
                    # print(v, self.visited_mx[new_pos[0]][new_pos[1]])
                    if v == word[0] and \
                            self.visited_mx[new_pos[0]][new_pos[1]] == 0:
                        print("found nearby letter %s @ %d,%d" %
                                                (v, new_pos[0], new_pos[1]))
                        x = self.search_pattern(new_pos, word=word[1:])
                        if x:
                            self.visited_mx[new_pos[0]][new_pos[1]] = 1
                            return True
                        else:
                            self.visited_mx[new_pos[0]][new_pos[1]] = 0
                            return False
            # next item in pattern isn't one of 8 neighbours
            return False
        else:
            # word='' ..meaning path has been traversed to reach this point
            return True

    def initiate_search(self, flag=0, pos=None):
        '''
        searches for first element in word and if found, starts
        pattern search, else notifies of pattern not being found.
        '''
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] == self.pattern[0]:
                    print("found starting letter @ %d,%d" % (i, j))
                    pos = (i,j)
                    self.visited_mx[i][j] = 1
                    flag = 1
                    break
                else:
                    continue
            if flag:
                break
        if pos:
            if self.search_pattern(pos, word=self.pattern[1:]):
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    user_matrix = [['a','i','b','d'],
                   ['v','x','r','t'],
                   ['l','y','u','w'],
                   ['n','a','u','z']]

    # user_matrix = [list(itertools.repeat('a', 4)),
    #                list(itertools.repeat('b', 4)),
    #                list(itertools.repeat('c', 4)),
    #                list(itertools.repeat('d', 4))]    

    print("Given Matrix: ")
    [print(x) for x in user_matrix]
    user_input = input("\nEnter single word to search for: ").lower()
    MPS = MatrixPatternSearch(user_matrix, user_input)
    if MPS.initiate_search():
        print("\nPattern exists!\n")
        print("coordinates visited pattern:")
        [print(x) for x in MPS.visited_mx]
    else:
        print("\nPattern does not exist. Try another one..\n")

# violates this example for :
# Example:
# Given Matrix:
# ['a', 'a', 'a', 'a']
# ['b', 'b', 'b', 'b']
# ['c', 'c', 'c', 'c']
# ['d', 'd', 'd', 'd']

# Enter single word to search for: aabbbabccd
# found starting letter @ 0,0
# looking for pattern 'abbbabccd' starting from 0,0
# found nearby letter a @ 0,1
# looking for pattern 'bbbabccd' starting from 0,1
# found nearby letter b @ 1,2
# looking for pattern 'bbabccd' starting from 1,2
# found nearby letter b @ 1,3
# looking for pattern 'babccd' starting from 1,3
# found nearby letter b @ 1,2
# looking for pattern 'abccd' starting from 1,2
# found nearby letter a @ 0,1
# looking for pattern 'bccd' starting from 0,1
# found nearby letter b @ 1,2
# looking for pattern 'ccd' starting from 1,2
# found nearby letter c @ 2,3
# looking for pattern 'cd' starting from 2,3
# found nearby letter c @ 2,2
# looking for pattern 'd' starting from 2,2
# found nearby letter d @ 3,3

# Pattern exists!

# coordinates visited pattern:
# [1, 1, 0, 0]
# [0, 0, 1, 1]
# [0, 0, 1, 1]
# [0, 0, 0, 1]
