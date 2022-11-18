f=open("b.txt",'w')
print("enter input = ")
while str != '@':
    str=input()
    if "@" in str:
        result=str.find("@")
        f.write(str[:result])
f.close()



f.close()
f=open("b.txt",'r')
print(f.read())
f.close()
