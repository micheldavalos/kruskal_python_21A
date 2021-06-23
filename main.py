import json
from pprint import pprint
from grafos import json_to_grafo
from algoritmos import kruskal

file = open('kruskal.json')
data = json.load(file)
#pprint(data)

grafo = json_to_grafo(data)
pprint(grafo, width=40)

aem = kruskal(grafo)
pprint(aem, width=40)






