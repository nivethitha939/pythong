a=input("\nenter the name to check palindrome or not:")
b=list(reversed(a))
d=list(reversed(b))
if b==d:
    print("\nyes")
else:
    print("\nno")
