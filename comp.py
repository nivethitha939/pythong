n=input("\nEnter the n value")
k=input("\nEnter the k value")
a=list(str(n))
b=0
for i in n:
    for j in k:
        if i==j:
           b=b+1
print(b)
