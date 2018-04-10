a=list(str(input()))
if a==list(reversed(a)):
    del a[len(a)-1]
    print("".join(a))
else:
    print("".join(a))
