import networkx as nx
import matplotlib.pyplot as plt


DG = nx.DiGraph()
DG.add_edge(2, 1)
DG.add_edge(1, 3)
DG.add_edge(2, 4)
DG.add_edge(1, 2)

print(f'Edges: {DG.edges}')
print(f'Nodes: {DG.nodes}')
print(f'Neighbours of 1: {DG.adj[1]}')
nx.draw(DG, with_labels=True, font_weight='bold')
plt.show()
