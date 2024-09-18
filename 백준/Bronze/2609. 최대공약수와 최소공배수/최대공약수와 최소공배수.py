import math

x, y = map(int, input().split(" "))
gcd = math.gcd(x, y)
lcm = math.lcm(x, y)
print(gcd)
print(lcm)
