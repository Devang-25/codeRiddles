import unittest

# Given an image represented by an NxN matrix, where each pixel in the image is
# 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in
# place?

# 1   2   3   4   5
# 6   7   8   9   10
# 11  12  13  14  15
# 16  17  18  19  20
# 21  22  23  24  25
# ^.. Initial Matrix

# 21  16  11  6   1
# 22  17  12  7   2
# 23  18  13  8   3
# 24  19  14  9   4
# 25  20  15  10  5
# ^.. Final Matrix

def produce_matrix(N):
    return [list(range(i+1,i+N+1)) for i in range(0,N*N,N)]

def pprint_mat(matrix):
    '''
    pretty print a matrix
    '''
    # [print(i) for i in matrix]
    # OR better.. https://stackoverflow.com/questions/13214809/pretty-print-2d-python-list
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

def rotate_matrix(matrix):
    # O(NxN)
    '''
    To rotates a 5x5 matrix 90 degrees clockwise:
    - Step 1: Work on it layer wise. So first we have outermost
              boundary wall
    - Step 2: For shift edges of the boundary to right,
              we can start from rotating corner elements first,
              then 1 ahead. Example, just rotate following set:
                [(0,0) --> (0,4) --> (4,4) --> (4,0)]
                .. where :
                    - (0,0) is top left
                    - (0,4) is top right
                    - (4,0) is bottom left
                    - (4,4) is bottom right

    - Step 3: Do the same with following:
                [(0,1) --> (1,4) --> (4,3) --> (3,0) ]

    Pattern we then see is following for outermost layer:
    [ (0,0)   --> (0,4)    --> (4,4)       --> (4,0)      --> (0,0)   ]
    [ (0,1)   --> (1,4)    --> (4,3)       --> (3,0)      --> (0,1)   ]
    [ (0,2)   --> (2,4)    --> (4,2)       --> (2,0)      --> (0,2)   ]
    [ (0,3)   --> (3,4)    --> (4,1)       --> (1,0)      --> (0,3)   ]
    [ topleft --> topright --> bottomright --> bottomleft --> topleft ]

    - Step 4: We now need to figure out how to assign those indices
              using following variables that vary with each layer:
              limits of array -> first, last
              >> first, last = layer, N - layer - 1
                .. where layer ranges from 0 to N//2
                    (this is because in N/2 layers,
                    we'd have reached all N^2 elements)

    '''
    n = len(matrix)
    pprint_mat(matrix)
    print("^.. Initial Matrix\n")
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        # Solution approach
        # # INIT
        # topleft = matrix[layer][layer]
        # bottomleft = matrix[n-layer-1][layer]
        # bottomright = matrix[n-layer-1][n-layer-1]
        # topright = matrix[layer][n-layer-1]
        # #######
        for i in range(first, last):
            # Let's use help from dry run to decide how to assign indices..
            # ######
            # # LAYER 0 (first=0, last=4)
            # topleft     # 0,0 (i=0) || 0,1 (i=1) || 0,2 (i=2) || 0,3 (i=3)
            # bottomleft  # 4,0 (i=0) || 3,0 (i=1) || 2,0 (i=2) || 1,0 (i=3)
            # bottomright # 4,4 (i=0) || 4,3 (i=1) || 4,2 (i=2) || 4,1 (i=3)
            # topright    # 0,4 (i=0) || 1,4 (i=1) || 2,4 (i=2) || 3,4 (i=3)
            # ######
            # # LAYER 1 (first=1, last=3)
            # topleft      1,1 (i=1) || 1,2 (i=2)
            # bottomleft   3,1 (i=1) || 2,1 (i=2)
            # bottomright  3,3 (i=1) || 3,2 (i=2)
            # topright     1,3 (i=1) || 2,3 (i=2)
            # ######

            # Now modify INIT indices to accomodate above patterns.

            # tmp = top right --> [0,1,2,3][4]
            tmp = matrix[i][last]
            # top right = top left --> [0][0,1,2,3]
            matrix[i][last] = matrix[first][i]
            # top left = bottom left --> [4,3,2,1][0]
            matrix[first][i] = matrix[-i-1][first]
            # bottom left = bottom right --> [4][4,3,2,1]
            matrix[-i-1][first] = matrix[last][-i-1]
            # bottom right = tmp
            matrix[last][-i-1] = tmp
            # ######

    pprint_mat(matrix)
    print("^.. Final Matrix\n")
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6,  1],
            [22, 17, 12, 7,  2],
            [23, 18, 13, 8,  3],
            [24, 19, 14, 9,  4],
            [25, 20, 15, 10, 5]
        ]),
        (
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ], [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])
    ]

    def test_rotate_matrix(self):
        c = 0
        for [test_matrix, expected] in self.data:
            print("\nTest case %s" % (c+1))
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)
            c+=1

if __name__ == "__main__":
    unittest.main()
