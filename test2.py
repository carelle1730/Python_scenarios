a = 1
b = 2
c = 3

c = a + b
if a == b:
    print("not equal")
elif a == c:
    print("not equal")
elif b == c:
    print("not equal")
elif c == a+b:
    print("equal")
else:
    print("wrong number")