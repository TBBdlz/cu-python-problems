"""
	P04-02 Median
"""

a: int = int(input())
b: int = int(input())
c: int = int(input())
d: int = int(input())
e: int = int(input())

if a > b:
    a, b = b, a
if c > d:
    c, d = d, c
if a > c:
    b, d = d, b
    c = a
a = e
if a > b:
    a, b = b, a
if c > a:
    b, d = d, b
    a = c
if a > d:
    print(d)
else:
    print(a)
