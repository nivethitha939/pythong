a=list(str(input()))
b=len(a)
c=0
d=0
i=0
while b>0:
    if a[i] is '(':
        c=c+1
    elif a[i] is ')':
        d=d+1
    i=i+1
    b=b-1
if c==d:
    print("yes")
else:
    print("no")
