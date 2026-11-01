# ============================================================
# EXERCÍCIO 08 — VERIFICAÇÃO DE UMA ÁRVORE
# ============================================================
#
# ENUNCIADO:
# Desenvolva um programa que verifique se um grafo
# não direcionado é uma árvore.
#
# O programa deverá:
# 1. Representar um grafo por lista de adjacência.
# 2. Verificar se o grafo é conexo.
# 3. Verificar se possui exatamente V - 1 arestas.
# 4. Informar se o grafo representa uma árvore.
#
# CONCEITO:
# Uma árvore é um grafo não direcionado, conexo e acíclico.
#
# Uma propriedade importante das árvores é:
#
#             E = V - 1
#
# Onde:
# V = quantidade de vértices.
# E = quantidade de arestas.
#
# Para um grafo não direcionado, ser conexo e possuir
# exatamente V - 1 arestas é suficiente para ser uma árvore.
#
# Complexidade: O(V + E).
#
# ============================================================


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B", "E"],
    "E": ["D"]
}


def verificar_conectividade(grafo):
    """
    Verifica se todos os vértices são alcançáveis
    a partir do primeiro vértice.
    """

    if not grafo:
        return False

    # Seleciona um vértice inicial.
    inicio = next(iter(grafo))

    # Conjunto de vértices visitados.
    visitados = set()

    # Pilha utilizada para executar DFS iterativa.
    pilha = [inicio]

    while pilha:

        atual = pilha.pop()

        if atual not in visitados:

            visitados.add(atual)

            # Adiciona os vizinhos à pilha.
            for vizinho in grafo[atual]:

                if vizinho not in visitados:
                    pilha.append(vizinho)

    # O grafo é conexo se todos os vértices foram visitados.
    return len(visitados) == len(grafo)


def contar_arestas(grafo):
    """
    Conta as arestas do grafo.

    Como o grafo é não direcionado, cada aresta aparece
    duas vezes na lista de adjacência.

    Por isso, dividimos a soma dos graus por dois.
    """

    soma_graus = sum(
        len(vizinhos)
        for vizinhos in grafo.values()
    )

    return soma_graus // 2


def verificar_arvore(grafo):
    """
    Verifica se o grafo satisfaz as condições de uma árvore.
    """

    quantidade_vertices = len(grafo)

    quantidade_arestas = contar_arestas(grafo)

    # Uma árvore precisa possuir pelo menos um vértice.
    if quantidade_vertices == 0:
        return False

    # Verifica a quantidade de arestas.
    if quantidade_arestas != quantidade_vertices - 1:
        return False

    # Verifica se o grafo é conexo.
    if not verificar_conectividade(grafo):
        return False

    return True


# Executa a verificação.
print("\n========== VERIFICAÇÃO DE ÁRVORE ==========")

print(f"Vértices: {len(grafo)}")
print(f"Arestas: {contar_arestas(grafo)}")

if verificar_arvore(grafo):
    print("O grafo é uma árvore.")
else:
    print("O grafo não é uma árvore.")