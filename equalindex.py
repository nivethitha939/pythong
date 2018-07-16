a,b,c=int(input()),list(str(input()).split()),[]
for i in range(0,a):
    if int(i) == int(b[i]):
        c.append(str(b[i]))
if len(c)==0:
    print("-1")
else:
    print(" ".join(sorted(c)))
