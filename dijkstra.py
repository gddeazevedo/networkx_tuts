import networkx as nx
import matplotlib.pyplot as plt
import random
import math


d = {}
pi = {}
weights = {}

nodes = [1, 2, 3, 4, 5, 6]
edges = [
    (1, 2),
    (1, 3),
    (2, 3),
    (2, 5),
    (2, 4),
    (3, 4),
    (4, 5),
    (4, 6),
    (6, 5)
]

g = nx.DiGraph()
g.add_nodes_from(nodes)
g.add_edges_from(edges)


for edge in edges:
    weights[edge] = random.randint(1, 5)


w = lambda u, v: weights[(u, v)]


def initialize_single_source(g: nx.DiGraph, s: int):
    for u in g.nodes:
        d[u] = math.inf
        pi[u] = None

    d[s] = 0


def relax(u, v , w):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)
        pi[v] = u


def extract_min(q: list[int]):
    min_node = q[0]
    min_d = d[q[0]]

    for node in q:
        if d[node] < min_d:
            min_node = node
            min_d = d[node]

    q.remove(min_node)
    return min_node


def dijkstra(g: nx.DiGraph, s: int):
    initialize_single_source(g, s)
    q = []
    q.extend(g.nodes)

    while q:
        print(q)
        u = extract_min(q)
        for v in g.adj[u]:
            relax(u, v, w)


dijkstra(g, 1)
print(f'd: {d}')
print(f'pi: {pi}')

# nx.draw(g, with_labels=True, font_weight='bold')
# plt.show()
