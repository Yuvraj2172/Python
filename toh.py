def tower(n,a,c,b):
    if n==1:
        print('Move %i disk from %s to %s '%(n,a,c))
    else :
        # print('Move %i disk from %s to %s ' % (n - 1, a, b))
        tower(n - 1, a,b,c)

        print('Move %i disk from %s to %s ' % (n , a, c))
        tower(n-1, b, c, a)

n=int(input('Number of disks='))
tower(n,'a','c','b')