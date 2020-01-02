import math

r = input()
rr = float(r)
if rr >=1 and rr <= 10000:
    area = math.pi * float(r) ** 2
    print("%.7f" % (area))