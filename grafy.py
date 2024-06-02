# grafy.py
import networkx as nx
import matplotlib.pyplot as plt

def stworz_graf():
    
    "Tworzy pusty graf nieskierowany."
    
    return nx.Graph()

def dodaj_wierzcholek(gra, wierzcholek):
    
    "Dodaje wierzchołek do grafu."
    
    gra.add_node(wierzcholek)

def dodaj_krawedz(gra, wierzcholek1, wierzcholek2):
    
    "Dodaje krawędź między dwoma wierzchołkami w grafie nieskierowanym."
    
    gra.add_edge(wierzcholek1, wierzcholek2)

def oblicz_stopnie(gra):
    
    "Oblicza stopnie wierzchołków w grafie."
    
    return dict(gra.degree())

def znajdz_sciezke(gra, start, koniec):
    
    "Znajduje ścieżkę między dwoma wierzchołkami w grafie."
    
    try:
        return nx.shortest_path(gra, source=start, target=koniec)
    except nx.NetworkXNoPath:
        return None

def rysuj_graf(gra):
    
    "Rysuje wizualizację grafu."
    
    pos = nx.spring_layout(gra)
    nx.draw(gra, pos, with_labels=True, font_weight='bold')
    plt.show()
