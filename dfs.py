import networkx as nx
from typing import Any


BLACK = 'B'
GREY  = 'G'
WHITE = 'W'

colors = {}
parents = {}
f = {}
d = {}
time = 0


def dfs_visit(G: nx.Graph | nx.DiGraph, u: Any):
    global time
    time += 1
    d[u] = time
    colors[u] = GREY

    for v in G.adj[u]:
        if colors[v] == WHITE:
            parents[v] = u
            dfs_visit(G, v)

    time += 1
    f[u] = time
    colors[u] = BLACK


def dfs(G: nx.Graph | nx.DiGraph):
    for u in G.nodes:
        colors[u] = WHITE
        parents[u] = None

    for u in G.nodes:
        if colors[u] == WHITE:
            dfs_visit(G, u)
