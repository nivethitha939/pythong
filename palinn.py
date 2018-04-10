a,b=list(str(input())),0
for i in range(0,len(a)):
    b=b+int(a[i])
if str(b)=="".join(list(reversed(str(b)))):
    print("YES")
else:
    print("NO")
