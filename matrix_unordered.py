import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adj_matrix = np.array([
    [0, 5, 0, 0, 0, 1],  # node 1
    [5, 0, 5, 1, 0, 0],  # node 2
    [0, 5, 0, 0, 6, 0],  # node 3
    [0, 1, 0, 0, 3, 7],  # node 4
    [0, 0, 6, 3, 0, 4],  # node 5
    [1, 0, 0, 7, 4, 0]   # node 6
])


G = nx.Graph()

num_nodes = len(adj_matrix)
G.add_nodes_from(range(1, num_nodes + 1))

for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        weight = adj_matrix[i][j]
        if weight != 0:
            G.add_edge(i + 1, j + 1, weight=weight)

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
