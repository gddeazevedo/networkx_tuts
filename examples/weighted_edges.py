import networkx as nx
import matplotlib.pyplot as plt


FG = nx.Graph()
FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])


for node, neighbors in FG.adj.items():
    print(f'{node} -> {neighbors}')

# for n, nbrs in FG.adj.items():
#    for nbr, eattr in nbrs.items():
#        wt = eattr['weight']
#        if wt < 0.5: print(f"({n}, {nbr}, {wt:.3})")

