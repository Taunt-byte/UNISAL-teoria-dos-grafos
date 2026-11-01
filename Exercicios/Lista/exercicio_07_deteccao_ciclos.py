# ============================================================
# EXERCÍCIO 07 — DETECÇÃO DE CICLOS EM UM GRAFO
# ============================================================
#
# ENUNCIADO:
# Desenvolva um programa capaz de identificar se um grafo
# não direcionado possui pelo menos um ciclo.
#
# O programa deverá:
# 1. Representar um grafo utilizando lista de adjacência.
# 2. Percorrer os vértices utilizando DFS.
# 3. Identificar se existe um ciclo.
# 4. Exibir o resultado da verificação.
#
# CONCEITO:
# Um ciclo é um caminho que começa e termina no mesmo vértice,
# passando por pelo menos uma aresta.
#
# Na DFS de um grafo não direcionado, encontramos um ciclo
# quando visitamos um vértice que já foi visitado e que não
# corresponde ao pai do vértice atual.
#
# Complexidade: O(V + E).
#
# ============================================================


grafo = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["C", "E"],
    "E": ["D"]
}


def possui_ciclo_dfs(grafo, vertice, visitados, pai):
    """
    Verifica a existência de ciclos utilizando DFS.

    O parâmetro pai representa o vértice anterior na busca.

    Essa informação é necessária porque, em grafos não
    direcionados, cada aresta aparece nos dois sentidos.
    """

    # Marca o vértice atual como visitado.
    visitados.add(vertice)

    # Percorre todos os vizinhos.
    for vizinho in grafo[vertice]:

        # Caso o vizinho ainda não tenha sido visitado,
        # continua a busca recursivamente.
        if vizinho not in visitados:

            if possui_ciclo_dfs(
                grafo,
                vizinho,
                visitados,
                vertice
            ):
                return True

        # Se o vizinho já foi visitado e não é o pai,
        # encontramos uma conexão que forma um ciclo.
        elif vizinho != pai:

            return True

    # Nenhum ciclo foi encontrado neste caminho.
    return False


def possui_ciclo(grafo):
    """
    Verifica todos os componentes do grafo.

    Isso permite identificar ciclos mesmo quando
    o grafo não é conexo.
    """

    visitados = set()

    # Percorre todos os vértices.
    for vertice in grafo:

        # Inicia uma DFS para cada componente não visitada.
        if vertice not in visitados:

            if possui_ciclo_dfs(
                grafo,
                vertice,
                visitados,
                None
            ):
                return True

    return False


# Executa a detecção de ciclos.
resultado = possui_ciclo(grafo)

print("\n========== DETECÇÃO DE CICLOS ==========")

if resultado:
    print("O grafo possui pelo menos um ciclo.")
else:
    print("O grafo não possui ciclos.")