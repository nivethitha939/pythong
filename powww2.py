a=int(input())
b=a*2
i=0
f=[]
while b>0:
    n=i*i
    f.append(n)
    i=i+1
    b=b-1
if a in f:
    print("yes")
else:
    print("no")
