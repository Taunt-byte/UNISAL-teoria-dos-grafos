# ============================================================
# DESAFIO 03 — FLUXO MÁXIMO COM EDMONDS-KARP
# ============================================================
#
# ENUNCIADO:
# Desenvolva um programa que calcule o fluxo máximo possível
# entre uma origem e um destino em uma rede direcionada.
#
# Imagine uma rede de distribuição na qual:
#
# - Os vértices representam centros de distribuição.
# - As arestas representam conexões entre os centros.
# - Os pesos representam a capacidade máxima de transporte.
#
# O programa deverá:
# 1. Representar uma rede utilizando uma matriz de capacidades.
# 2. Receber um vértice de origem.
# 3. Receber um vértice de destino.
# 4. Encontrar caminhos com capacidade residual disponível.
# 5. Atualizar as capacidades residuais.
# 6. Calcular o fluxo máximo da rede.
# 7. Exibir os caminhos utilizados e seus respectivos fluxos.
#
# CONCEITOS:
# O problema de fluxo máximo busca determinar a maior
# quantidade de fluxo que pode sair da origem e chegar
# ao destino sem ultrapassar a capacidade das arestas.
#
# O algoritmo Edmonds-Karp é uma implementação do método
# de Ford-Fulkerson que utiliza BFS para encontrar caminhos
# aumentantes com o menor número de arestas.
#
# Capacidade residual:
# Quantidade adicional de fluxo que ainda pode passar
# por uma conexão.
#
# Caminho aumentante:
# Caminho entre origem e destino em que todas as arestas
# possuem capacidade residual positiva.
#
# Complexidade: O(V * E²).
#
# ============================================================


from collections import deque


# ============================================================
# REPRESENTAÇÃO DA REDE
# ============================================================

# Os vértices representam centros de distribuição.
vertices = [
    "Origem",
    "A",
    "B",
    "C",
    "D",
    "Destino"
]


# Matriz de capacidades.
#
# Cada posição representa a capacidade de uma aresta:
#
# capacidade[origem][destino]
#
# O valor zero significa que não existe uma conexão
# direcionada com capacidade disponível nessa posição.
#
# Os índices correspondem à ordem da lista vertices.
capacidades = [
    # O   A   B   C   D   T
    [ 0, 16, 13,  0,  0,  0 ],  # Origem
    [ 0,  0, 10, 12,  0,  0 ],  # A
    [ 0,  4,  0,  0, 14,  0 ],  # B
    [ 0,  0,  9,  0,  0, 20 ],  # C
    [ 0,  0,  0,  7,  0,  4 ],  # D
    [ 0,  0,  0,  0,  0,  0 ]   # Destino
]


def encontrar_caminho_bfs(
    residual,
    origem,
    destino,
    quantidade_vertices
):
    """
    Procura um caminho aumentante utilizando BFS.

    A busca considera apenas arestas que possuem
    capacidade residual maior que zero.

    Retorna:
    True  -> encontrou um caminho até o destino.
    False -> não existe caminho aumentante.
    """

    # Registra o antecessor de cada vértice.
    # O valor -1 representa ausência de antecessor.
    pai = [-1] * quantidade_vertices

    # Marca a origem como seu próprio antecessor.
    pai[origem] = origem

    # Inicializa a fila com o vértice de origem.
    fila = deque([origem])

    while fila:

        # Retira o primeiro vértice da fila.
        atual = fila.popleft()

        # Analisa todos os possíveis destinos.
        for vizinho in range(quantidade_vertices):

            # Verifica se existe capacidade residual
            # e se o vértice ainda não foi visitado.
            if (
                residual[atual][vizinho] > 0
                and pai[vizinho] == -1
            ):

                # Registra de onde chegamos ao vizinho.
                pai[vizinho] = atual

                # Se encontramos o destino, o caminho existe.
                if vizinho == destino:

                    return True, pai

                # Adiciona o vizinho à fila.
                fila.append(vizinho)

    # Nenhum caminho aumentante foi encontrado.
    return False, pai


def edmonds_karp(
    capacidades,
    origem,
    destino,
    vertices
):
    """
    Calcula o fluxo máximo utilizando Edmonds-Karp.

    Parâmetros:
    capacidades -> matriz de capacidades da rede.
    origem      -> índice do vértice de origem.
    destino     -> índice do vértice de destino.
    vertices    -> lista de identificação dos vértices.

    Retorna:
    fluxo_maximo -> quantidade máxima de fluxo.
    caminhos     -> caminhos aumentantes utilizados.
    """

    quantidade_vertices = len(vertices)

    # Cria uma cópia da matriz original.
    #
    # A matriz residual será modificada durante o algoritmo,
    # preservando a matriz original de capacidades.
    residual = [
        linha.copy()
        for linha in capacidades
    ]

    # Armazena o fluxo máximo encontrado.
    fluxo_maximo = 0

    # Armazena os caminhos utilizados durante o cálculo.
    caminhos = []

    # ========================================================
    # ETAPA 1 — PROCURA DE CAMINHOS AUMENTANTES
    # ========================================================

    while True:

        # Procura um caminho entre origem e destino.
        encontrou_caminho, pai = encontrar_caminho_bfs(
            residual,
            origem,
            destino,
            quantidade_vertices
        )

        # Se não existir caminho aumentante, o algoritmo termina.
        if not encontrou_caminho:
            break

        # ====================================================
        # ETAPA 2 — ENCONTRAR O GARGALO DO CAMINHO
        # ====================================================

        # Inicialmente, o gargalo é infinito.
        fluxo_caminho = float("inf")

        # Começa pelo destino e retorna até a origem.
        atual = destino

        while atual != origem:

            # Recupera o vértice anterior.
            anterior = pai[atual]

            # Identifica a menor capacidade residual
            # encontrada no caminho.
            fluxo_caminho = min(
                fluxo_caminho,
                residual[anterior][atual]
            )

            atual = anterior

        # ====================================================
        # ETAPA 3 — ATUALIZAÇÃO DA REDE RESIDUAL
        # ====================================================

        # Percorre novamente o caminho.
        atual = destino

        caminho_indices = [destino]

        while atual != origem:

            anterior = pai[atual]

            # Diminui a capacidade residual da aresta utilizada.
            residual[anterior][atual] -= fluxo_caminho

            # Aumenta a capacidade residual da aresta reversa.
            #
            # Isso permite que o algoritmo reorganize fluxos
            # anteriores caso encontre uma solução melhor.
            residual[atual][anterior] += fluxo_caminho

            # Armazena o vértice anterior no caminho.
            caminho_indices.append(anterior)

            atual = anterior

        # Inverte para apresentar origem -> destino.
        caminho_indices.reverse()

        # Converte os índices em nomes dos vértices.
        caminho_nomes = [
            vertices[indice]
            for indice in caminho_indices
        ]

        # Registra o caminho e a quantidade de fluxo enviada.
        caminhos.append(
            (caminho_nomes, fluxo_caminho)
        )

        # Atualiza o fluxo máximo acumulado.
        fluxo_maximo += fluxo_caminho

    return fluxo_maximo, caminhos


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

# Define a origem e o destino pelos índices da matriz.
origem = vertices.index("Origem")
destino = vertices.index("Destino")

# Executa o algoritmo.
fluxo_maximo, caminhos = edmonds_karp(
    capacidades,
    origem,
    destino,
    vertices
)


print("\n========== ALGORITMO EDMONDS-KARP ==========")

print(f"Origem: {vertices[origem]}")
print(f"Destino: {vertices[destino]}")


# ============================================================
# EXIBIÇÃO DOS CAMINHOS AUMENTANTES
# ============================================================

print("\n========== CAMINHOS UTILIZADOS ==========")

for numero, (caminho, fluxo) in enumerate(
    caminhos,
    start=1
):

    print(f"\nCaminho {numero}:")

    print(" -> ".join(caminho))

    print(f"Fluxo enviado: {fluxo}")


# ============================================================
# RESULTADO FINAL
# ============================================================

print("\n========== RESULTADO FINAL ==========")

print(f"Fluxo máximo da rede: {fluxo_maximo}")

print(
    f"Quantidade de caminhos aumentantes: {len(caminhos)}"
)