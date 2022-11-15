from itertools import permutations
from sys import maxsize

v = 4


def solution(graph, start):
    vertex = []
    for i in range(v):
        if i != start:
            vertex.append(i)
    min_cost = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_cost = 0
        k = start
        for j in i:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]
        min_cost = min(min_cost, current_cost)

    return min_cost


graph = []
for i in range(v):
    t = []
    for j in range(v):
        t.append(int(input(f"enter {i} {j} value: ")))
    graph.append(t)
s = 0

print(solution(graph, s))
