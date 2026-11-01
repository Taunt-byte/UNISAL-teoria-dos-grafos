# 4. Árvores

## 4.1 Definição

Uma **árvore** é um grafo não direcionado, conexo e acíclico. Um grafo acíclico que não precisa ser conexo é chamado de **floresta**.

Árvores são usadas para representar hierarquias, estruturas de arquivos, redes de distribuição e soluções de problemas de otimização.

## 4.2 Propriedades fundamentais

Para uma árvore com \(n\) vértices:

1. Existem exatamente \(n-1\) arestas.
2. Existe um único caminho simples entre cada par de vértices.
3. A remoção de qualquer aresta desconecta a árvore.
4. A adição de uma aresta entre dois vértices cria exatamente um ciclo.

Essas propriedades são equivalentes: um grafo não direcionado é uma árvore se, e somente se, satisfaz uma delas em conjunto com as condições apropriadas de finitude e conectividade.

## 4.3 Árvores enraizadas

Uma árvore enraizada possui um vértice especial chamado **raiz**. A partir dele, podemos definir:

- **Pai:** predecessor de um vértice no caminho até a raiz.
- **Filho:** vértice diretamente abaixo de outro.
- **Folha:** vértice sem filhos.
- **Profundidade:** número de arestas entre a raiz e o vértice.
- **Altura:** maior profundidade entre os vértices da árvore.

A raiz não possui pai. Em uma árvore enraizada, a relação pai-filho organiza os vértices em níveis.

## 4.4 Árvores geradoras

Uma **árvore geradora** de um grafo conexo é uma árvore que contém todos os vértices do grafo e utiliza apenas arestas do próprio grafo.

Um grafo pode possuir várias árvores geradoras. Se o grafo tem \(n\) vértices, toda árvore geradora possui \(n-1\) arestas.

## 4.5 Árvore geradora mínima (AGM)

Em um grafo conexo ponderado, uma árvore geradora mínima é uma árvore geradora cuja soma dos pesos das arestas é mínima.

### Algoritmo de Kruskal

1. Ordene as arestas por peso crescente.
2. Inicialize uma floresta com cada vértice isolado.
3. Considere as arestas em ordem.
4. Adicione uma aresta se ela conectar componentes diferentes (não formar ciclo).
5. Pare quando houver \(n-1\) arestas selecionadas.

Kruskal costuma ser implementado com uma estrutura **Union-Find**. Sua complexidade típica é \(O(E\log E)\), dominada pela ordenação.

### Algoritmo de Prim

1. Escolha um vértice inicial.
2. Mantenha um conjunto de vértices já incluídos.
3. Adicione a aresta de menor peso que conecta esse conjunto a um vértice ainda não incluído.
4. Repita até incluir todos os vértices.

Com fila de prioridade e lista de adjacência, uma implementação comum custa \(O(E\log V)\).

## 4.6 Exemplo

Considere arestas ponderadas:

```text
A-B: 1
A-C: 4
B-C: 2
B-D: 5
C-D: 3
```

Uma árvore geradora mínima seleciona A-B (1), B-C (2) e C-D (3), com peso total \(1+2+3=6\).

## 4.7 Exercícios

1. Verifique se um grafo é árvore usando conectividade e número de arestas.
2. Construa uma árvore geradora para um grafo conexo.
3. Execute Kruskal passo a passo em um grafo ponderado.
4. Execute Prim a partir de diferentes vértices e compare os resultados.
5. Explique por que uma árvore com \(n\) vértices possui \(n-1\) arestas.
