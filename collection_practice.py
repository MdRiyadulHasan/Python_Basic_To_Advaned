from collections import Counter
arr=[7,2,5,3,5,3]
brr=[7,2,5,4,6,3,5,3]
a=Counter(arr)
b=Counter(brr)
c=b-a
print(c.keys())