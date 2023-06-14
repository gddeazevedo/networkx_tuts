import networkx as nx
import matplotlib.pyplot as plt


g = nx.complete_graph(3)
k = nx.complete_bipartite_graph(2, 3)

u = nx.disjoint_union(g, k)
p = nx.cartesian_product(g, k)
k_complement = nx.complement(k)

nx.draw(k_complement, with_labels=True, font_weight='bold')
plt.show()

