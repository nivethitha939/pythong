a=int(input())
b=int(input())
i=2
while True:
 if a==1 and b==1:
  print(a)
  break
 elif a%i==0 and b%i==0:
  print(i)
  break
 i=i+1
