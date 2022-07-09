"""
	P03-07: Gymnastics score
"""
import logging
s1, s2, s3, s4 = [float(i) for i in input().split()]


logging.basicConfig(filename='P3_7_info.log', level=logging.INFO)
# objectives get {s1', s2', s3', s4'} such that s1' < s2' < s3' < s4'
# hardcode insertion sort for efficiency
if s1 > s2:
    s1, s2 = s2, s1
elif s1 > s3:
    s1, s3 = s3, s1
elif s1 > s4:
    s1, s4 = s4, s1

if s2 > s3:
    s2, s3 = s3, s2
elif s2 > s4:
    s2, s4 = s4, s2

if s3 > s4:
    s3, s4 = s4, s3

logging.info(f'{s1} {s2} {s3} {s4}')
print((s2 + s3) / 2)
