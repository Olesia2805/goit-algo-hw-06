'''

This directed graph is a visualization of the transport network between cities.
Each city is represented as a vertex, and directed edges between cities show transport routes between them.
The weight of each edge represents the time it takes to travel between cities, measured in hours.

'''

import networkx as nx
import matplotlib.pyplot as plt
import analisis

G_list = nx.DiGraph()

G_list.add_nodes_from(["Poltava_1", "Ivano-Frankivsk_2", "Mykolaiv_3", "Kyiv_4", "Kropyvnytskyi_5", "Lviv_6"])

edges_with_weights = [
    ("Poltava_1", "Kyiv_4", {'weight': 5}), ("Poltava_1", "Lviv_6", {'weight': 4}),
    ("Lviv_6", "Poltava_1", {'weight': 4}), ("Kyiv_4", "Lviv_6", {'weight': 7}),
    ("Kropyvnytskyi_5", "Lviv_6", {'weight': 4}), ("Ivano-Frankivsk_2", "Kyiv_4", {'weight': 13}), 
    ("Kropyvnytskyi_5", "Ivano-Frankivsk_2", {'weight': 7}), ("Kyiv_4", "Kropyvnytskyi_5", {'weight': 10}),
    ("Kropyvnytskyi_5", "Kyiv_4", {'weight': 10}), ("Kyiv_4", "Mykolaiv_3", {'weight': 8}),
    ("Kropyvnytskyi_5", "Mykolaiv_3", {'weight': 6}), ("Ivano-Frankivsk_2", "Ivano-Frankivsk_2", {'weight': 1})
]

G_list.add_edges_from(edges_with_weights)

pos = nx.planar_layout(G_list)

nx.draw(G_list, pos, with_labels=True, node_color="pink", font_weight="bold", arrows=True, node_size=1500, font_size=8)

edge_labels = nx.get_edge_attributes(G_list, 'weight')
nx.draw_networkx_edge_labels(G_list, pos, edge_labels=edge_labels)

analisis.analisis_func(G_list, "Poltava_1", "Ivano-Frankivsk_2")
analisis.myDFS(G_list, "Poltava_1")
analisis.myBFS(G_list, "Poltava_1")
analisis.myDijkstra(G_list, "Poltava_1")

plt.show()
