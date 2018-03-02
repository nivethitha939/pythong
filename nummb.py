a=input()
b=list(str(a))
c=len(b)
d=0
i=0
while c>0:
    if b[i] in ("0","1","2","3","4","5","6","7","8","9"):
        f=0
    else:
        d=d+1
    i=i+1
    c=c-1
if d==0:
    print("yes")
else:
    print("no")
