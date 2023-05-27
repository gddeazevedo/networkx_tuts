import math
import networkx as nx
from collections import deque
from typing import Any


BLACK = 'b'
GREY  = 'g'
WHITE = 'w'

colors = {}
parents = {}
distances = {}


def bfs(G: nx.Graph | nx.DiGraph, s: Any):
    for u in G.nodes:
        colors[u] = WHITE
        parents[u] = None
        distances[u] = math.inf

    q = deque()
    colors[s] = GREY
    distances[s] = 0
    q.append(s)

    while q:
        u = q.pop()
        
        for v in G.adj[u]:
            if colors[v] == WHITE:
                colors[v] = GREY
                parents[v] = u
                distances[v] = distances[u] + 1
                q.append(v)

        colors[u] = BLACK
