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
G.add_node(10)
G.add_edges_from(edges)
G.add_edge(3, 10)

print(f'Nodes: {G.nodes}')
print(f'Edges: {G.edges}')

G.remove_node(1)

print('----ADJ LIST----')
for node in G.nodes:
    print(f'{node} -> {G.adj[node]}')
    
    
print('----DEGREE----')
for node in G.nodes:
    print(f'd({node}) = {G.degree[node]}')

nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
