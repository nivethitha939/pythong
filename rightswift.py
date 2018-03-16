l=int(input())
c=l
d=c
i=d
j=i
b=int(input())
f=[]
while a>0:
    f.append(input())
    l=l-1
f.insert(d,0)
while b>0:
    i=j
    d=i
    c=d
    e=c
    h=e
    while c>0:
        f[d]=f[i-1]
        d=d-1
        i=i-1
        c=c-1
    f[0]=f[e]
    b=b-1
print(" ".join(f[:-1]))        
