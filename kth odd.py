a=input("\nEnter number of values")
k=int(input("\nenter the kth number"))
b=list(str(a))
j=len(b)
c=0
d=[]
f=[]
e=0
g=0
h=0
while j>0:
    if(int(b[c])%2==0):
        f.insert(g,b[h])
    else:
        d.insert(e,b[c])
    c=c+1
    e=e+1
    j=j-1
print("\n",d[k-1])
    
