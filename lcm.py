a=input("enter the number")
b=input("enter the number")
if(a>b):
    c=a
else:
    c=b
while(1):
    if(c%a==0)and(c%b==0):
        d=c
        break
    d=d+c
print(d)
