def fabonacci(n):
    a, b = 0, 1
    c=[]
    for i in range(0,n):

        if i==0:
            c.append(a)
        elif i==1 :
            c.append(b)
        else:
            t=b
            b = a + t
            a = t
            c.append(b)

    return c
n=int(input())
x=fabonacci(n)
print(list(map(lambda y:y**3,x)))