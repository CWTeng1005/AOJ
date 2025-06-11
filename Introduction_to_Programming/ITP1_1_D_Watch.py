sec = int(input())
(h, m, s) = (0, 0, 0)
h = sec // 3600
m = (sec // 60) % 60
s = sec % 60
print(f"{h}:{m}:{s}")