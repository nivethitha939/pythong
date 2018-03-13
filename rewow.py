a=list(str(input()))
b=len(a)
i=0
d=[]
c=0
while b>0:
   if a[i] in ("a","e","i","o","u","A","E","I","O","U"):
       c=c+1
   else:
       d.append(a[i])
   i=i+1
   b=b-1
print("".join(list(reversed(d))))
