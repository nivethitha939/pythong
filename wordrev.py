a=str(input()).split()
for i in range(0,len(a)):
    print("".join(list(reversed(a[i]))),end=" ")
