import networkx as nx
import math

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


for edge in edges:
    weights[edge] = random.randint(1, 5)


w = lambda u, v: weights[(u, v)]


def initialize_single_source(g: nx.DiGraph, s: int):
    for u in g.nodes:
        d[u] = math.inf
        pi[u] = None

    d[s] = 0


def extract_min(q: list[int]):
    min_node = q[0]
    min_key = key[q[0]]

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

    keys[v] = 0
    q = []
    q.extend(G.nodes)

    while q:
        u = extract_min(q)

        for v in G.adj[u]:
            if v in q and keys[v] > w(u, v):
                pi[v] = u
                keys[v] = w(u, v)
