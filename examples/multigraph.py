import networkx as nx


mg = nx.MultiDiGraph()
mg.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])
print(dict(mg.degree(weight='weight')))
