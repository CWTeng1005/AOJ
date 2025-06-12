"""
Find the sum of weights of edges of the Minimum Spanning Tree

Input:
|V| |E|
s0 t0 w0
s1 t1 w1
...
|V|: number of vertices
|E|: number of edges
vertices named with 0, 1, ..., |V|-1
si: source vertices of i-th edge
ti: target vertices of i-th edge
wi: the weight of i=th edge

Output: sum of weight
"""

num_v, num_e = map(int, input().split( ))

p = [0] * num_v
rank = [0] * num_v

for i in range(num_v):
    p[i] = i
    rank[i] = 0

edges = []
for _ in range(num_e):
    s, t, w = map(int, input().split( ))
    edges.append((w, s, t))

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def unite(x, y):
    x = find(x)
    y = find(y)
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank [y]:
            rank[y] += 1

def kruskal():
    mst_weight = 0
    edges.sort()
    for w, s, t in edges:
        if find(s) != find(t):
            unite(s,t)
            mst_weight += w
    print(mst_weight)

kruskal()