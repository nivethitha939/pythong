a=input()
b=list(str(a))
c=len(b)
d=0
i=0
while c>0:
    d=d+(int(b[i]))**2
    c=c-1
    i=i+1
print(d)
