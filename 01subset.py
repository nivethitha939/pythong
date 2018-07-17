a,c,d,e=input().split(),input().split(),input().split(),0
for i in range(int(a[1])):
    if d[i] in c:e=e+1
print("YES" if e==int(a[1]) else "NO")
