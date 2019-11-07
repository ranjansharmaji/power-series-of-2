L=[1,2,4,8,16,32,64]
X=5
if 2**X in L:
    print('found at',L.index(2**X),'.')
else:
    print('not found')
    
L:[]
for i in range(6):
    L.append(2**i)
print(L)
