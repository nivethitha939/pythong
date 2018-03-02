a=input()
b=list(a)
d=len(b)
i=0
j=0
f=[]
while d>0:
    c=ord(b[i])
    if c>96:
        e=b[i].upper()
    else:
        e=b[i].lower()
    f.insert(j,e)
    d=d-1
    j=j+1
    i=i+1
print("".join(f))
