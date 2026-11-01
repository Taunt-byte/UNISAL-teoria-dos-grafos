
"""
===========================================================
Projeto: Teoria dos Grafos
Assunto: Algoritmos de Grafos
Algoritmo: Prim
Estrutura: Grafo utilizando NetworkX

Descrição:
    O programa implementa o algoritmo de Prim para encontrar
    uma Árvore Geradora Mínima (AGM) em um grafo ponderado
    e não direcionado.

    A implementação utiliza a biblioteca NetworkX para
    representar os vértices e as arestas do grafo.

    O algoritmo seleciona progressivamente as arestas de
    menor peso, conectando novos vértices à árvore geradora
    sem formar ciclos.

Funcionalidades:
    1. Representar um grafo utilizando NetworkX.
    2. Consultar os vizinhos de cada vértice.
    3. Encontrar a aresta de menor peso disponível.
    4. Construir uma Árvore Geradora Mínima.
    5. Exibir as conexões selecionadas e o peso total.

Estruturas utilizadas:
    - NetworkX: representação do grafo.
    - Lista open_node: vértices candidatos à expansão.
    - Lista closed_node: vértices já processados.
    - Lista w: menor peso conhecido para alcançar cada vértice.
    - Lista t: predecessor de cada vértice na árvore.

Complexidade:
    Tempo: O(V² + E), na implementação com busca linear.
    Espaço: O(V + E).

Autor: Lucas Neves
===========================================================
"""


# Importa a biblioteca responsável pela representação
# e manipulação de grafos.
import networkx as nx


# =========================================================
# FUNÇÃO AUXILIAR: ENCONTRAR O VÉRTICE DE MENOR PESO
# =========================================================

def node_min(open_node, w):
    """
    Encontra o vértice com o menor peso na lista de candidatos.

    Parâmetros:
        open_node: vértices que ainda podem ser processados.
        w: lista contendo o menor peso conhecido de cada vértice.

    Retorno:
        Vértice que apresenta o menor peso acumulado.
    """

    # Seleciona o vértice cuja posição na lista w
    # apresenta o menor valor.
    return min(open_node, key=lambda node: w[node])


# =========================================================
# FUNÇÃO PRINCIPAL: ALGORITMO DE PRIM
# =========================================================

def prim(g, init):
    """
    Executa o algoritmo de Prim em um grafo ponderado.

    Parâmetros:
        g: grafo não direcionado criado com NetworkX.
        init: vértice inicial da árvore geradora.

    Retorno:
        Uma lista de arestas no formato:
        (predecessor, vertice, peso).

    Observação:
        Esta implementação calcula a árvore geradora mínima
        somente da componente conexa do vértice inicial.
    """

    # Lista de vértices candidatos.
    #
    # Representa os vértices que ainda podem ser selecionados
    # para integrar a árvore geradora.
    open_node = []

    # Lista de vértices já incorporados à árvore.
    #
    # Impede que o algoritmo processe um vértice novamente
    # e evita a formação de ciclos.
    closed_node = []

    # Lista que armazena o menor peso conhecido para
    # conectar cada vértice à árvore geradora.
    #
    # Inicialmente, todos recebem infinito, pois ainda
    # não existe uma conexão conhecida.
    w = {}

    # Lista que armazena o predecessor de cada vértice.
    #
    # O predecessor representa o vértice anterior que
    # oferece a conexão de menor peso.
    t = {}

    # Percorre todos os vértices existentes no grafo.
    for node in g.nodes:

        # Inicializa a distância de cada vértice como infinito.
        w[node] = float('inf')

        # Inicialmente, nenhum vértice possui predecessor.
        t[node] = None

    # Define o peso do vértice inicial como zero.
    #
    # Isso permite que ele seja escolhido primeiro.
    w[init] = 0

    # Adiciona o vértice inicial à lista de candidatos.
    open_node.append(init)

    # Continua enquanto existirem vértices candidatos.
    while open_node:

        # Seleciona o vértice com o menor peso.
        n = node_min(open_node, w)

        # Remove o vértice da lista de candidatos.
        open_node.remove(n)

        # Adiciona o vértice à lista de processados.
        closed_node.append(n)

        # Percorre todos os vizinhos do vértice atual.
        for e in g.neighbors(n):

            # Verifica se o vizinho ainda não foi incorporado
            # à árvore geradora.
            #
            # Também verifica se a aresta atual possui peso
            # menor do que a melhor conexão conhecida.
            if e not in closed_node and w[e] > g[n][e]['weight']:

                # Adiciona o vizinho à lista de candidatos,
                # caso ele ainda não esteja presente.
                if e not in open_node:
                    open_node.append(e)

                # Atualiza o predecessor do vizinho.
                t[e] = n

                # Atualiza o menor peso conhecido.
                w[e] = g[n][e]['weight']

    # Organiza as arestas selecionadas para a árvore.
    resultado = []

    # Percorre todos os vértices e seus predecessores.
    for node in g.nodes:

        # O vértice inicial não possui predecessor.
        if t[node] is not None:

            # Obtém o peso da conexão entre o vértice
            # e seu respectivo predecessor.
            peso = g[t[node]][node]['weight']

            # Armazena a aresta selecionada.
            resultado.append((t[node], node, peso))

    # Retorna as arestas da árvore geradora mínima.
    return resultado


# =========================================================
# DEFINIÇÃO DO GRAFO
# =========================================================

# Cria um grafo não direcionado.
grafo = nx.Graph()

# Adiciona as arestas e seus respectivos pesos.
#
# Formato:
# (origem, destino, peso)

grafo.add_weighted_edges_from([
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6),
    (3, 5, 5)
])


# =========================================================
# EXECUÇÃO DO ALGORITMO
# =========================================================

# Define o vértice inicial.
vertice_inicial = 0

# Executa o algoritmo de Prim.
resultado = prim(grafo, vertice_inicial)


# =========================================================
# EXIBIÇÃO DA ÁRVORE GERADORA MÍNIMA
# =========================================================

print("\n========== ÁRVORE GERADORA MÍNIMA ==========")

# Inicializa a variável que armazenará o peso total.
peso_total = 0

# Percorre as arestas selecionadas.
for origem, destino, peso in resultado:

    # Exibe cada conexão escolhida pelo algoritmo.
    print(f"{origem} -> {destino} | Peso: {peso}")

    # Soma o peso da aresta ao custo total.
    peso_total += peso


# Exibe o custo total da árvore geradora mínima.
print("\nPeso total da AGM:", peso_total)
