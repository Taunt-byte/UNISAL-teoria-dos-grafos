# 5. Grafos Eulerianos e Hamiltonianos

Grafos eulerianos e hamiltonianos tratam de percursos que visitam arestas ou vértices. Embora os nomes sejam parecidos, os requisitos são diferentes.

## 5.1 Trilhas, caminhos e ciclos

- **Trilha:** percurso que não repete arestas.
- **Caminho simples:** percurso que não repete vértices.
- **Circuito:** trilha fechada, que começa e termina no mesmo vértice.
- **Ciclo simples:** caminho fechado sem repetição de vértices, exceto o primeiro e o último.

A terminologia pode variar entre livros; neste material, usamos essas definições.

## 5.2 Grafos eulerianos

Um **circuito euleriano** percorre cada aresta exatamente uma vez e retorna ao vértice inicial.

Um grafo não direcionado conexo (desconsiderando vértices isolados) possui circuito euleriano se, e somente se, todos os vértices têm grau par.

Um **caminho euleriano aberto** percorre cada aresta exatamente uma vez, mas começa e termina em vértices diferentes. Em um grafo não direcionado conexo, existe se, e somente se, exatamente dois vértices têm grau ímpar.

### Como verificar

1. Verifique que todos os vértices incidentes a arestas pertencem ao mesmo componente conexo.
2. Conte o grau de cada vértice.
3. Se todos os graus forem pares, existe circuito euleriano.
4. Se exatamente dois graus forem ímpares, existe caminho euleriano aberto.
5. Se houver mais de dois vértices de grau ímpar, não existe percurso euleriano que use cada aresta exatamente uma vez.

## 5.3 Exemplo euleriano

Considere um ciclo com vértices A, B, C e D e arestas AB, BC, CD e DA. Todos os vértices têm grau 2, portanto o grafo possui circuito euleriano: A-B-C-D-A.

## 5.4 Grafos hamiltonianos

Um **ciclo hamiltoniano** visita cada vértice exatamente uma vez e retorna ao vértice inicial.

Um **caminho hamiltoniano** visita cada vértice exatamente uma vez, sem exigir retorno ao início.

Diferentemente do caso euleriano, não existe uma caracterização simples baseada apenas nos graus dos vértices que determine, em geral, se um grafo é hamiltoniano.

### Condições suficientes conhecidas

Para um grafo simples com \(n\geq 3\):

- **Teorema de Dirac:** se todo vértice tem grau pelo menos \(n/2\), então o grafo é hamiltoniano.
- **Teorema de Ore:** se para todo par de vértices não adjacentes \(u,v\), vale \(\deg(u)+\deg(v)\geq n\), então o grafo é hamiltoniano.

Essas condições são suficientes, não necessárias: um grafo pode ser hamiltoniano mesmo sem satisfazê-las.

## 5.5 Diferença essencial

| Euleriano | Hamiltoniano |
|---|---|
| Percorre cada aresta exatamente uma vez | Visita cada vértice exatamente uma vez |
| Pode repetir vértices | Não repete vértices, exceto o retorno no ciclo |
| Verificação em grafos não direcionados pode ser feita por conectividade e graus | Determinar existência é, em geral, computacionalmente difícil |

## 5.6 Aplicações

- **Euleriano:** inspeção de ruas, coleta de resíduos, roteamento que precisa percorrer ligações.
- **Hamiltoniano:** planejamento de visitas a cidades, sequenciamento de tarefas e problemas relacionados ao caixeiro-viajante.

O problema do caixeiro-viajante busca um ciclo de custo mínimo que visite cada cidade uma vez. Ele está relacionado a ciclos hamiltonianos, mas inclui uma função de custo e uma exigência de otimização.

## 5.7 Exercícios

1. Determine se um grafo possui circuito euleriano usando os graus.
2. Encontre um caminho euleriano quando existirem exatamente dois vértices de grau ímpar.
3. Para um grafo pequeno, procure um ciclo hamiltoniano por tentativa sistemática.
4. Explique por que um grafo pode ser euleriano sem ser hamiltoniano, e vice-versa.
5. Aplique as condições de Dirac e Ore a exemplos e identifique quando elas não permitem concluir nada.
