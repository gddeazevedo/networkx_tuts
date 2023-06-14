import networkx as nx
import matplotlib.pyplot as plt


DG = nx.DiGraph()

nodes = [i for i in range(1, 11)]
DG.add_nodes_from(nodes)

DG.add_edge(1, 2)
DG.add_edge(1, 3)
DG.add_edge(4, 2)
DG.add_edge(2, 3)
DG.add_edge(10, 2)
DG.add_edge(5, 2)
DG.add_edge(5, 1)
DG.add_edge(1, 10)
DG.add_edge(6, 7)
DG.add_edge(10, 7)
DG.add_edge(6, 8)
DG.add_edge(6, 9)


print(f'Edges: {DG.edges}')
print(f'Nodes: {DG.nodes}')
print(f'Neighbours of 1: {DG.adj[1]}')
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()
