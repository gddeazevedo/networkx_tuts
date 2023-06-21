import math
import networkx as nx
from collections import deque

BLACK = 'B'
WHITE = 'W'
GREY  = 'G'

d = {}
pi = {}
colors = {}


def bfs(G: nx.DiGraph | nx.Graph, s):
    for v in G.nodes:
        colors[v] = WHITE
        pi[v] = None
        d[v] = math.inf

    q = deque()
    colors[s] = GREY
    d[s] = 0
    q.append(s)

    while q:
        u = q.popleft()

        for v in G.adj[u]:
            if colors[v] == WHITE:
                colors[v] = GREY
                pi[v] = u
                d[v] = d[u] + 1
                q.append(v)

        colors[u] = BLACK


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

bfs(G, 1)

print(pi)
print(d)
