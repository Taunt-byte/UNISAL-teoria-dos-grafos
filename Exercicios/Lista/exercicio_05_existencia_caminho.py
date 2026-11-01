# ============================================================
# EXERCÍCIO 05 — VERIFICAÇÃO DE EXISTÊNCIA DE CAMINHO
# ============================================================
#
# ENUNCIADO:
# Desenvolva um programa que verifique se existe um caminho
# entre dois vértices de um grafo não direcionado.
#
# O programa deverá:
# 1. Receber um grafo representado por lista de adjacência.
# 2. Receber um vértice de origem.
# 3. Receber um vértice de destino.
# 4. Informar se existe um caminho entre eles.
#
# CONCEITO:
# Um caminho é uma sequência de vértices conectados por arestas.
#
# Para solucionar o problema, será utilizada a BFS.
# Caso o destino seja encontrado durante a busca, significa
# que existe um caminho entre a origem e o destino.
#
# Complexidade: O(V + E).
#
# ============================================================


from collections import deque


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C", "F"],
    "F": ["E"],
    "G": []
}


def existe_caminho(grafo, origem, destino):
    """
    Verifica se existe um caminho entre dois vértices.

    Retorna:
    True  -> existe um caminho.
    False -> não existe um caminho.
    """

    # Verifica se os dois vértices existem no grafo.
    if origem not in grafo or destino not in grafo:
        return False

    # Um vértice sempre possui um caminho até ele mesmo.
    if origem == destino:
        return True

    # Conjunto para armazenar os vértices visitados.
    visitados = {origem}

    # Fila utilizada pela BFS.
    fila = deque([origem])

    while fila:

        # Remove o primeiro vértice da fila.
        atual = fila.popleft()

        # Analisa os vizinhos do vértice atual.
        for vizinho in grafo[atual]:

            # Se o destino foi encontrado, existe um caminho.
            if vizinho == destino:
                return True

            # Adiciona apenas vértices ainda não visitados.
            if vizinho not in visitados:

                visitados.add(vizinho)
                fila.append(vizinho)

    # Se a busca terminou, o destino não foi encontrado.
    return False


# Define os vértices que serão analisados.
origem = "A"
destino = "F"

# Executa a verificação.
resultado = existe_caminho(grafo, origem, destino)

print("\n========== VERIFICAÇÃO DE CAMINHO ==========")

if resultado:
    print(f"Existe caminho entre {origem} e {destino}.")
else:
    print(f"Não existe caminho entre {origem} e {destino}.")