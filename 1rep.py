a,b,c=int(input()),list(str(input()).split()),[]
for i in range(0,a):
    for j in range(i+1,a):
        if b[i]==b[j]:
            c.append(b[i])
print(c[0])
