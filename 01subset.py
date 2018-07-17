a,b,c,d,e=int(input()),int(input()),input().split(),input().split(),0
for i in range(b):
    if d[i] in c:e=e+1
print("YES" if e==b else "NO")
