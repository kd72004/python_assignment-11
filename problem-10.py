x=int(input("enter number -> "))
octal=0
while x:
    octal=octal*10+x%8
    x=x//8
while octal:
    print(octal%10,end="")
    octal=octal//10
    
