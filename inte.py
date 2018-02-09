a=input("enter the values")
b=list(str(a))
c=0
d=len(b)
while d>0:
    if(("0" in b)or("1" in b)or("2" in b)or("3" in b)or("4" in b)or("5" in b)or("6" in b)or("7" in b)or("8" in b)or("9" in b)):
        c=c+1
    d=d-1
print("\n",c)
