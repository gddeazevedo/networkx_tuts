import networkx as nx
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

H = nx.DiGraph(G)

print(G)
print(H)
print(G.adj)
print(H.adj)

# nx.draw(G, with_labels=True, font_weight='bold')
# nx.draw(H, with_labels=True, font_weight='bold')
# plt.show()
