x=int(input("enter number "))
sum=0
while(x):
    sum=sum+x%10
    x=x//10
print(sum)
