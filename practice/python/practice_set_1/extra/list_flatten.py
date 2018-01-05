def flatten(L):
  if L==[]:
    return []
  elif isinstance(L[0],list):
     return flatten(L[0])+flatten(L[1:])
  else:
     return L[:1]+flatten(L[1:])

assert flatten([1,[2,3],4,])== [1,2,3,4,]
assert flatten([2, 1, [3, [4, 5], 6], 7, [8]]) == [2, 1, 3, 4, 5, 6, 7, 8]

