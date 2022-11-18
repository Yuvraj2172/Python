
import itertools
a=(input())
x=itertools.groupby(a)
# s=[(len(list(j)),int(i)) for i,j in x]
# for tup in s:
#     print(tup,end=" ")
for i,j in x:
    print(tup(len(list(j)),i))