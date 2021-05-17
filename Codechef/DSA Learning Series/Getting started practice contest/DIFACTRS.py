# cook your dish here
from math import sqrt
n = int(input())

li = []

i = 1
while i <= sqrt(n):
    if n%i == 0:
        li.append(i)
        if i != n//i:
            li.append(n//i)
    i += 1        

li.sort()

print(len(li))

for i in li:
    print(i, end = " ")
    
    