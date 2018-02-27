a=input()
b=a.split()
c=len(b)
e=c
d=[]
i=0
j=0
while c>0:
    d=list(b[i])
    e=d[0].upper()
    d[0]=e
    print("".join(d)," ",end="")
    i=i+1
    c=c-1
