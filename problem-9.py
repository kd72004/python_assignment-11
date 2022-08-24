x=int(input("enter number "))
b=0
while(x):
    b=(b*10)+x%2
    x=x//2
while(b):
    print(b%10)
    b=b//10
