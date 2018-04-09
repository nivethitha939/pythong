a,b,f=list(str(raw_input())),list(str(raw_input())),list(str("FLAMES"))
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            a[i],b[j]="",""
b=(len(''.join(a))+len(''.join(b)))-1
while True:
    for j in range(0,b):
        a=f[0]
        for i in range(0,len(f)-1):
            f[i]=f[i+1]
        f[len(f)-1]=a
    del f[0]
    if len(f)==1:
        break
if ("".join(f[0]))=="F":
    print("Friends!")
elif ("".join(f[0]))=="L":
    print("Lovers!")
elif ("".join(f[0]))=="A":
    print("Affection!")
elif ("".join(f[0]))=="M":
    print("Marriage!")
elif ("".join(f[0]))=="E":
    print("Enemy!")
else:
    print("Sister!")
