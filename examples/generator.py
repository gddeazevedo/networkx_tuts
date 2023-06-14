import networkx as nx
import matplotlib.pyplot as plt


k_5 = nx.complete_graph(5)
k_3_5 = nx.complete_bipartite_graph(3, 5)
barbell = nx.barbell_graph(10, 10)
lollipop = nx.lollipop_graph(10, 20)

# Stochastic graph generator
er = nx.erdos_renyi_graph(100, 0.15)
ws = nx.watts_strogatz_graph(30, 3, 0.1)
ba = nx.barabasi_albert_graph(100, 5)
red = nx.random_lobster(100, 0.9, 0.9)

nx.draw(lollipop, with_labels=True, font_weight='bold')
plt.show()
