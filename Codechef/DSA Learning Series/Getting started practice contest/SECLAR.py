# cook your dish here

a = int(input())
b = int(input())
c = int(input())

if a >= b and b >= c:
    print(b)
elif a >= c and c >= b:
    print(c)
elif b >= a and a >= c:
    print(a)
elif b >= c and c >= a:
    print(c)
elif c >=a and a >= b:
    print(a)
elif c >= b and b >= a:
    print(b)