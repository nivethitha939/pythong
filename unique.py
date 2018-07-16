a,b,c=int(input()),input().split(),[]
for i in range(a):
    for j in range(i+1,a):
        if b[i]==b[j]:
            c.append(b[i])
if len(c)==0:
    print("unique")
else:
    print(" ".join(sorted(set(c))))
