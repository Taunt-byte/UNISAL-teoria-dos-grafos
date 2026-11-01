# 1. Introdução à Teoria dos Grafos

## 1.1 O que é um grafo?

A **Teoria dos Grafos** é uma área da matemática discreta que estuda relações entre objetos. Um grafo é um modelo formado por um conjunto de **vértices** (ou nós) e um conjunto de **arestas** (ou ligações) que conectam pares de vértices.

Formalmente, um grafo simples não direcionado é definido como:

\[
G = (V, E)
\]

em que:

- \(V\) é o conjunto de vértices;
- \(E\) é o conjunto de arestas, cada uma ligando dois vértices distintos.

Por exemplo, uma rede de computadores pode ser representada por vértices que correspondem a dispositivos e arestas que representam conexões entre eles.

## 1.2 Exemplo

Considere:

\[
V = \{A, B, C, D\}
\]

\[
E = \{\{A,B\}, \{A,C\}, \{B,D\}, \{C,D\}\}
\]

Esse grafo possui quatro vértices e quatro arestas. A e B são adjacentes, assim como A e C. Não existe uma aresta direta entre A e D.

## 1.3 Conceitos fundamentais

- **Adjacência:** dois vértices são adjacentes quando existe uma aresta entre eles.
- **Incidência:** uma aresta é incidente aos vértices que conecta.
- **Grau de um vértice:** número de arestas incidentes ao vértice. Em grafos simples, o grau de \(v\) é denotado por \(\deg(v)\).
- **Laço:** aresta que conecta um vértice a si mesmo.
- **Arestas paralelas:** duas ou mais arestas que conectam o mesmo par de vértices.
- **Grafo simples:** grafo sem laços e sem arestas paralelas.
- **Grafo nulo:** grafo sem arestas.
- **Grafo completo:** grafo simples no qual todo par de vértices distintos é adjacente. É denotado por \(K_n\).

## 1.4 Tipos de grafos

### Grafo não direcionado

As arestas não possuem orientação. A ligação entre \(u\) e \(v\) é equivalente à ligação entre \(v\) e \(u\).

### Grafo direcionado

As arestas possuem orientação e são chamadas de **arcos**. Um arco \((u,v)\) representa uma ligação de \(u\) para \(v\), que não implica necessariamente uma ligação de \(v\) para \(u\).

### Grafo ponderado

Cada aresta possui um valor associado, chamado **peso**, que pode representar distância, custo, tempo ou capacidade.

### Grafo bipartido

Seus vértices podem ser divididos em dois conjuntos disjuntos \(U\) e \(W\), de modo que toda aresta conecte um vértice de \(U\) a um vértice de \(W\). Não há arestas entre vértices do mesmo conjunto.

## 1.5 Caminhos e ciclos

Um **caminho** é uma sequência de vértices em que cada par consecutivo está conectado por uma aresta. O comprimento de um caminho é o número de arestas percorridas.

Um **ciclo** é um caminho fechado que começa e termina no mesmo vértice, sem repetir outros vértices (na definição de ciclo simples).

## 1.6 Aplicações

A Teoria dos Grafos aparece em diversos problemas reais:

- Redes de computadores e roteamento.
- Mapas e planejamento de rotas.
- Redes sociais e análise de relacionamentos.
- Dependências entre tarefas e módulos de software.
- Circuitos elétricos e sistemas de transporte.
- Bioinformática e análise de redes de interação.

## 1.7 Resumo

Um grafo abstrai relações entre objetos. Seus conceitos básicos — vértices, arestas, graus, caminhos e ciclos — permitem modelar e resolver problemas de conectividade, otimização e organização de redes.
