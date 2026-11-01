# ============================================================
# EXERCÍCIO 01 — REPRESENTAÇÃO DE UM GRAFO POR LISTA DE ADJACÊNCIA
# ============================================================
#
# ENUNCIADO:
# Crie um programa que represente um grafo não direcionado
# utilizando uma lista de adjacência.
#
# O programa deverá:
# 1. Criar um grafo com cinco vértices.
# 2. Adicionar as arestas entre os vértices.
# 3. Exibir todos os vértices e seus respectivos vizinhos.
#
# CONCEITO:
# Na lista de adjacência, cada vértice possui uma lista
# contendo os vértices diretamente conectados a ele.
#
# ============================================================


# Cria um grafo utilizando dicionário.
# Cada chave representa um vértice.
# Cada valor representa a lista de vizinhos desse vértice.
grafo = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": []
}


def adicionar_aresta(grafo, origem, destino):
    """
    Adiciona uma aresta entre dois vértices.

    Como o grafo é não direcionado, a conexão
    precisa ser adicionada nos dois sentidos.
    """

    grafo[origem].append(destino)
    grafo[destino].append(origem)


def exibir_grafo(grafo):
    """
    Percorre o dicionário e exibe a lista de
    adjacência de cada vértice.
    """

    print("\n========== LISTA DE ADJACÊNCIA ==========")

    for vertice, vizinhos in grafo.items():
        print(f"{vertice} -> {vizinhos}")


# Adiciona as arestas do grafo.
adicionar_aresta(grafo, "A", "B")
adicionar_aresta(grafo, "A", "C")
adicionar_aresta(grafo, "B", "D")
adicionar_aresta(grafo, "C", "D")
adicionar_aresta(grafo, "D", "E")


# Exibe a estrutura completa do grafo.
exibir_grafo(grafo)