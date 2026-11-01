# 2. Representação de Grafos

Um grafo pode ser armazenado de diferentes maneiras. A escolha da representação influencia o consumo de memória e o custo das operações, como verificar se dois vértices são adjacentes ou percorrer os vizinhos de um vértice.

Considere o grafo não direcionado:

\[
V = \{0,1,2,3\}, \quad E = \{\{0,1\},\{0,2\},\{1,3\},\{2,3\}\}
\]

## 2.1 Lista de arestas

A lista de arestas armazena cada ligação como um par de vértices.

```text
(0, 1)
(0, 2)
(1, 3)
(2, 3)
```

**Vantagens:** simples e compacta para grafos esparsos; fácil percorrer todas as arestas.

**Desvantagens:** verificar se uma aresta específica existe pode exigir percorrer a lista inteira.

Espaço: \(O(|E|)\).

## 2.2 Lista de adjacência

Para cada vértice, armazenamos seus vizinhos.

```text
0: 1, 2
1: 0, 3
2: 0, 3
3: 1, 2
```

Em um grafo não direcionado, cada aresta aparece nas listas dos dois extremos.

**Vantagens:** eficiente para percorrer vizinhos e econômica em grafos esparsos.

**Desvantagens:** verificar a existência de uma aresta pode exigir buscar na lista de vizinhos.

Espaço: \(O(|V|+|E|)\).

## 2.3 Matriz de adjacência

Uma matriz \(A\) de dimensão \(|V|\times|V|\) representa as conexões:

\[
A[i][j] =
\begin{cases}
1 & \text{se existe aresta entre } i \text{ e } j\\
0 & \text{caso contrário}
\end{cases}
\]

Para o exemplo:

```text
    0 1 2 3
0 [ 0 1 1 0 ]
1 [ 1 0 0 1 ]
2 [ 1 0 0 1 ]
3 [ 0 1 1 0 ]
```

Em grafos ponderados, a célula pode armazenar o peso da aresta; um valor especial indica ausência de conexão.

**Vantagens:** verificar uma aresta é \(O(1)\); adequada para grafos densos.

**Desvantagens:** ocupa \(O(|V|^2)\) de memória, mesmo quando há poucas arestas.

## 2.4 Comparação

| Operação | Lista de arestas | Lista de adjacência | Matriz |
|---|---:|---:|---:|
| Memória | \(O(E)\) | \(O(V+E)\) | \(O(V^2)\) |
| Verificar aresta | \(O(E)\) | \(O(\deg(v))\) | \(O(1)\) |
| Percorrer vizinhos | \(O(E)\) | \(O(\deg(v))\) | \(O(V)\) |

Os custos indicados são limites típicos; detalhes dependem da implementação e da estrutura usada para armazenar vizinhos.

## 2.5 Grafos direcionados e ponderados

Em um grafo direcionado, a lista de adjacência de \(u\) contém os vértices \(v\) para os quais existe arco \(u\to v\). A matriz não precisa ser simétrica.

Em grafos ponderados, cada vizinho pode ser armazenado junto ao peso, por exemplo:

```text
A: (B, 5), (C, 2)
B: (C, 4)
C: (A, 7)
```

## 2.6 Escolhendo a representação

- Use **lista de adjacência** como escolha geral, especialmente em grafos esparsos.
- Use **matriz de adjacência** quando o grafo for pequeno ou denso e consultas de adjacência forem frequentes.
- Use **lista de arestas** quando o processamento principal envolver ordenar ou percorrer todas as arestas, como em Kruskal.

## 2.7 Exercícios

1. Represente o grafo do exemplo por lista de arestas, lista de adjacência e matriz.
2. Modifique o grafo para incluir a aresta \(\{0,3\}\). Atualize as três representações.
3. Explique qual representação escolheria para uma rede com milhares de vértices e poucas arestas.
4. Em um grafo direcionado, explique por que a matriz de adjacência pode não ser simétrica.
