import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from([1, 2, 3, 4, 5, 6])

edges_with_weights = [
    (1, 4, {'weight': 5}), (1, 6, {'weight': 4}), (6, 1, {'weight': 4}),
    (4, 6, {'weight': 7}), (5, 6, {'weight': 4}), (2, 4, {'weight': 13}), 
    (5, 2, {'weight': 7}), (4, 5, {'weight': 10}), (5, 4, {'weight': 10}),
    (4, 3, {'weight': 8}), (5, 3, {'weight': 6})
]

G.add_edges_from(edges_with_weights)

pos = nx.planar_layout(G)

nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold", arrows=True)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
