'''

This graph is a visualization of a social network that reflects relationships and mutual friendships.
Each node in the graph represents one of the participants in the network,
and the edges between the nodes represent mutual friendships between the participants.
The weight of each edge represents the number of people between two participants.

'''

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import analisis

adj_matrix = np.array([
    [0, 5, 0, 0, 0, 1],  # node 1 John
    [5, 0, 5, 1, 0, 0],  # node 2 Mary
    [0, 5, 0, 0, 6, 0],  # node 3 Alex
    [0, 1, 0, 0, 3, 7],  # node 4 Sophia
    [0, 0, 6, 3, 0, 4],  # node 5 Michael
    [1, 0, 0, 7, 4, 0]   # node 6 Emma
])

user_names = ["John_1", "Mary_2", "Alex_3", "Sophia_4", "Michael_5", "Emma_6"]

G_matrix = nx.Graph()

num_nodes = len(adj_matrix)
G_matrix.add_nodes_from(range(1, num_nodes + 1))

for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        weight = adj_matrix[i][j]
        if weight != 0:
            G_matrix.add_edge(i + 1, j + 1, weight=weight)

pos = nx.circular_layout(G_matrix)
nx.draw(G_matrix, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=8, 
        font_weight='bold', labels={node: user_names[node-1] for node in G_matrix.nodes()},)

edge_labels = nx.get_edge_attributes(G_matrix, 'weight')
nx.draw_networkx_edge_labels(G_matrix, pos, edge_labels=edge_labels)

analisis.analisis_func(G_matrix, 2, 5)

is_connected = nx.is_connected(G_matrix)
avg_path_length = nx.average_shortest_path_length(G_matrix)

print ('is_connected: ', is_connected, '\navg_path_length: ', avg_path_length)

plt.show()