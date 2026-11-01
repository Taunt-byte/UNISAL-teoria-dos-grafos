# ============================================================
# EXERCÍCIO 10 — ÁRVORE GERADORA MÍNIMA (KRUSKAL)
# ============================================================
#
# ENUNCIADO:
# Implemente o algoritmo de Kruskal para encontrar a Árvore
# Geradora Mínima (AGM) de um grafo não direcionado e ponderado.
#
# O programa deverá:
# 1. Representar um grafo utilizando uma lista de arestas.
# 2. Ordenar as arestas pelo peso em ordem crescente.
# 3. Selecionar as arestas de menor peso.
# 4. Evitar a formação de ciclos.
# 5. Exibir as arestas selecionadas e o custo total da AGM.
#
# CONCEITO:
# Uma Árvore Geradora Mínima é uma árvore que conecta
# todos os vértices de um grafo conexo, utilizando o menor
# custo total possível.
#
# Kruskal utiliza a estrutura Union-Find para identificar
# se dois vértices já pertencem ao mesmo conjunto.
#
# Complexidade: O(E log E).
#
# ============================================================


# Lista de vértices do grafo.
vertices = ["A", "B", "C", "D", "E"]


# Lista de arestas no formato:
# (origem, destino, peso)
arestas = [
    ("A", "B", 2),
    ("A", "D", 6),
    ("B", "C", 3),
    ("B", "D", 8),
    ("B", "E", 5),
    ("C", "E", 7),
    ("D", "E", 9)
]


class UnionFind:
    """
    Implementação da estrutura Union-Find.

    Essa estrutura controla os conjuntos de vértices
    utilizados durante a construção da AGM.

    find() identifica o representante de um conjunto.

    union() une dois conjuntos diferentes.
    """

    def __init__(self, vertices):

        # Inicialmente, cada vértice pertence ao próprio conjunto.
        self.pai = {
            vertice: vertice
            for vertice in vertices
        }

        # Armazena o tamanho de cada conjunto.
        self.tamanho = {
            vertice: 1
            for vertice in vertices
        }

    def find(self, vertice):
        """
        Encontra o representante do conjunto.

        A compressão de caminho aproxima a complexidade
        das operações de uma constante amortizada.
        """

        # Se o vértice não é seu próprio pai,
        # continua procurando o representante.
        if self.pai[vertice] != vertice:

            # Atualiza o pai diretamente para o representante.
            self.pai[vertice] = self.find(
                self.pai[vertice]
            )

        return self.pai[vertice]

    def union(self, vertice_a, vertice_b):
        """
        Une os conjuntos de dois vértices.

        Utiliza união por tamanho:
        o conjunto menor é incorporado ao maior.

        Retorna:
        True  -> os conjuntos foram unidos.
        False -> os vértices já pertenciam ao mesmo conjunto.
        """

        # Encontra os representantes dos dois conjuntos.
        raiz_a = self.find(vertice_a)
        raiz_b = self.find(vertice_b)

        # Se as raízes são iguais, existe um ciclo potencial.
        if raiz_a == raiz_b:
            return False

        # Mantém a raiz do maior conjunto.
        if self.tamanho[raiz_a] < self.tamanho[raiz_b]:

            raiz_a, raiz_b = raiz_b, raiz_a

        # Une o conjunto menor ao conjunto maior.
        self.pai[raiz_b] = raiz_a

        # Atualiza o tamanho do conjunto resultante.
        self.tamanho[raiz_a] += self.tamanho[raiz_b]

        return True


def kruskal(vertices, arestas):
    """
    Executa o algoritmo de Kruskal.

    Retorna:
    arvore -> lista de arestas selecionadas.
    custo  -> custo total da árvore geradora mínima.
    """

    # Ordena as arestas pelo peso em ordem crescente.
    arestas_ordenadas = sorted(
        arestas,
        key=lambda aresta: aresta[2]
    )

    # Inicializa a estrutura Union-Find.
    conjuntos = UnionFind(vertices)

    # Armazena as arestas selecionadas.
    arvore = []

    # Acumula o custo total da AGM.
    custo_total = 0

    # Analisa as arestas da menor para a maior.
    for origem, destino, peso in arestas_ordenadas:

        # Tenta unir os conjuntos dos dois vértices.
        # Se já estiverem no mesmo conjunto, a aresta
        # não será adicionada, pois formaria um ciclo.
        if conjuntos.union(origem, destino):

            # Adiciona a aresta à árvore.
            arvore.append((origem, destino, peso))

            # Atualiza o custo total.
            custo_total += peso

            # Uma árvore com V vértices possui V - 1 arestas.
            if len(arvore) == len(vertices) - 1:
                break

    return arvore, custo_total


# Executa o algoritmo.
arvore, custo = kruskal(vertices, arestas)

print("\n========== ALGORITMO DE KRUSKAL ==========")

print("\nArestas selecionadas:")

# Exibe as arestas que compõem a AGM.
for origem, destino, peso in arvore:

    print(f"{origem} -- {destino} | Peso: {peso}")


print("\n========== RESULTADO ==========")

# Verifica se todos os vértices foram conectados.
if len(arvore) == len(vertices) - 1:

    print(f"Custo total da AGM: {custo}")

else:

    print("O grafo não é conexo.")
    print("Foi encontrada uma floresta geradora mínima.")
    print(f"Custo total: {custo}")