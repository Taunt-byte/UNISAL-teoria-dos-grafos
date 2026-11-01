# ============================================================
# EXERCÍCIO 02 — CÁLCULO DO GRAU DOS VÉRTICES
# ============================================================
#
# ENUNCIADO:
# Considere um grafo não direcionado representado por uma
# lista de adjacência.
#
# Desenvolva um programa que:
# 1. Represente um grafo com cinco vértices.
# 2. Calcule o grau de cada vértice.
# 3. Identifique o vértice com maior grau.
#
# CONCEITO:
# O grau de um vértice corresponde à quantidade de arestas
# incidentes nele.
#
# Em um grafo não direcionado, o grau pode ser calculado
# contando os vizinhos de cada vértice.
#
# ============================================================


grafo = {
    "A": ["B", "C", "D"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["A", "C", "E"],
    "E": ["D"]
}


def calcular_graus(grafo):
    """
    Calcula e exibe o grau de cada vértice.

    O método len() retorna a quantidade de vizinhos
    armazenados na lista de adjacência.
    """

    print("\n========== GRAU DOS VÉRTICES ==========")

    for vertice, vizinhos in grafo.items():

        grau = len(vizinhos)

        print(f"Vértice {vertice}: grau {grau}")


def encontrar_maior_grau(grafo):
    """
    Identifica o vértice que possui o maior grau.

    A função max() utiliza como critério a quantidade
    de vizinhos de cada vértice.
    """

    maior_vertice = max(
        grafo,
        key=lambda vertice: len(grafo[vertice])
    )

    maior_grau = len(grafo[maior_vertice])

    print("\n========== MAIOR GRAU ==========")

    print(f"Vértice: {maior_vertice}")
    print(f"Grau: {maior_grau}")


# Executa as funções.
calcular_graus(grafo)

encontrar_maior_grau(grafo)