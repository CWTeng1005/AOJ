import random

a = random.randint(0, 100)
b = random.randint(0, 100)

def same(x, y):
    if x == y:
        y = random.randint(0, 100)
        same(x, y)
    return y

same(a, b)
print(f"{a} {b}")
print(f"{b} {a}")