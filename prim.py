import networkx as nx
import math
import random
import matplotlib.pyplot as plt


nodes = [1, 2, 3, 4, 5, 6]
edges = [
    (1, 2),
    (1, 3),
    (1, 6),
    (2, 4),
    (5, 6),
    (3, 4),
    (4, 5)
]
G = nx.Graph()

G.add_nodes_from(nodes)
G.add_edges_from(edges)



keys = {}
pi = {}
weights = {}

for u, v in G.edges:
    weights[(u, v)] = random.randint(1, 5)
    weights[(v, u)] = weights[(u, v)]


w = lambda u, v: weights[(u, v)]

def extract_min(q: list[int]):
    min_node = q[0]
    min_key = keys[q[0]]

    for node in q:
        if keys[node] < min_key:
            min_node = node
            min_key = keys[node]

    q.remove(min_node)
    return min_node


def mst_prim(G: nx.Graph, w, r):
    for v in G.nodes:
        keys[v] = math.inf
        pi[v] = None

    keys[r] = 0
    q = []
    q.extend(G.nodes)

    while q:
        print(q)
        u = extract_min(q)
        for v in G.adj[u]:
            if v in q and (u, v) in G.edges and keys[v] > w(u, v):
                pi[v] = u
                keys[v] = w(u, v)

mst_prim(G, w, 1)
print(keys)
print(pi)

mst = nx.Graph()
mst.add_nodes_from(pi.keys())

for key, value in pi.items():
    if value != None:
        mst.add_edge(key, value)


nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

nx.draw(mst, with_labels=True, font_weight='bold')
plt.show()
