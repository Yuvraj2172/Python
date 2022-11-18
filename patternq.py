a=int(input())
n=0
d=n
s=0
c=0
f=[]
while True:
    for n in range(0,inf):
        while n!=0:
            r=n%10
            s=s*10+r
            n=int(n/10)

        if d==s:
            f.append(s)
            c+=1
        else :
            pass
        if c==a:
            break

