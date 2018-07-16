a,b=int(input()),input().split()
for i in range(a):
    if i%2==0 and int(b[i])%2 !=0:
        print(b[i],end=" ")
    elif i%2 != 0 and int(b[i])%2 == 0:
        print(b[i],end=" ")
