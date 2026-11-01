# ============================================================
# EXERCÍCIO 04 — BUSCA EM PROFUNDIDADE (DFS)
# ============================================================
#
# ENUNCIADO:
# Implemente o algoritmo de Busca em Profundidade
# (Depth-First Search) utilizando recursividade.
#
# O programa deverá:
# 1. Representar um grafo por lista de adjacência.
# 2. Receber um vértice inicial.
# 3. Visitar os vértices aprofundando-se em cada caminho.
# 4. Exibir a ordem de visitação.
#
# CONCEITO:
# A DFS explora um caminho até não encontrar mais vértices
# não visitados. Depois, retorna para explorar outros caminhos.
#
# A implementação utiliza uma função recursiva.
#
# Complexidade com lista de adjacência: O(V + E).
#
# ============================================================


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


def busca_profundidade(grafo, vertice, visitados):
    """
    Executa a DFS recursivamente.

    Parâmetros:
    grafo     -> estrutura do grafo.
    vertice   -> vértice atualmente visitado.
    visitados -> conjunto que armazena os vértices visitados.
    """

    # Marca o vértice atual como visitado.
    visitados.add(vertice)

    # Exibe o vértice atual.
    print(vertice, end=" -> ")

    # Percorre os vizinhos do vértice atual.
    for vizinho in grafo[vertice]:

        # Continua a busca apenas em vértices não visitados.
        if vizinho not in visitados:

            # Chamada recursiva para aprofundar a busca.
            busca_profundidade(grafo, vizinho, visitados)


def executar_dfs(grafo, inicio):
    """
    Inicializa a busca em profundidade.
    """

    if inicio not in grafo:
        print("Vértice inicial não encontrado.")
        return

    # Conjunto vazio para controlar os vértices visitados.
    visitados = set()

    print("\n========== PERCURSO DFS ==========")

    # Inicia a busca pelo vértice informado.
    busca_profundidade(grafo, inicio, visitados)

    print("FIM")


# Executa a DFS começando pelo vértice A.
executar_dfs(grafo, "A")