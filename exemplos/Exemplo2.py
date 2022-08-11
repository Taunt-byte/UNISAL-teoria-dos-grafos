grafo = {
    1: [2,3,4],
    2: [1,3,5],
    3: [1,2,4],
    4: [1,3],
    5: [2]
}

print(grafo)
print("Vertices do grafo: ", grafo.keys())
for i in grafo:
    print(i)
vert = int(input("Informe o vertice para encontrar os adjacentes..:"))
print(grafo.get(vert))