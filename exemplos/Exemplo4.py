grafo = {
    "Cruzeiro":   {"Cachoeira": 15, "Canas": 20, "Lorena": 30},
    "Lorena":     {"Canas": 10, "Cachoeira": 20, "Aparecida": 25, "Piquete": 8},
    "Piquete":    {"Lorena": 8, "Delfim Moreira": 15},
    "Aparecida":  {"Potim": 5, "Lorena": 25, "Roseira": 12},
    "Roseira":    {"Lorena": 30, "Taubate": 40},
    "Taubate":    {"Roseira": 40, "Cacapava": 20}
}

print(grafo)
for i in grafo:
    print(i)