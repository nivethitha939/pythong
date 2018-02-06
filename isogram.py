a=input("enter the value:")
b=list(str(a))
c=len(b)
i=0
d=0
while i<c:
    if(b[i]==b[i+1]):
        d=d+1
        i=i+1
if(d==0):
    printf("yes")
else:
    print("No")
