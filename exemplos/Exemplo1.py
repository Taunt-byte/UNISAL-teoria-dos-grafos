def dadosGrafo():
  print("Estrutura geral do grafo:")
  print(grafo)

  print("Grafo formado pelos seguintes vertices:")
  print(grafo.keys())

  vert = input("Informe o vertice para encontrar os adjacentes..:")
  print(grafo.get(vert))


grafo = {
  '1': ['2', '5'],
  '2': ['1', '3', '5'],
  '3': ['2', '4'],
  '4': ['3', '5', '6'],
  '5': ['1', '2', '4'],
  '6': ['4']
}

rep='s'

while rep == 's':
  dadosGrafo()
  rep = input("Deseja repetir? <s/n> :")


