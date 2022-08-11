grafo = {
    "Cruzeiro":   ["Cachoeira", "Canas", "Lorena"],
    "Lorena":     ["Canas", "Cachoeira", "Aparecida", "Piquete"],
    "Piquete":    ["Lorena", "Delfim Moreira"],
    "Aparecida":  ["Potim", "Lorena", "Roseira"],
    "Roseira":    ["Lorena", "Taubate"],
    "Taubate":    ["Roseira", "Cacapava"]
}


print("O grafo das cidades da regiao:")
print(grafo)

print("As cidades da regiao sao:")
for i in grafo:
    print(i)

cidade=input("Informe a cidade para verificar as adjacencias..:")
print(grafo.get(cidade))