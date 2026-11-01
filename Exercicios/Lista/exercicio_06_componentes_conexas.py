# ============================================================
# EXERCÍCIO 06 — IDENTIFICAÇÃO DE COMPONENTES CONEXAS
# ============================================================
#
# ENUNCIADO:
# Implemente um programa que identifique todas as componentes
# conexas de um grafo não direcionado.
#
# O programa deverá:
# 1. Representar um grafo com diferentes grupos de vértices.
# 2. Identificar os vértices pertencentes a cada componente.
# 3. Exibir todas as componentes encontradas.
# 4. Informar a quantidade total de componentes conexas.
#
# CONCEITO:
# Uma componente conexa é um conjunto máximo de vértices
# no qual existe um caminho entre qualquer par de vértices.
#
# Será utilizada a DFS para explorar cada componente.
#
# Complexidade: O(V + E).
#
# ============================================================


grafo = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D"],
    "F": ["G"],
    "G": ["F"],
    "H": []
}


def dfs_componente(grafo, vertice, visitados, componente):
    """
    Percorre uma componente conexa utilizando DFS.

    Os vértices encontrados são armazenados na lista
    componente.
    """

    # Marca o vértice como visitado.
    visitados.add(vertice)

    # Adiciona o vértice à componente atual.
    componente.append(vertice)

    # Percorre os vizinhos do vértice.
    for vizinho in grafo[vertice]:

        # Explora somente os vértices ainda não visitados.
        if vizinho not in visitados:

            dfs_componente(
                grafo,
                vizinho,
                visitados,
                componente
            )


def encontrar_componentes(grafo):
    """
    Identifica todas as componentes conexas do grafo.
    """

    # Armazena todos os vértices já visitados.
    visitados = set()

    # Armazena as componentes encontradas.
    componentes = []

    # Percorre todos os vértices do grafo.
    for vertice in grafo:

        # Um vértice não visitado inicia uma nova componente.
        if vertice not in visitados:

            componente = []

            # Explora todos os vértices conectados a ele.
            dfs_componente(
                grafo,
                vertice,
                visitados,
                componente
            )

            # Armazena a componente completa.
            componentes.append(componente)

    return componentes


# Executa a identificação das componentes.
componentes = encontrar_componentes(grafo)

print("\n========== COMPONENTES CONEXAS ==========")

# Exibe cada componente encontrada.
for indice, componente in enumerate(componentes, start=1):

    print(f"Componente {indice}: {componente}")


# Exibe a quantidade total de componentes.
print(f"\nTotal de componentes: {len(componentes)}")