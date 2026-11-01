
"""
===========================================================
Projeto: Teoria dos Grafos
Assunto: Representação de Grafos por Lista de Adjacência

Descrição:
    O programa representa um conjunto de cidades e suas
    respectivas conexões utilizando um dicionário Python.

    Cada cidade representa um vértice do grafo.
    Cada conexão entre duas cidades representa uma aresta.

Funcionalidades:
    1. Exibir a estrutura completa do grafo.
    2. Listar todas as cidades.
    3. Consultar as cidades adjacentes a uma cidade informada.

Tipo de grafo:
    Não direcionado e não ponderado.

Autor: Lucas Neves
===========================================================
"""

# Definição do grafo utilizando uma lista de adjacência
grafo = {
    "Cruzeiro": ["Cachoeira", "Canas", "Lorena"],
    "Lorena": ["Canas", "Cachoeira", "Aparecida", "Piquete"],
    "Piquete": ["Lorena", "Delfim Moreira"],
    "Aparecida": ["Potim", "Lorena", "Roseira"],
    "Roseira": ["Lorena", "Taubate"],
    "Taubate": ["Roseira", "Cacapava"]
}


# Exibe a estrutura completa do grafo
print("========== GRAFO DAS CIDADES DA REGIÃO ==========")
print(grafo)


# Percorre o dicionário e apresenta todas as cidades (vértices)
print("\n========== CIDADES DA REGIÃO ==========")

for cidade in grafo:
    print(f"- {cidade}")


# Solicita ao usuário uma cidade para consultar suas adjacências
cidade = input("\nInforme a cidade para verificar as adjacências: ").strip()


# Verifica se a cidade informada existe no grafo
if cidade in grafo:

    # Recupera e apresenta as cidades diretamente conectadas
    adjacentes = grafo[cidade]

    print(f"\nCidades adjacentes a {cidade}:")

    for vizinha in adjacentes:
        print(f"- {vizinha}")

else:
    # Informa que a cidade não foi encontrada
    print("\nCidade não encontrada no grafo!")
