
"""
===========================================================
Projeto: Teoria dos Grafos
Assunto: Representação de Grafos
Estrutura: Lista de Adjacência

Descrição:
    O programa representa um grafo não direcionado e não
    ponderado utilizando um dicionário Python.

    Cada chave do dicionário representa um vértice.
    Cada lista associada à chave armazena os vértices
    adjacentes, ou seja, aqueles que possuem uma conexão
    direta com o vértice correspondente.

Funcionalidades:
    1. Criar e inicializar a estrutura do grafo.
    2. Exibir a estrutura completa do grafo.
    3. Listar todos os vértices existentes.
    4. Consultar os vértices adjacentes a um vértice informado.
    5. Verificar se determinado vértice existe no grafo.

Tipo de grafo:
    Não direcionado e não ponderado.

Representação:
    Lista de adjacência utilizando dicionário e listas.

Autor: Lucas Neves
===========================================================
"""


# =========================================================
# FUNÇÃO: DEFINIR O GRAFO
# =========================================================

def definir_grafo():

    """
    Cria e retorna um grafo representado por lista de adjacência.

    Cada chave representa um vértice.
    Cada lista contém seus respectivos vértices adjacentes.

    Retorno:
        Um dicionário contendo todos os vértices e conexões.
    """

    # Define os vértices e suas respectivas conexões.
    #
    # Exemplo:
    # O vértice '1' possui conexões diretas com os vértices
    # '2' e '5'.
    #
    # Como o grafo é não direcionado, cada conexão aparece
    # nos dois sentidos.

    grafo = {

        '1': ['2', '5'],

        '2': ['1', '3', '5'],

        '3': ['2', '4'],

        '4': ['3', '5', '6'],

        '5': ['1', '2', '4'],

        '6': ['4']

    }

    # Retorna o dicionário contendo a estrutura do grafo.
    return grafo


# =========================================================
# FUNÇÃO: MOSTRAR E CONSULTAR O GRAFO
# =========================================================

def mostrar_grafo():

    # Chama a função definir_grafo() para criar e obter
    # a estrutura completa do grafo.
    grafo = definir_grafo()


    # -----------------------------------------------------
    # EXIBIÇÃO DA ESTRUTURA COMPLETA
    # -----------------------------------------------------

    # Apresenta o dicionário com todos os vértices
    # e suas respectivas listas de adjacência.
    print("\n========== ESTRUTURA DO GRAFO ==========")
    print(grafo)


    # -----------------------------------------------------
    # EXIBIÇÃO DOS VÉRTICES
    # -----------------------------------------------------

    # O método keys() retorna todas as chaves do dicionário.
    # Como cada chave representa um vértice, podemos
    # utilizá-lo para listar os vértices existentes.
    print("\n========== VÉRTICES DO GRAFO ==========")

    print(*list(grafo.keys()))


    # -----------------------------------------------------
    # CONSULTA DE VÉRTICES ADJACENTES
    # -----------------------------------------------------

    # Solicita ao usuário um vértice para consultar
    # suas conexões diretas.
    vertice = input(
        "\nInforme o vértice para encontrar os adjacentes: "
    ).strip()


    # Verifica se o vértice informado existe no dicionário.
    if vertice in grafo:

        # Acessa a lista associada ao vértice informado
        # e apresenta todos os seus vértices adjacentes.
        print(f"\nVértices adjacentes a {vertice}:")
        print(grafo[vertice])


    else:

        # Informa que o vértice não está cadastrado
        # na estrutura do grafo.
        print("\nVértice não encontrado.")


# =========================================================
# EXECUÇÃO DO PROGRAMA
# =========================================================

# Chama a função principal responsável por apresentar
# a estrutura do grafo e realizar a consulta.
mostrar_grafo()
