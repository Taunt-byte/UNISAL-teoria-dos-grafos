
"""
===========================================================
Projeto: Teoria dos Grafos
Assunto: Algoritmos de Grafos
Algoritmo: Prim
Estrutura: Lista de Adjacência com Pesos

Descrição:
    O programa implementa o algoritmo de Prim, utilizado
    para encontrar uma Árvore Geradora Mínima (AGM) em
    um grafo ponderado, não direcionado e conexo.

    Uma Árvore Geradora Mínima conecta todos os vértices
    do grafo sem formar ciclos, buscando minimizar a soma
    dos pesos de todas as arestas utilizadas.

Funcionamento:
    1. Escolhe um vértice inicial.
    2. Adiciona o vértice à árvore geradora.
    3. Analisa as arestas que conectam a árvore aos
       vértices ainda não visitados.
    4. Seleciona a aresta de menor peso.
    5. Repete o processo até alcançar todos os vértices
       da componente conexa.

Estruturas utilizadas:
    - Lista de adjacência: armazena os vértices e arestas.
    - Heap de prioridade: seleciona a menor aresta disponível.
    - Lista de visitados: controla os vértices já adicionados.
    - Lista de arestas: registra as conexões selecionadas.

Complexidade:
    Tempo: O(E log V), em grafos simples.
    Espaço: O(V + E).

Autor: Lucas Neves
===========================================================
"""

# Importa as operações de fila de prioridade.
#
# heappush(): adiciona elementos ao heap.
# heappop(): remove e retorna o elemento de menor prioridade.
#
# O heap permite selecionar eficientemente a menor aresta
# disponível durante a execução do algoritmo.

from heapq import heappop, heappush


# =========================================================
# FUNÇÃO: ADICIONAR ARESTA
# =========================================================

def adicionar_aresta(grafo, origem, destino, peso):
    """
    Adiciona uma aresta ponderada ao grafo.

    Parâmetros:
        grafo: lista de adjacência.
        origem: vértice de origem.
        destino: vértice de destino.
        peso: custo ou distância da conexão.

    Como o grafo é não direcionado, a conexão é registrada
    nos dois sentidos.
    """

    # Registra a conexão da origem para o destino.
    grafo[origem].append((destino, peso))

    # Registra a conexão inversa.
    grafo[destino].append((origem, peso))


# =========================================================
# FUNÇÃO AUXILIAR: EXECUTAR PRIM EM UMA COMPONENTE
# =========================================================

def _prim_componente(grafo, inicio, arestas, visitados):
    """
    Executa o algoritmo de Prim a partir de um vértice inicial.

    Parâmetros:
        grafo: lista de adjacência ponderada.
        inicio: vértice inicial da busca.
        arestas: registra a melhor conexão encontrada
                 para cada vértice.
        visitados: indica quais vértices já foram processados.

    A função modifica as listas arestas e visitados.
    """

    # Define o vértice inicial como raiz da árvore.
    #
    # (0, None) indica que ele não possui vértice predecessor
    # dentro da árvore geradora.
    arestas[inicio] = (0, None)

    # Inicializa o heap com o vértice inicial e peso zero.
    #
    # Cada elemento possui o formato:
    # (peso_da_aresta, vertice)
    heap = [(0, inicio)]

    # Continua enquanto existirem vértices disponíveis.
    while heap:

        # Remove o vértice associado ao menor peso.
        peso, vertice = heappop(heap)

        # Ignora vértices que já foram processados.
        #
        # Isso evita processar novamente um vértice
        # que tenha sido inserido várias vezes no heap.
        if visitados[vertice]:
            continue

        # Marca o vértice como visitado.
        visitados[vertice] = True

        # Percorre todas as conexões do vértice atual.
        #
        # Cada conexão possui:
        # (vertice_adjacente, peso_da_aresta)
        for vizinho, peso_aresta in grafo[vertice]:

            # Verifica se o vizinho ainda não foi visitado.
            if not visitados[vizinho]:

                # Verifica se ainda não existe uma conexão
                # registrada para o vizinho ou se a nova
                # aresta possui um peso menor.
                #
                # Isso permite encontrar a conexão de menor
                # custo para incorporar o vizinho à árvore.
                if (
                    arestas[vizinho] is None
                    or peso_aresta < arestas[vizinho][0]
                ):

                    # Atualiza a melhor conexão encontrada.
                    #
                    # Formato:
                    # (peso_da_aresta, vertice_predecessor)
                    arestas[vizinho] = (peso_aresta, vertice)

                    # Insere a nova possibilidade no heap.
                    heappush(heap, (peso_aresta, vizinho))


# =========================================================
# FUNÇÃO PRINCIPAL: ALGORITMO DE PRIM
# =========================================================

def prim(grafo, inicio=0):
    """
    Encontra uma Árvore Geradora Mínima utilizando Prim.

    O algoritmo considera somente a componente conexa
    que contém o vértice inicial.

    Parâmetros:
        grafo: lista de adjacência ponderada.
        inicio: vértice utilizado para iniciar o algoritmo.

    Retorno:
        Lista contendo a melhor aresta utilizada para
        conectar cada vértice à árvore geradora.

        Cada elemento possui o formato:
        (peso_da_aresta, vertice_predecessor)

        Caso um vértice não seja alcançável, retorna None.
    """

    # Obtém a quantidade de vértices do grafo.
    quantidade_vertices = len(grafo)

    # Verifica se o grafo está vazio.
    if quantidade_vertices == 0:
        return []

    # Verifica se o vértice inicial é válido.
    if not 0 <= inicio < quantidade_vertices:
        raise ValueError("Vértice inicial inválido.")

    # Inicializa a lista de arestas.
    #
    # None indica que ainda não foi encontrada uma conexão
    # para alcançar determinado vértice.
    arestas = [None] * quantidade_vertices

    # Inicializa o controle de vértices visitados.
    #
    # False: vértice ainda não processado.
    # True: vértice já incorporado à árvore.
    visitados = [False] * quantidade_vertices

    # Executa Prim a partir do vértice informado.
    _prim_componente(grafo, inicio, arestas, visitados)

    # Retorna as conexões selecionadas pelo algoritmo.
    return arestas


# =========================================================
# FUNÇÃO ADICIONAL: PRIM PARA GRAFOS DESCONEXOS
# =========================================================

def prim_desconexo(grafo):
    """
    Calcula uma Floresta Geradora Mínima para um grafo
    que pode possuir várias componentes conexas.

    Diferentemente de prim(), esta função percorre
    todas as componentes do grafo.

    Cada componente recebe seu próprio vértice raiz.

    Retorno:
        Lista de arestas selecionadas para cada vértice.
    """

    # Obtém a quantidade de vértices.
    quantidade_vertices = len(grafo)

    # Inicializa as estruturas utilizadas pelo algoritmo.
    arestas = [None] * quantidade_vertices
    visitados = [False] * quantidade_vertices

    # Percorre todos os vértices do grafo.
    for vertice in range(quantidade_vertices):

        # Se o vértice ainda não foi visitado,
        # significa que pertence a uma componente
        # que ainda não foi processada.
        if not visitados[vertice]:

            # Executa Prim a partir desse vértice.
            #
            # As listas são compartilhadas entre as chamadas,
            # permitindo construir uma floresta geradora.
            _prim_componente(
                grafo,
                vertice,
                arestas,
                visitados
            )

    # Retorna as arestas da floresta geradora mínima.
    return arestas


# =========================================================
# DEFINIÇÃO DO GRAFO
# =========================================================

# Cria um grafo com seis vértices.
#
# Cada posição da lista representa um vértice.
# Cada tupla representa:
# (vértice adjacente, peso da aresta).

grafo = [[] for _ in range(6)]


# Adiciona as conexões ponderadas ao grafo.

adicionar_aresta(grafo, 0, 1, 4)
adicionar_aresta(grafo, 0, 2, 3)
adicionar_aresta(grafo, 1, 2, 1)
adicionar_aresta(grafo, 1, 3, 2)
adicionar_aresta(grafo, 2, 3, 4)
adicionar_aresta(grafo, 3, 4, 2)
adicionar_aresta(grafo, 4, 5, 6)
adicionar_aresta(grafo, 3, 5, 5)


# =========================================================
# EXECUÇÃO DO ALGORITMO
# =========================================================

# Executa Prim a partir do vértice 0.
resultado = prim(grafo, inicio=0)


# =========================================================
# EXIBIÇÃO DA ÁRVORE GERADORA MÍNIMA
# =========================================================

print("\n========== ÁRVORE GERADORA MÍNIMA ==========")

# Inicializa a variável que armazenará o peso total.
peso_total = 0

# Percorre os resultados obtidos pelo algoritmo.
for vertice, conexao in enumerate(resultado):

    # O vértice inicial não possui predecessor.
    if conexao is None:
        print(f"Vértice {vertice}: não alcançado.")

    elif conexao[1] is None:
        print(f"Vértice {vertice}: raiz da árvore.")

    else:
        # Separa o peso e o vértice predecessor.
        peso, predecessor = conexao

        # Exibe a aresta selecionada.
        print(
            f"{predecessor} -> {vertice} "
            f"| Peso: {peso}"
        )

        # Acumula o peso da árvore geradora.
        peso_total += peso


# Exibe a soma dos pesos das arestas selecionadas.
print("\nPeso total da Árvore Geradora Mínima:", peso_total)


# =========================================================
# EXECUÇÃO PARA GRAFOS DESCONEXOS (OPCIONAL)
# =========================================================

# Para testar um grafo desconexo, utilize:
#
# resultado = prim_desconexo(grafo)
#
# Nesse caso, o algoritmo encontrará uma Floresta
# Geradora Mínima, processando todas as componentes.
