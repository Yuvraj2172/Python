def greater(x,y):
    while x>=y:
        yield x
        x-=1
d=list(greater(20,4))
for i in range(len(d)-1,-1,-1):
    print(d[i])