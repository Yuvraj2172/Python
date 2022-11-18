def wrapper(f):
    def fun(l):
        c=[]
        for i in l:
            if len(i)==12:
                a = "+91" + " " + i[2:7] + " " + i[7:]
                c.append(a)
            elif len(i) == 11:
                a = "+91"+" " + i[1:6] + " " + i[6:]
                c.append(a)
            elif len(i) == 10:
                a = "+91"+" " + i[0:5] + " " + i[5:]
                c.append(a)
            l=c.copy()

    return fun

@wrapper
def sort_phone(l):
    print("in sorted")
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


