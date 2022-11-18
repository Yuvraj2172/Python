n=int(input())
m=int(input())

for i in range (1,(n+1)):
    if(i==m):
        for j in range (1,(2*n)):
            if((j>=(n-i+1)) and (j<=(n+i-1))):
                print("*",end="")
            else:
                print(" ",end="")
    else:
        for j in range (1,(n*2)):
            if i==1:
                if j==n:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if((j==(n-i+1)) or (j==(n+i-1))):
                    print("*",end="")
                else:
                    print(" ",end="")
    print("")