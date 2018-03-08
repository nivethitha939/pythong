a=list(input())
b=a
c=len(b)
i=0
while True:
    k=0
    d=0
    while True:
        if d==c:
            break
        elif b[i]==a[d]:
            k=k+1
        d=d+1
    if k==1:
        print(b[i],end="")
    i=i+1
    if i==c:
        break
        
