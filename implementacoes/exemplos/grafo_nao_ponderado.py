"""
===========================================================
Projeto: Teoria dos Grafos
Assunto: Grafos Não Ponderados
Estrutura: Lista de Adjacência

Descrição:
    O programa representa um grafo por meio de um dicionário
    Python, utilizando a estrutura de lista de adjacência.

    Cada chave do dicionário representa um vértice.
    Cada lista associada a uma chave contém os vértices
    adjacentes, ou seja, aqueles que possuem uma conexão
    direta com o vértice correspondente.

Funcionalidades:
    1. Exibir a estrutura completa do grafo.
    2. Listar todos os vértices existentes.
    3. Consultar os vértices adjacentes a um vértice informado.
    4. Repetir a consulta enquanto o usuário desejar.

Tipo de grafo:
    Não ponderado e não direcionado.

Representação:
    Lista de adjacência utilizando dicionário e listas.

Autor: Lucas Neves
===========================================================
"""


# =========================================================
# FUNÇÃO: CONSULTAR DADOS DO GRAFO
# =========================================================

def dados_grafo(grafo):

    # Exibe a estrutura completa do grafo.
    # Cada chave representa um vértice e sua lista contém
    # os respectivos vértices adjacentes.
    print("\n========== ESTRUTURA DO GRAFO ==========")
    print(grafo)


    # Exibe todos os vértices presentes no grafo.
    # O método keys() retorna as chaves do dicionário,
    # que representam os vértices da estrutura.
    print("\n========== VÉRTICES ==========")
    print(*list(grafo.keys()))


    # Solicita ao usuário um vértice para consultar
    # suas conexões diretas com outros vértices.
    vertice = input("\nInforme o vértice para encontrar os adjacentes: ")


    # Verifica se o vértice informado existe no grafo.
    # Caso exista, acessa sua lista de adjacência.
    if vertice in grafo:

        # Exibe os vértices que possuem uma aresta
        # diretamente conectada ao vértice consultado.
        print(f"\nVértices adjacentes a {vertice}:")
        print(grafo[vertice])


    # Caso o vértice não esteja presente no dicionário,
    # informa ao usuário que ele não foi encontrado.
    else:

        print("\nVértice não encontrado!")


# =========================================================
# DEFINIÇÃO DO GRAFO
# =========================================================

# Representação do grafo por meio de um dicionário Python.
#
# Cada chave representa um vértice.
# Cada lista contém seus respectivos vértices adjacentes.
#
# Exemplo:
# O vértice '1' possui conexões diretas com os vértices
# '2' e '5'.
#
# Como o grafo é não direcionado, as conexões são
# representadas nos dois sentidos.

grafo = {

    '1': ['2', '5'],

    '2': ['1', '3', '5'],

    '3': ['2', '4'],

    '4': ['3', '5', '6'],

    '5': ['1', '2', '4'],

    '6': ['4']

}


# =========================================================
# CONTROLE DE REPETIÇÃO
# =========================================================

# Inicializa a variável responsável por controlar
# a repetição das consultas.
#
# Enquanto o usuário informar 's', o programa continuará
# executando a função dados_grafo().

repetir = 's'


while repetir.lower() == 's':

    # Executa a função responsável por apresentar
    # a estrutura do grafo e consultar suas adjacências.
    dados_grafo(grafo)

    # Pergunta ao usuário se deseja realizar uma nova consulta.
    repetir = input("\nDeseja repetir? <s/n>: ")


# =========================================================
# ENCERRAMENTO DO PROGRAMA
# =========================================================

# Exibe uma mensagem informando que a execução terminou.
print("\nPrograma encerrado!")