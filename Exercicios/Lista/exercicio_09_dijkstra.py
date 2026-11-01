# ============================================================
# EXERCÍCIO 09 — ALGORITMO DE DIJKSTRA
# ============================================================
#
# ENUNCIADO:
# Implemente o algoritmo de Dijkstra para encontrar o menor
# caminho entre um vértice de origem e os demais vértices
# de um grafo ponderado.
#
# O programa deverá:
# 1. Representar um grafo ponderado por lista de adjacência.
# 2. Receber um vértice de origem.
# 3. Calcular as menores distâncias.
# 4. Exibir o menor caminho até cada vértice alcançável.
#
# CONCEITO:
# O algoritmo de Dijkstra encontra os menores caminhos
# a partir de uma origem em grafos com pesos não negativos.
#
# Utiliza uma fila de prioridade para selecionar o vértice
# com a menor distância conhecida.
#
# Complexidade com heap binário: O((V + E) log V).
#
# IMPORTANTE:
# Dijkstra não deve ser utilizado com arestas de peso negativo.
#
# ============================================================


import heapq


# Grafo ponderado:
# Cada vizinho possui um peso associado à aresta.
grafo = {
    "A": {
        "B": 4,
        "C": 2
    },
    "B": {
        "A": 4,
        "C": 1,
        "D": 5
    },
    "C": {
        "A": 2,
        "B": 1,
        "D": 8,
        "E": 10
    },
    "D": {
        "B": 5,
        "C": 8,
        "E": 2
    },
    "E": {
        "C": 10,
        "D": 2
    }
}


def dijkstra(grafo, origem):
    """
    Calcula as menores distâncias utilizando Dijkstra.

    Retorna:
    distancias -> menor distância da origem até cada vértice.
    anteriores -> vértice anterior no menor caminho.
    """

    if origem not in grafo:
        raise ValueError("Vértice de origem não encontrado.")

    # Verifica se existem pesos negativos.
    for vizinhos in grafo.values():

        for peso in vizinhos.values():

            if peso < 0:
                raise ValueError(
                    "Dijkstra não aceita pesos negativos."
                )

    # Inicializa todas as distâncias como infinito.
    distancias = {
        vertice: float("inf")
        for vertice in grafo
    }

    # Registra o vértice anterior de cada caminho.
    anteriores = {
        vertice: None
        for vertice in grafo
    }

    # A distância da origem até ela mesma é zero.
    distancias[origem] = 0

    # Fila de prioridade no formato (distância, vértice).
    fila = [(0, origem)]

    while fila:

        # Retira o vértice com a menor distância.
        distancia_atual, atual = heapq.heappop(fila)

        # Ignora entradas antigas da fila.
        if distancia_atual > distancias[atual]:
            continue

        # Analisa os vizinhos do vértice atual.
        for vizinho, peso in grafo[atual].items():

            # Calcula a distância passando pelo vértice atual.
            nova_distancia = distancia_atual + peso

            # Verifica se encontramos um caminho melhor.
            if nova_distancia < distancias[vizinho]:

                # Atualiza a menor distância.
                distancias[vizinho] = nova_distancia

                # Registra o antecessor do vértice.
                anteriores[vizinho] = atual

                # Adiciona o novo caminho à fila.
                heapq.heappush(
                    fila,
                    (nova_distancia, vizinho)
                )

    return distancias, anteriores


def reconstruir_caminho(anteriores, origem, destino):
    """
    Reconstrói o caminho percorrendo os antecessores
    do destino até a origem.
    """

    caminho = []

    atual = destino

    # Percorre os antecessores até chegar à origem.
    while atual is not None:

        caminho.append(atual)

        if atual == origem:
            break

        atual = anteriores[atual]

    # Verifica se o destino é alcançável.
    if not caminho or caminho[-1] != origem:
        return None

    # Inverte a lista para apresentar origem -> destino.
    caminho.reverse()

    return caminho


# Define o vértice de origem.
origem = "A"

# Executa o algoritmo.
distancias, anteriores = dijkstra(grafo, origem)

print("\n========== ALGORITMO DE DIJKSTRA ==========")

print(f"Vértice de origem: {origem}")

# Exibe as menores distâncias e seus caminhos.
for destino in grafo:

    caminho = reconstruir_caminho(
        anteriores,
        origem,
        destino
    )

    if caminho is None:

        print(f"\nDestino: {destino}")
        print("Não existe caminho.")

    else:

        print(f"\nDestino: {destino}")
        print(f"Distância mínima: {distancias[destino]}")
        print(f"Caminho: {' -> '.join(caminho)}")