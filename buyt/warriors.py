image = []
dim = int(raw_input())

for i in xrange(dim):
    image.append(list(raw_input()))

track = [[0]*dim]*dim
tmp = []

for i in xrange(dim):
    for j in xrange(dim):
        if [i,j] in tmp:
            continue
        else:
            c = 0
            if image[i][j] == 1:
                tmp.append([i,j])
                c+=1
            if image[i+1][j] == 1:
                tmp.append([i+1,j])
                c+=1
            if image[i][j+1] == 1:
                tmp.append([i,j+1])
                c+=1
            if image[i+1][j+1] == 1:
                tmp.append([i+1,j+1])
                c+=1
            
