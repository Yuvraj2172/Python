n=int(input())
m=int(input())
k=0
for i in range(1,n+1):
    print(" "*(n-i),end="")
    while k!=2*i-1:
        if k==0 or k==2*i-i or i==m or k==2*i -i +1:
            print("*",end='')
        else:
            print(" ",end='')
        k+=1
    k=0
    print()
