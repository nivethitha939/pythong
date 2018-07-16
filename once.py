a,b=int(input()),input().split()
for i in range(a):
    for j in range(i+1,a):
        if b[i]==b[j]:
            b[i],b[j]="",""
print(" ".join(b))
