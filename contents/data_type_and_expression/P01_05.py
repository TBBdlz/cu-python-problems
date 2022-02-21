"""
	P01-05: Time interval
	Calculate time time interval in hh:MM:ss format
"""
h1: int = int(input())
m1: int = int(input())
s1: int = int(input())
h2: int = int(input())
m2: int = int(input())
s2: int = int(input())
dt = (24 + (h2 - h1)) % 24 * 60*60 + (m2 - m1) * 60 + (s2 - s1)
dh = dt // (60*60)
dt -= dh * 60*60
dm = dt // 60
dt -= dm*60
ds = dt
print(f'{dh}:{dm}:{ds}')
