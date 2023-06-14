import networkx as nx
import matplotlib.pyplot as plt


g = nx.Graph()
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
g.add_nodes_from(nodes)
g.add_edges_from(edges)

sg = g.subgraph([1, 2, 5]) # keeps the nodes passed in parameter

nx.draw(sg, with_labels=True, font_weight='bold')
plt.show()
