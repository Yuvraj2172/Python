from random import *
from string import *
def password_generator(n):
    letters=list(ascii_letters)
    dig=list(digits)
    punctuations=list(punctuation)
    f=dig+letters+punctuations
    password=sample(f,n)
    return "".join(password)
if __name__=='__main__':
    print("\033[1m" + "Welcome to Password Generator" + "\033[0m")
    while True:
        ch=input("Press  "+"\033[1m" + "Y or y " + "\033[0m"+" to generate a password "+ " To quit press "+"\033[1m" + "N or n " + "\033[0m"+'\n')
        if ch=='y' or ch=='Y':
            n=int(input("\033[1m" + "Enter the length of password to be generated=" + "\033[0m"))
            f=password_generator(n)
            print("\033[1m" + "Generated Password=" + "\033[0m"+f)

        elif ch=='N' or ch=='n':
            break
        else :
            print("")