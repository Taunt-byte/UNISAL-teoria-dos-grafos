
"""
===========================================================
Projeto: Teoria dos Grafos
Assunto: Grafos Ponderados
Estrutura: Lista de Adjacência com Pesos

Descrição:
    O programa representa cidades e suas conexões por meio
    de um dicionário Python.

    Cada chave representa um vértice (cidade).
    Cada elemento interno representa uma cidade adjacente.
    Cada valor numérico representa o peso da aresta,
    interpretado neste exemplo como distância em quilômetros.

Funcionalidades:
    1. Exibir a estrutura completa do grafo.
    2. Listar os vértices existentes.
    3. Consultar as cidades adjacentes e suas distâncias.
    4. Consultar a distância entre duas cidades.

Tipo de grafo:
    Ponderado e não direcionado (conforme a modelagem pretendida).

Autor: Lucas Neves
===========================================================
"""

# Definição do grafo ponderado por lista de adjacência
grafo = {
    "Cruzeiro": {
        "Cachoeira": 15,
        "Canas": 20,
        "Lorena": 30
    },

    "Lorena": {
        "Canas": 10,
        "Cachoeira": 20,
        "Aparecida": 25,
        "Piquete": 8
    },

    "Piquete": {
        "Lorena": 8,
        "Delfim Moreira": 15
    },

    "Aparecida": {
        "Potim": 5,
        "Lorena": 25,
        "Roseira": 12
    },

    "Roseira": {
        "Lorena": 30,
        "Taubate": 40
    },

    "Taubate": {
        "Roseira": 40,
        "Cacapava": 20
    }
}


# Exibe a estrutura completa do grafo
print("========== ESTRUTURA DO GRAFO ==========")
print(grafo)


# Percorre o dicionário e apresenta os vértices
print("\n========== VÉRTICES DO GRAFO ==========")

for cidade in grafo:
    print(f"- {cidade}")


# Solicita uma cidade para consultar suas conexões
cidade = input("\nInforme uma cidade para consultar suas adjacências: ").strip()

# Verifica se a cidade existe como vértice no grafo
if cidade in grafo:

    print(f"\n========== CONEXÕES DE {cidade.upper()} ==========")

    # Percorre as cidades adjacentes e seus respectivos pesos
    for vizinha, distancia in grafo[cidade].items():
        print(f"{cidade} -> {vizinha}: {distancia} km")

else:
    print("\nCidade não encontrada como vértice no grafo.")


# Solicita duas cidades para consultar uma conexão direta
origem = input("\nInforme a cidade de origem: ").strip()
destino = input("Informe a cidade de destino: ").strip()

# Verifica se existe uma aresta direta entre as cidades
if origem in grafo and destino in grafo[origem]:

    distancia = grafo[origem][destino]

    print(f"\nDistância entre {origem} e {destino}: {distancia} km")

else:
    print("\nNão existe uma conexão direta cadastrada entre essas cidades.")
