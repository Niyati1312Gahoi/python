a=int(input("enter a number "))
if a%2==0:
    print(f"Number {a} is even")
else:
    print(f"Number {a} is odd")

s=f"{a} is even" if(a%2==0)else f"{a} is odd"
print(s)
