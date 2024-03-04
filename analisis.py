import networkx as nx

def analisis_func(Graph, source = None, target = None):
    num_nodes = Graph.number_of_nodes()
    num_edges = Graph.number_of_edges()
    #is_connected = nx.is_connected(Graph) -> in list_of_edges_ordered: raise nx.NetworkXNotImplemented(errmsg)
    degree_centrality = nx.degree_centrality(Graph)
    closeness_centrality = nx.closeness_centrality(Graph)
    betweenness_centrality = nx.betweenness_centrality(Graph)
    #avg_path_length = nx.average_shortest_path_length(Graph) -> in list_of_edges_ordered: raise nx.NetworkXError("Graph is not strongly connected.")
    path = nx.shortest_path(Graph, source, target)
    

    print(f'\n\nnum_nodes: ', num_nodes, '\n\nnum_edges: ', num_edges,
          '\n\ndegree_centrality: ', degree_centrality, '\n\ncloseness_centrality: ', closeness_centrality,
          '\n\nbetweenness_centrality: ', betweenness_centrality, '\n\npath: ', path)


def myDFS ():
    pass

def myBFS ():
    pass

def myDijkstra():
    pass
