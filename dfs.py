import networkx as nx


BLACK = 'B'
WHITE = 'W'
GREY  = 'G'


d = {}
f = {}
pi = {}
colors = {}
time = 0

nodes = [1, 2, 3, 4, 5, 6]
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (5, 6),
    (3, 4),
]
G = nx.Graph()

G.add_nodes_from(nodes)
G.add_edges_from(edges)


def dfs_visit(G: nx.Graph, u: int):
    global time
    time += 1
    d[u] = time
    colors[u] = GREY

    for v in G.adj[u]:
        if colors[v] == WHITE:
            pi[v] = u
            dfs_visit(G, v)

    colors[u] = BLACK
    time += 1
    f[u] = time


def dfs(G: nx.Graph):
    for u in G.nodes:
        pi[u] = None
        colors[u] = WHITE

    for u in G.nodes:
        if colors[u] == WHITE:
            dfs_visit(G, u)


dfs(G)

print(pi)
print(d)
print(f)
