# ============================================================
# EXERCÍCIO 03 — BUSCA EM LARGURA (BFS)
# ============================================================
#
# ENUNCIADO:
# Implemente o algoritmo de Busca em Largura (Breadth-First
# Search), utilizando uma fila para percorrer um grafo.
#
# O programa deverá:
# 1. Representar um grafo por lista de adjacência.
# 2. Receber um vértice inicial.
# 3. Percorrer o grafo visitando os vértices por níveis.
# 4. Exibir a ordem em que os vértices foram visitados.
#
# CONCEITO:
# A BFS explora primeiro os vértices mais próximos da origem.
#
# Utiliza uma fila (FIFO):
# First In, First Out.
#
# Complexidade com lista de adjacência: O(V + E).
#
# ============================================================


from collections import deque


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}


def busca_largura(grafo, inicio):
    """
    Executa a Busca em Largura a partir de um vértice.

    Parâmetros:
    grafo  -> dicionário contendo a lista de adjacência.
    inicio -> vértice inicial da busca.
    """

    # Verifica se o vértice inicial existe.
    if inicio not in grafo:
        print("Vértice inicial não encontrado.")
        return

    # Conjunto utilizado para registrar os vértices visitados.
    visitados = set()

    # Fila responsável por controlar a ordem da busca.
    fila = deque()

    # O vértice inicial é marcado como visitado.
    visitados.add(inicio)

    # Insere o vértice inicial na fila.
    fila.append(inicio)

    print("\n========== PERCURSO BFS ==========")

    # Continua enquanto existirem vértices na fila.
    while fila:

        # Remove o primeiro elemento da fila.
        vertice = fila.popleft()

        print(vertice, end=" -> ")

        # Percorre todos os vizinhos do vértice atual.
        for vizinho in grafo[vertice]:

            # Verifica se o vizinho ainda não foi visitado.
            if vizinho not in visitados:

                # Marca o vizinho como visitado.
                visitados.add(vizinho)

                # Adiciona o vizinho ao final da fila.
                fila.append(vizinho)

    print("FIM")


# Executa a busca começando pelo vértice A.
busca_largura(grafo, "A")