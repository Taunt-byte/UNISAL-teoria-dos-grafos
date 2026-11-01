
"""
============================================================
PROJETO: Algoritmo de Kruskal
LINGUAGEM: Python
AUTOR: Lucas Neves

DESCRICAO:
Implementacao do algoritmo de Kruskal para encontrar
a Arvore Geradora Minima (AGM) de um grafo ponderado.

FUNCIONALIDADES:
- Representacao do grafo por lista de arestas.
- Ordenacao das arestas pelo peso.
- Identificacao e prevencao de ciclos.
- Utilizacao da estrutura Union-Find (DSU).
- Calculo do custo total da arvore.

TIPO DE GRAFO:
- Nao direcionado.
- Ponderado.

COMPLEXIDADE:
O(E log E), considerando a ordenacao das arestas.
============================================================
"""


class UnionFind:
    """
    Estrutura de conjuntos disjuntos (Union-Find).

    Permite verificar se dois vertices pertencem ao
    mesmo conjunto e unir conjuntos diferentes.

    Utiliza:
    - Compressao de caminho.
    - Uniao por tamanho.
    """

    def __init__(self, quantidade_vertices):

        # Inicialmente, cada vertice e seu proprio pai.
        self.pai = list(range(quantidade_vertices))

        # Cada conjunto comeca contendo apenas um vertice.
        self.tamanho = [1] * quantidade_vertices

    def encontrar(self, vertice):
        """
        Encontra o representante do conjunto de um vertice.

        A compressao de caminho reduz a altura da estrutura,
        tornando futuras consultas mais eficientes.
        """

        if self.pai[vertice] != vertice:
            self.pai[vertice] = self.encontrar(
                self.pai[vertice]
            )

        return self.pai[vertice]

    def unir(self, a, b):
        """
        Une os conjuntos dos vertices a e b.

        Retorna:
        True: os conjuntos foram unidos.
        False: os vertices ja pertenciam ao mesmo conjunto.
        """

        raiz_a = self.encontrar(a)
        raiz_b = self.encontrar(b)

        # Se as raizes forem iguais, a aresta formaria um ciclo.
        if raiz_a == raiz_b:
            return False

        # O conjunto menor sera unido ao maior.
        if self.tamanho[raiz_a] < self.tamanho[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a

        self.pai[raiz_b] = raiz_a
        self.tamanho[raiz_a] += self.tamanho[raiz_b]

        return True


def algoritmo_kruskal(quantidade_vertices, arestas):
    """
    Encontra a Arvore Geradora Minima utilizando Kruskal.

    Parametros:
    quantidade_vertices: quantidade de vertices do grafo.
    arestas: lista de tuplas (origem, destino, peso).

    Retorna:
    Uma lista com as arestas selecionadas e o custo total.
    """

    # Cria a estrutura de conjuntos disjuntos.
    uf = UnionFind(quantidade_vertices)

    # Ordena as arestas pelo peso, em ordem crescente.
    arestas_ordenadas = sorted(arestas, key=lambda aresta: aresta[2])

    # Armazena as arestas selecionadas.
    arvore_minima = []

    # Acumula o peso total da arvore.
    custo_total = 0

    # Percorre as arestas ordenadas.
    for origem, destino, peso in arestas_ordenadas:

        # Tenta unir os conjuntos dos dois vertices.
        if uf.unir(origem, destino):

            arvore_minima.append((origem, destino, peso))
            custo_total += peso

            # Uma AGM possui exatamente V - 1 arestas.
            if len(arvore_minima) == quantidade_vertices - 1:
                break

    return arvore_minima, custo_total


def main():

    # Quantidade de vertices do grafo.
    quantidade_vertices = 5

    # Representacao do grafo por lista de arestas.
    #
    # Cada tupla possui:
    # (vertice de origem, vertice de destino, peso)
    arestas = [
        (0, 1, 2),
        (0, 3, 6),
        (1, 2, 3),
        (1, 3, 8),
        (1, 4, 5),
        (2, 4, 7),
        (3, 4, 9)
    ]

    # Executa o algoritmo de Kruskal.
    arvore_minima, custo_total = algoritmo_kruskal(
        quantidade_vertices,
        arestas
    )

    # Exibe os resultados.
    print("\n========== ALGORITMO DE KRUSKAL ==========")
    print("Arestas selecionadas:\n")

    for origem, destino, peso in arvore_minima:
        print(f"{origem} -- {destino} | Peso: {peso}")

    print("\n------------------------------------------")

    # Verifica se o grafo e conexo.
    if len(arvore_minima) == quantidade_vertices - 1:

        print(f"Custo total da AGM: {custo_total}")

    else:

        print("O grafo nao e conexo.")
        print("Foi encontrada uma floresta geradora minima.")
        print(f"Custo total da floresta: {custo_total}")


if __name__ == "__main__":
    main()
