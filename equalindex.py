a,b,c=int(input()),list(str(input()).split()),[]
for i in range(0,a):
    if int(i) == int(b[i]):
        c.append(str(b[i]))
print(" ".join(sorted(c)))
