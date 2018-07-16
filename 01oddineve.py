a,b,c=int(input()),input().split(),[]
for i in range(a):
    if i%2==0 and int(b[i])%2 !=0:
        c.append(b[i])
    elif i%2 != 0 and int(b[i])%2 == 0:
        c.append(b[i])
print(" ".join(c))
