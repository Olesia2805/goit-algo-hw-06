'''

This directed graph is a visualization of the transport network between cities.
Each city is represented as a vertex, and directed edges between cities show transport routes between them.
The weight of each edge represents the time it takes to travel between cities, measured in hours.

'''

import networkx as nx
import matplotlib.pyplot as plt
import analisis

G = nx.DiGraph()

graph = {
    "Odesa_1": [("Lutsk_4", 5), ("Avdiivka_6", 4)],
    "Irpin_2": [("Lutsk_4", 13),("Irpin_2", 1)],
    "Mariupol_3": [],
    "Lutsk_4": [("Avdiivka_6", 7), ("Bakhmut_5", 10), ("Mariupol_3", 8)],
    "Bakhmut_5": [("Avdiivka_6", 4),("Irpin_2", 7), ("Lutsk_4", 10), ("Mariupol_3", 6)],
    "Avdiivka_6": [("Odesa_1", 4)]
}

for node, edges in graph.items():
    for edge, weight in edges:
        G.add_edge(node, edge, weight=weight)

pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=True, node_color="yellow", font_weight="bold", arrows=True, node_size=2000, font_size=6)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

analisis.analisis_func(G, "Lutsk_4", "Odesa_1")
analisis.myDFS(G, "Odesa_1")
analisis.myBFS(G, "")
analisis.myDijkstra(G, "")

plt.show()
