a,b=list(str(input())),list(str("dhoni"))
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            a[i],b[j]="",""
if len(''.join(a))+len(''.join(b))==0:
    print("yes")
else:
    print("no")
