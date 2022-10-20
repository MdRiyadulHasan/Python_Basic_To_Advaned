from collections import defaultdict
d=defaultdict(int)
L=[1,2,3,4,2,4,1,2,3,1,4,2,1,2,1,2,3]
for i in L:
    d[i]=d[i]+1
print(d)