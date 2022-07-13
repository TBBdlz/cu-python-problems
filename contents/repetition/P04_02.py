"""
	P04-02: partition flowchart
"""

d: list[int] = [int(i) for i in input().split()]
p: int = d[-1]
i: int = -1
j: int = 0
n: int = len(d)

while j < n - 1:
	while d[j] <= p:
		i += 1
		d[i], d[j] = d[j], d[i]
	j += 1

d[i+1], d[-1] = d[-1], d[i+1]
print(d)
