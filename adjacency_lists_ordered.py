import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    pos = nx.spring_layout(G)  # Позиціонування вершин
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=5, font_weight="bold")
    plt.show()


graph = {
    
    "Modrice, smycka": ["Modrice, Tyrsova"],
    "Modrice, Tyrsova": ["Modrice, smycka", "Modricka cihelna"],
    "Modricka cihelna": ["Modrice, Tyrsova", "Moravanska"],
    "Moravanska": ["Modricka cihelna", "Moravanske lany"],
    "Moravanske lany": ["Moravanska", "Orechovska"],
    "Orechovska": ["Moravanske lany", "Bohunicka"],
    "Bohunicka": ["Orechovska", "Ustredni hrbitov"],
    "Ustredni hrbitov": ["Bohunicka", "Hluboka", "Ustredni hrbitov smycka"],
    
    "Ustredni hrbitov smycka": ["Ustredni hrbitov"],
    
    "Hluboka": ["Ustredni hrbitov", "Celni"],
    "Celni": ["Hluboka", "Nemocnice Milosrdnych bratri", "Krematorium"],
    "Nemocnice Milosrdnych bratri": ["Celni", "Porici"],
    "Porici": ["Nemocnice Milosrdnych bratri", "Mendlovo namesti", "Vaclavska"],
    "Mendlovo namesti": ["Porici", "Vystaviste", "Nemocnice u sv. Anny"],
    "Vystaviste": ["Mendlovo namesti", "Lipova"],
    "Lipova": ["Vystaviste", "Pisarky"],
    "Pisarky": ["Lipova", "Brafova"],
    "Brafova": ["Pisarky", "Stranskeho"],
    "Stranskeho": ["Brafova", "Vozovna Komin"],
    "Vozovna Komin": ["Stranskeho", "Svratecka", "Komin, smycka", "Rosickeho namesti"],
    
    "Komin, smycka": ["Vozovna Komin"],

    "Svratecka": ["Vozovna Komin", "Branka"],
    "Branka": ["Svratecka", "Podlesi"],
    "Podlesi": ["Branka", "Kamenolom"],
    "Kamenolom": ["Podlesi", "Zoologicka zahrada"],
    "Zoologicka zahrada": ["Kamenolom", "Pristaviste"],
    "Pristaviste": ["Zoologicka zahrada", "Kubickova", "Rakovecka"],
    
    "Rakovecka": ["Pristaviste"],
    
    "Kubickova": ["Pristaviste", "Ondrouskova"],
    "Ondrouskova": ["Kubickova", "Ecerova"],
    "Ecerova": ["Ondrouskova"],
    
    
    "Stary Liskovec, smycka": ["Dunajska"],
    "Dunajska": ["Stary Liskovec, smycka", "Osova"],
    "Osova": ["Dunajska", "Svermova"],
    "Svermova": ["Osova", "Beloruska"],
    "Beloruska": ["Svermova", "Krematorium"],
    "Krematorium": ["Beloruska", "Celni", "Vsetinska"],

}

# Виведення графа
draw_graph(graph)