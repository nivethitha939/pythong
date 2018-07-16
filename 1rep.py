a,b,c=int(input()),input().split(),[]
for i in range(a):
    for j in range(i+1,a):
        if b[i]==b[j]:
            c.append(b[i])
            break
    if len(c)==1:
        break
if len(c)==0:
    print("unique")
else:
    print(" ".join(c))
