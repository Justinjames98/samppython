a=int(input("enter a number"))
rev=0
while(a>0):
    remainder=a%10
    rev=(rev*10)+remainder
    a=a//10
print(rev)