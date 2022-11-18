import itertools
subject=['I','You']
verb=['Play','Love']
object=['Hockey','Football']
a=(itertools.product(subject,verb,object))
for i in (a) :
    for j in i:
        print(j,sep=" ",end=" ")
    print()