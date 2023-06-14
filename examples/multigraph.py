import networkx as nx
import matplotlib.pyplot as plt


mg = nx.MultiGraph()
nodes = [1, 2, 3, 4, 5, 6]
edges = [
    (1, 2),
    (1, 3),
    (1, 6),
    (2, 4),
    (5, 6),
    (3, 4),
    (4, 5),
    (5, 4)
]

mg.add_nodes_from(nodes)
mg.add_edges_from(edges)

nx.draw(mg, with_labels=True, font_weight='bold')
plt.show()
