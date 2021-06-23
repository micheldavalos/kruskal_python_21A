from pprint import pprint

def json_to_grafo(data):
    grafo = {} # dict()

    for particula in data:
        origen = particula['origen_x'], \
                particula['origen_y']
        destino = particula['destino_x'], \
                particula['destino_y']
        v = particula['velocidad']
        print(origen, destino, v)
        add_arista(origen, destino, v, grafo)
    return grafo

def add_arista(origen, destino, v, grafo):
    if origen in grafo:
        grafo[origen].append((v, destino))
    else:
        grafo[origen] = [(v, destino)]
    if destino in grafo:
        grafo[destino].append((v, origen))
    else:
        grafo[destino] = [(v, origen)]

        