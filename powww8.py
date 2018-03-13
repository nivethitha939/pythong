a=int(input())
b=a*8
i=0
f=[]
while b>0:
    n=i*i
    f.append(n)
    i=i+8
    b=b-1
if a in f:
    print("yes")
else:
    print("no")
