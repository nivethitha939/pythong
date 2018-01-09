a=[]
b=int(input("Enter number of elements:"))
for i in range(1,b+1):
    c=int(input(" "))
    a.append(c)
a.sort()
print("Largest element is:",a[b-1])
