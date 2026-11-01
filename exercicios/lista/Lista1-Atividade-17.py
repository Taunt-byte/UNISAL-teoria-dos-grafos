# A partir do mapa abaixo, faça um programa que crie um grafo com vértices e suas
# respectivas arestas. Após criar este grafo ele deverá solicitar ao usuário a entrada de
# dois vértices conhecidos sendo retornado todos os caminhos possíveis entre estes
# vértices e a soma das distâncias de cada caminho

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
entrada1 = input("Digite o primeiro vértice: ")
entrada2 = input("Digite o segundo vértice: ")

resultados = []