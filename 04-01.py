s = ['R','G','B','R']
lst = []
for j in s:
    if j.isalpha():
        lst.append(j)
while(len(lst)!=1):
    i=1
    while(len(lst)>len(lst)-1):
        if lst[i] == 'G' and lst[i-1] == 'B':
                lst[i] = 'R'
                lst.pop(i-1)
                break
        elif lst[i] == 'G' and lst[i-1] == 'R':
                lst[i] = 'B'
                lst.pop(i-1)
                break
        elif lst[i] == 'R' and lst[i-1] == 'G':
                lst[i] = 'B'
                lst.pop(i-1)
                break
        elif lst[i] == 'R' and lst[i-1] == 'B':
                lst[i] = 'G'
                lst.pop(i-1)
                break
        elif lst[i] == 'B' and lst[i-1] == 'G':
                lst[i] = 'R'
                lst.pop(i-1)
                break
        elif lst[i] == 'B' and lst[i-1] == 'R':
                lst[i] = 'G'
                lst.pop(i-1)
                break
        else:
            i += 1
print('"',end="")
print(*lst,end="")
print('"')