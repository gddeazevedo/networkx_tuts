import networkx as nx
import matplotlib.pyplot as plt
import dfs
import bfs


nodes = ['a', 'b', 'c', 'd', 'e', 'f']
edges = [
    ('a', 'b'),
    ('a', 'c'),
    # (1, 6),
    ('b', 'd'),
    ('e', 'f'),
    ('c', 'd'),
    # (4, 5)
]

G = nx.Graph()

G.add_nodes_from(nodes)
G.add_edges_from(edges)

dfs.dfs(G)
bfs.bfs(G, 'a')
print(dfs.d)
print(dfs.f)
print(dfs.parents)

print(bfs.distances)
print(bfs.parents)

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
