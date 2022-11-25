import math
import random

x1 = random.randint(10, 99)
y1 = random.randint(10, 99)
z1 = random.randint(10, 99)
x2 = random.randint(10, 99)
y2 = random.randint(10, 99)
z2 = random.randint(10, 99)
x = math.pow(x2-x1, 2)
y = math.pow(y2-y1, 2)
z = math.pow(z2-z1, 2)
c = round(math.sqrt(x+y), 2)
d = round(math.sqrt(x+y+z), 2)

print(f"Расстояние между точками в 2D - {c}")
print(f"Расстояние между точками в 3D - {d}")



