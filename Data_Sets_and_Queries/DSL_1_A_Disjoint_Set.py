"""
DSL_1_A: Disjoint Set
Write a program which manipulates a disjoint set S = S1, S2, ..., Sk
1. The program should read an integer n
2. Make a disjoint set where each element consists of 0, 1, ..., n-1
3. Read an integer q
4. Manipulate the set for q queries:
    - 0: unite(x,y): unites sets that contain x and y into a new set
    - 1: same(x,y): determine whether x and y are in the same set

input: 1st line: n q
n q
q1 x1 y1
q2 x2 y2
...
qq xq yq

output: for same operation, print 1 if same else print 0
"""

n, q = map(int, input().split( ))

parent = [0] * n
rank = [0] * n

for i in range(n):
    parent[i] = i
    rank[i] = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def unite(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    else:
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        else:
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1

def same(rx, ry):
    if find(rx) != find(ry):
        print("0")
    else:
        print("1")

for _ in range(q):
    query, x, y = map(int, input().split( ))
    if query == 0:
        unite(x, y)
    elif query == 1:
        same(x, y)