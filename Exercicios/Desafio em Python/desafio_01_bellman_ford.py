# ============================================================
# DESAFIO 01 — ALGORITMO DE BELLMAN-FORD
# ============================================================
#
# ENUNCIADO:
# Desenvolva um programa que encontre os menores caminhos
# entre um vértice de origem e os demais vértices de um
# grafo direcionado e ponderado.
#
# Diferentemente do algoritmo de Dijkstra, o Bellman-Ford
# deve permitir arestas com pesos negativos.
#
# O programa deverá:
# 1. Representar um grafo direcionado por uma lista de arestas.
# 2. Receber um vértice de origem.
# 3. Calcular as menores distâncias possíveis.
# 4. Reconstruir os caminhos encontrados.
# 5. Identificar a existência de ciclos negativos alcançáveis
#    a partir da origem.
#
# CONCEITOS:
# O algoritmo relaxa todas as arestas V - 1 vezes.
#
# Relaxamento consiste em verificar se um caminho encontrado
# através de uma aresta é menor que a distância conhecida.
#
# Após as iterações, uma nova possibilidade de redução
# indica a existência de um ciclo negativo alcançável.
#
# Complexidade: O(V * E).
#
# ============================================================


# Grafo direcionado representado por uma lista de arestas.
#
# Cada aresta possui o formato:
# (origem, destino, peso)
#
# Os pesos negativos são permitidos.
arestas = [
    ("A", "B", 6),
    ("A", "C", 7),
    ("B", "C", 8),
    ("B", "D", 5),
    ("B", "E", -4),
    ("C", "D", -3),
    ("C", "E", 9),
    ("D", "B", -2),
    ("E", "A", 2),
    ("E", "D", 7)
]


# Lista de vértices existentes no grafo.
vertices = ["A", "B", "C", "D", "E"]


def bellman_ford(vertices, arestas, origem):
    """
    Executa o algoritmo de Bellman-Ford.

    Parâmetros:
    vertices -> lista contendo os vértices do grafo.
    arestas  -> lista de arestas com seus respectivos pesos.
    origem   -> vértice inicial da busca.

    Retorna:
    distancias -> menor distância conhecida até cada vértice.
    anteriores -> antecessor de cada vértice no menor caminho.
    """

    # Verifica se a origem pertence ao grafo.
    if origem not in vertices:
        raise ValueError("Vértice de origem não encontrado.")

    # Inicializa todas as distâncias com infinito.
    distancias = {
        vertice: float("inf")
        for vertice in vertices
    }

    # Armazena o vértice anterior de cada destino.
    anteriores = {
        vertice: None
        for vertice in vertices
    }

    # A distância da origem até ela mesma é zero.
    distancias[origem] = 0

    # ========================================================
    # ETAPA 1 — RELAXAMENTO DAS ARESTAS
    # ========================================================

    # Para um grafo com V vértices, são necessárias
    # no máximo V - 1 iterações.
    for _ in range(len(vertices) - 1):

        # Controla se alguma distância foi modificada.
        houve_atualizacao = False

        # Percorre todas as arestas.
        for origem_aresta, destino, peso in arestas:

            # Não é possível relaxar uma aresta partindo
            # de um vértice que ainda não foi alcançado.
            if distancias[origem_aresta] == float("inf"):
                continue

            # Calcula a distância passando pela aresta atual.
            nova_distancia = (
                distancias[origem_aresta] + peso
            )

            # Verifica se encontramos um caminho menor.
            if nova_distancia < distancias[destino]:

                # Atualiza a menor distância.
                distancias[destino] = nova_distancia

                # Registra o antecessor do destino.
                anteriores[destino] = origem_aresta

                houve_atualizacao = True

        # Se nenhuma distância foi alterada, não precisamos
        # continuar executando as iterações.
        if not houve_atualizacao:
            break

    # ========================================================
    # ETAPA 2 — DETECÇÃO DE CICLO NEGATIVO
    # ========================================================

    # Se ainda for possível diminuir uma distância,
    # existe um ciclo negativo alcançável pela origem.
    for origem_aresta, destino, peso in arestas:

        if distancias[origem_aresta] == float("inf"):
            continue

        if (
            distancias[origem_aresta] + peso
            < distancias[destino]
        ):

            return None, None, True

    return distancias, anteriores, False


def reconstruir_caminho(anteriores, origem, destino):
    """
    Reconstrói o caminho entre a origem e o destino.

    A reconstrução começa pelo destino e utiliza
    os antecessores até encontrar a origem.
    """

    caminho = []

    atual = destino

    # Percorre os antecessores.
    while atual is not None:

        caminho.append(atual)

        # Quando encontramos a origem, terminamos.
        if atual == origem:
            break

        atual = anteriores[atual]

    # Verifica se o destino realmente é alcançável.
    if not caminho or caminho[-1] != origem:
        return None

    # Inverte o caminho para apresentar origem -> destino.
    caminho.reverse()

    return caminho


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

origem = "A"

distancias, anteriores, ciclo_negativo = bellman_ford(
    vertices,
    arestas,
    origem
)

print("\n========== ALGORITMO DE BELLMAN-FORD ==========")

if ciclo_negativo:

    print("Foi identificado um ciclo negativo alcançável.")
    print("Não é possível determinar menores caminhos finitos.")

else:

    print(f"Vértice de origem: {origem}")

    for destino in vertices:

        print(f"\nDestino: {destino}")

        # Verifica se o destino é inalcançável.
        if distancias[destino] == float("inf"):

            print("Não existe caminho a partir da origem.")

        else:

            caminho = reconstruir_caminho(
                anteriores,
                origem,
                destino
            )

            print(f"Distância mínima: {distancias[destino]}")
            print(f"Caminho: {' -> '.join(caminho)}")