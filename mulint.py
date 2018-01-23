a=int(input("Enter a number:"))
b=1
while(a>0):
    c=a%10
    b=b*c
    a=a//10
if b%2==0:
    print("even")
else:
    print(odd)
