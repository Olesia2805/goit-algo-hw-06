import networkx as nx
import collections

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


def myDFS(graph, vertex, visited=None):

    if visited is None:
        visited = set()

    visited.add(vertex)

    print(vertex, end=' ')
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            myDFS(graph, neighbor, visited)

def myBFS(graph, start):

    visited = set()
    queue = collections.deque([start])

    while queue:

        vertex = queue.popleft()
        
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)

            queue.extend(set(graph[vertex]) - visited)

    return visited

def myDijkstra(graph, start):

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        current = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current)

        for neighbor in graph[current]:

            if neighbor in unvisited:
                new_distance = distances[current] + graph[current][neighbor]['weight']

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    
    return distances