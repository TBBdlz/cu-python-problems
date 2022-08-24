"""
	P05-05: Amount of difference data
"""

# you can do the sort -> count method
# but if we have plenty of space we should use set method
data = [int(k) for k in input().split()]
print(len(set(data)))
print(set(data))