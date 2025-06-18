import random

a = random.randint(0, 100)
b = random.randint(0, 100)

def same(x, y):
    if x == y:
        y = random.randint(0, 100)
        same(x, y)
    return x, y

same(a, b)
print(f"{a} {b}")
t_a = a
t_b = b
a = t_b
b = t_a
print(f"{a} {b}")