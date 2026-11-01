# 3. Conectividade

Conectividade descreve a possibilidade de alcançar vértices de um grafo por meio de caminhos. É um conceito central em redes de comunicação, transporte e análise de dependências.

## 3.1 Grafos conexos

Um grafo não direcionado é **conexo** se existe um caminho entre todo par de vértices. Caso contrário, é **desconexo**.

Um **componente conexo** é um subgrafo conexo maximal: não é possível acrescentar outro vértice do grafo sem perder essa propriedade.

Um grafo desconexo pode conter vários componentes independentes.

## 3.2 Busca em largura (BFS)

A busca em largura explora o grafo por níveis, visitando primeiro os vértices mais próximos da origem em número de arestas. Utiliza uma fila (FIFO).

Pseudocódigo:

```text
BFS(G, origem):
    marcar origem como visitada
    inserir origem na fila

    enquanto a fila não estiver vazia:
        u = remover da fila
        para cada vizinho v de u:
            se v não foi visitado:
                marcar v como visitado
                predecessor[v] = u
                inserir v na fila
```

Com lista de adjacência, a complexidade é \(O(V+E)\). Em grafos não ponderados, BFS encontra caminhos com o menor número de arestas a partir da origem.

## 3.3 Busca em profundidade (DFS)

A busca em profundidade segue um caminho o máximo possível antes de retroceder. Pode ser implementada com recursão ou pilha.

```text
DFS(u):
    marcar u como visitado
    para cada vizinho v de u:
        se v não foi visitado:
            DFS(v)
```

Com lista de adjacência, a complexidade é \(O(V+E)\). DFS é útil para encontrar componentes conexos, detectar ciclos e apoiar algoritmos de ordenação topológica.

## 3.4 Componentes conexos

Para encontrar todos os componentes de um grafo não direcionado:

1. Inicialize todos os vértices como não visitados.
2. Percorra os vértices.
3. Ao encontrar um vértice não visitado, execute BFS ou DFS.
4. Todos os vértices alcançados formam um componente.
5. Repita até visitar todos os vértices.

O processo completo custa \(O(V+E)\) com lista de adjacência.

## 3.5 Conectividade em grafos direcionados

Em grafos direcionados, distinguem-se:

- **Fortemente conexo:** existe caminho dirigido de \(u\) para \(v\) e de \(v\) para \(u\), para todo par de vértices.
- **Fracamente conexo:** o grafo torna-se conexo quando ignoramos a orientação dos arcos.

## 3.6 Pontes e vértices de articulação

- **Ponte:** aresta cuja remoção aumenta o número de componentes conexos.
- **Vértice de articulação:** vértice cuja remoção (junto às arestas incidentes) aumenta o número de componentes conexos.

Esses elementos identificam pontos críticos de uma rede. Em uma rede de comunicação, uma ponte pode representar uma conexão cuja falha separa partes da rede.

## 3.7 Exercícios

1. Dado um grafo, determine seus componentes conexos.
2. Execute BFS a partir de um vértice e registre a ordem de visita.
3. Execute DFS no mesmo grafo e compare as ordens.
4. Encontre pontes e vértices de articulação em um grafo pequeno.
5. Explique a diferença entre conectividade forte e fraca.
