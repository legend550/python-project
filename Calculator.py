# calculator made by Keshav
a = int(input("enter your number\n"))
b = int(input("enter your another number\n"))
print("type your function")
c = str(input())
if c==("+"):
    print(a+b)
elif c == ("-"):
    print(a-b)
elif c==("*"):
    print(a*b)
elif c==("//"):
    print(a//b)
elif c==("**"):
    print(a**b)
elif c==("%"):
    print(a%b)
elif b==(0):
    print("Invalid input")
else:
    print(a/b)



