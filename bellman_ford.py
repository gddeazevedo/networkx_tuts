import networkx as nx
import matplotlib.pyplot as plt
import math
import random


d = {}
pi = {}

g = nx.DiGraph()
nodes = [i for i in range(1, 11)]
g.add_nodes_from(nodes)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(4, 2)
g.add_edge(2, 3)
g.add_edge(10, 2)
g.add_edge(5, 2)
g.add_edge(5, 1)
g.add_edge(1, 10)
g.add_edge(6, 7)
g.add_edge(10, 7)
g.add_edge(6, 8)
g.add_edge(6, 9)
weights = []


for i in range(len(g.nodes)):
    weights.append([])
    for j in range(len(g.nodes)):
        weights[i].append(random.randint(-10, 10))


w = lambda u, v: weights[u - 1][v - 1]


def init_single_source(g: nx.DiGraph, s):
    for v in g.nodes:
        d[v] = math.inf
        pi[v] = None

    d[s] = 0


def relax(u, v, w):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)
        pi[v] = u


def bellman_ford(g: nx.Graph, w, s):
    init_single_source(g, s)

    for i in range(len(g.nodes) - 1):
        for (u, v) in g.edges:
            relax(u, v, w)

    for (u, v) in g.edges:
        if d[v] > d[u] + w(u, v):
            return False

    return True


print(bellman_ford(g, w, 1))
print(pi)
print(d)

nx.draw(g, with_labels=True, font_weight='bold')
plt.show()
