
"""
===========================================================
Projeto: Teoria dos Grafos
Assunto: Representação de Grafos
Estrutura: Lista de Adjacência

Descrição:
    O programa representa um grafo não direcionado utilizando
    um dicionário Python.

    Cada chave representa um vértice e cada lista contém
    os vértices adjacentes a ele.

Funcionalidades:
    1. Exibir a estrutura completa do grafo.
    2. Mostrar os vértices existentes.
    3. Consultar os vértices adjacentes a um vértice informado.

Autor: Lucas Neves
===========================================================
"""

# Definição do grafo por meio de uma lista de adjacência
grafo = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 4],
    4: [1, 3],
    5: [2]
}

# Exibe a estrutura completa do grafo
print("========== ESTRUTURA DO GRAFO ==========")
print(grafo)

# Exibe todos os vértices existentes
print("\n========== VÉRTICES DO GRAFO ==========")
print(list(grafo.keys()))

# Percorre e imprime individualmente cada vértice
for vertice in grafo:
    print(f"Vértice: {vertice}")

# Solicita ao usuário um vértice para consulta
vertice = int(input("\nInforme o vértice para encontrar os adjacentes: "))

# Verifica se o vértice existe no grafo
if vertice in grafo:

    # Exibe os vértices adjacentes ao vértice informado
    print(f"\nVértices adjacentes a {vertice}:")
    print(grafo[vertice])

else:
    # Informa que o vértice não foi encontrado
    print("\nVértice não encontrado!")
