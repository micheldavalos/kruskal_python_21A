from pprint import pprint
from grafos import add_arista


def kruskal(grafo):
    aem = {}
    lista = [] 

    for key, value in grafo.items():
        for ady in value:
            arista = ady[0], key, ady[1]
            print(arista)
            lista.append(arista)
    lista.sort(key=lambda arista:arista[0])
    pprint(lista)
    dj = make_set(grafo)
    pprint(dj)

    while len(lista) > 0:
        arista = lista[-1]
        lista.pop()
        print(arista)

        v = arista[0]
        origen = arista[1]
        destino = arista[2]

        if find_set(origen, dj) != find_set(destino, dj):
            add_arista(origen, destino, v, aem)
            union(origen, destino, dj)
            print(dj)
    
    return aem

def make_set(grafo):
    dj = []

    for key in grafo:
        dj.append([key]) # [[(x, y)], [(x1, y2)]  ]    

    return dj

def find_set(vertice, dj):
    i = 0
    while i < len(dj):
        if vertice in dj[i]:
            return i
        i = i + 1

def union(origen, destino, dj):
    i = find_set(origen, dj)
    j = find_set(destino, dj)

    l_origen = dj[i]
    l_destino = dj[j]
    l_nueva = l_origen + l_destino

    dj.remove(l_origen)
    dj.remove(l_destino)
    dj.append(l_nueva)