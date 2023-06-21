import networkx as nx
import matplotlib.pyplot as plt

BLACK = 'B'
WHITE = 'W'
GREY  = 'G'


d = {}
f = {}
pi = {}
colors = {}
time = 0

nodes = [1, 2, 3, 4, 5, 6, 7]
edges = [
    (1, 2),
    (2, 3),
    (2, 6),
    (6, 7),
    (7, 6),
    (4, 1),
    (3, 4),
    (5, 4),
    (5, 3),
    (3, 7)
]
G = nx.DiGraph()

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


def dfs(G: nx.Graph | nx.DiGraph):
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

tree = nx.DiGraph()

tree.add_nodes_from(pi.keys())

for key, value in pi.items():
    if value != None:
        tree.add_edge(value, key)


nx.draw(G, with_labels=True)
plt.show()
nx.draw(tree, with_labels=True)
plt.show()
