import string
a=(input())
a.lower()
a=list(a)
a.sort()
b=list(string.ascii_lowercase)
c=0
for i in b:
    if i in a:
        c+=1

if c==26:
    print("YES")
else :
    print("NO")
# if a==b:
#     print("YES")
# else :
#     print("NO")
