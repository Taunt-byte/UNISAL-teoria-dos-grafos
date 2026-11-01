# ============================================================
# DESAFIO 02 — ORDENAÇÃO TOPOLÓGICA COM ALGORITMO DE KAHN
# ============================================================
#
# ENUNCIADO:
# Desenvolva um sistema que organize tarefas de um projeto
# considerando as dependências existentes entre elas.
#
# Imagine que uma equipe precisa executar várias atividades,
# mas algumas só podem começar depois que outras terminarem.
#
# O programa deverá:
# 1. Representar as tarefas como vértices de um grafo.
# 2. Representar as dependências como arestas direcionadas.
# 3. Identificar uma ordem válida de execução.
# 4. Exibir as tarefas respeitando suas dependências.
# 5. Identificar se existe uma dependência circular.
#
# CONCEITOS:
# A ordenação topológica organiza os vértices de um
# grafo direcionado acíclico (DAG).
#
# Uma aresta A -> B significa que A precisa ser concluída
# antes que B possa ser executada.
#
# O algoritmo de Kahn utiliza o grau de entrada dos vértices.
#
# Grau de entrada:
# Quantidade de arestas que chegam até determinado vértice.
#
# Complexidade: O(V + E).
#
# ============================================================


from collections import deque


# ============================================================
# REPRESENTAÇÃO DO GRAFO
# ============================================================

# Cada chave representa uma tarefa.
#
# Os valores representam as tarefas que dependem dela.
#
# Exemplo:
# "Planejamento": ["Modelagem"]
#
# Significa que a Modelagem depende do Planejamento.
grafo = {
    "Planejamento": [
        "Modelagem",
        "Documentacao"
    ],

    "Modelagem": [
        "Desenvolvimento"
    ],

    "Documentacao": [
        "Desenvolvimento"
    ],

    "Desenvolvimento": [
        "Testes"
    ],

    "Testes": [
        "Implantacao"
    ],

    "Implantacao": []
}


def calcular_grau_entrada(grafo):
    """
    Calcula o grau de entrada de cada vértice.

    Inicialmente, todos os vértices possuem grau de entrada 0.

    Depois, percorremos as arestas e incrementamos
    o grau de entrada de cada destino.
    """

    # Inicializa o grau de entrada de todos os vértices.
    grau_entrada = {
        vertice: 0
        for vertice in grafo
    }

    # Percorre as conexões existentes.
    for origem in grafo:

        for destino in grafo[origem]:

            # Cada aresta aumenta o grau de entrada do destino.
            grau_entrada[destino] += 1

    return grau_entrada


def ordenacao_topologica(grafo):
    """
    Executa o algoritmo de Kahn.

    Retorna:
    ordem  -> sequência válida de execução das tarefas.
    sucesso -> indica se a ordenação foi concluída.
    """

    # Calcula os graus de entrada.
    grau_entrada = calcular_grau_entrada(grafo)

    # Fila contendo os vértices sem dependências pendentes.
    fila = deque()

    # Procura os vértices com grau de entrada igual a zero.
    for vertice, grau in grau_entrada.items():

        if grau == 0:
            fila.append(vertice)

    # Armazena a ordem topológica encontrada.
    ordem = []

    # Processa os vértices disponíveis.
    while fila:

        # Retira uma tarefa que não possui dependências pendentes.
        atual = fila.popleft()

        # Adiciona a tarefa à sequência de execução.
        ordem.append(atual)

        # Analisa todas as tarefas dependentes da atual.
        for vizinho in grafo[atual]:

            # A conclusão da tarefa atual elimina
            # uma dependência do vizinho.
            grau_entrada[vizinho] -= 1

            # Se todas as dependências foram resolvidas,
            # o vizinho pode entrar na fila.
            if grau_entrada[vizinho] == 0:

                fila.append(vizinho)

    # ========================================================
    # DETECÇÃO DE CICLO
    # ========================================================

    # Se nem todos os vértices foram processados,
    # existe pelo menos um ciclo no grafo.
    if len(ordem) != len(grafo):

        return ordem, False

    return ordem, True


def exibir_dependencias(grafo):
    """
    Exibe todas as dependências cadastradas.
    """

    print("\n========== DEPENDÊNCIAS DO PROJETO ==========")

    for tarefa, dependencias in grafo.items():

        if dependencias:

            for dependencia in dependencias:

                print(f"{tarefa} -> {dependencia}")

        else:

            print(f"{tarefa} -> Nenhuma dependência posterior")


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================

exibir_dependencias(grafo)

ordem, sucesso = ordenacao_topologica(grafo)

print("\n========== ORDEM DE EXECUÇÃO ==========")

if sucesso:

    print("Foi encontrada uma ordem topológica válida.\n")

    # Exibe a sequência de tarefas.
    for numero, tarefa in enumerate(ordem, start=1):

        print(f"{numero}. {tarefa}")

else:

    print("Não foi possível organizar todas as tarefas.")

    print("O grafo possui uma dependência circular.")

    print("\nTarefas processadas antes da identificação do ciclo:")

    for tarefa in ordem:

        print(f"- {tarefa}")