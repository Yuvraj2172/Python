# # 1
# s=input().split(',')
# a=[]
# for i in s:
#     a.append(s.count(i))
# l=max(a)
# c=[]
# for  i in s:
#     if s.count(i)==l:
#         c.append(i)
# c.sort()
# print(c[0])

# 2
# a=int(input())
# l=len(str(bin(a)[2:]))
# for i in range(a+1):
#     print(bin(i)[2:].rjust(l))
s='())()'.split()
if s.count('(')==s.count(')'):
    print("e")
else :
    print("no")
