
/*
 * ============================================================
 * PROJETO: Algoritmo de Kruskal
 * LINGUAGEM: C
 * AUTOR: Lucas Neves
 *
 * DESCRICAO:
 * Implementacao do algoritmo de Kruskal para encontrar
 * a Arvore Geradora Minima (AGM) de um grafo ponderado.
 *
 * FUNCIONALIDADES:
 * - Representacao do grafo por lista de arestas.
 * - Ordenacao das arestas pelo peso.
 * - Identificacao e prevencao de ciclos.
 * - Utilizacao da estrutura Union-Find (DSU).
 * - Calculo do custo total da arvore.
 *
 * TIPO DE GRAFO:
 * - Nao direcionado.
 * - Ponderado.
 *
 * COMPLEXIDADE:
 * O(E log E), considerando a ordenacao das arestas.
 * ============================================================
 */

#include <stdio.h>
#include <stdlib.h>

#define NUM_VERTICES 5
#define NUM_ARESTAS 7

/*
 * Estrutura que representa uma aresta.
 *
 * origem: vertice inicial.
 * destino: vertice final.
 * peso: custo da conexao entre os vertices.
 */
typedef struct {
    int origem;
    int destino;
    int peso;
} Aresta;

/*
 * Estrutura que representa os conjuntos disjuntos.
 *
 * pai[i]: representante do conjunto ao qual i pertence.
 * tamanho[i]: quantidade de elementos do conjunto.
 */
typedef struct {
    int pai[NUM_VERTICES];
    int tamanho[NUM_VERTICES];
} UnionFind;

/*
 * Lista de arestas do grafo.
 *
 * Cada elemento representa uma conexao entre dois vertices
 * e seu respectivo peso.
 */
Aresta arestas[NUM_ARESTAS] = {
    {0, 1, 2},
    {0, 3, 6},
    {1, 2, 3},
    {1, 3, 8},
    {1, 4, 5},
    {2, 4, 7},
    {3, 4, 9}
};

/*
 * Inicializa o Union-Find.
 *
 * Inicialmente, cada vertice pertence a um conjunto
 * independente.
 */
void inicializarUnionFind(UnionFind *uf) {

    for (int i = 0; i < NUM_VERTICES; i++) {
        uf->pai[i] = i;
        uf->tamanho[i] = 1;
    }
}

/*
 * Encontra o representante do conjunto de um vertice.
 *
 * A compressao de caminho faz com que os vertices
 * visitados apontem diretamente para o representante.
 */
int encontrar(UnionFind *uf, int vertice) {

    if (uf->pai[vertice] != vertice) {
        uf->pai[vertice] = encontrar(uf, uf->pai[vertice]);
    }

    return uf->pai[vertice];
}

/*
 * Une os conjuntos de dois vertices.
 *
 * A uniao por tamanho coloca o conjunto menor
 * dentro do conjunto maior.
 *
 * Retorna:
 * 1 se os conjuntos foram unidos.
 * 0 se ja pertenciam ao mesmo conjunto.
 */
int unir(UnionFind *uf, int a, int b) {

    int raizA = encontrar(uf, a);
    int raizB = encontrar(uf, b);

    // Os vertices ja pertencem ao mesmo conjunto.
    // Portanto, adicionar essa aresta criaria um ciclo.
    if (raizA == raizB) {
        return 0;
    }

    // Mantem a arvore mais alta como representante.
    if (uf->tamanho[raizA] < uf->tamanho[raizB]) {
        int temporario = raizA;
        raizA = raizB;
        raizB = temporario;
    }

    // Une os conjuntos.
    uf->pai[raizB] = raizA;
    uf->tamanho[raizA] += uf->tamanho[raizB];

    return 1;
}

/*
 * Funcao de comparacao utilizada pelo qsort().
 *
 * Ordena as arestas pelo peso em ordem crescente.
 */
int compararArestas(const void *a, const void *b) {

    const Aresta *arestaA = (const Aresta *)a;
    const Aresta *arestaB = (const Aresta *)b;

    if (arestaA->peso < arestaB->peso) {
        return -1;
    }

    if (arestaA->peso > arestaB->peso) {
        return 1;
    }

    return 0;
}

/*
 * Implementacao do algoritmo de Kruskal.
 */
void algoritmoKruskal() {

    UnionFind uf;

    // Inicializa os conjuntos disjuntos.
    inicializarUnionFind(&uf);

    // Ordena todas as arestas pelo peso.
    qsort(
        arestas,
        NUM_ARESTAS,
        sizeof(Aresta),
        compararArestas
    );

    int custoTotal = 0;
    int quantidadeSelecionada = 0;

    printf("\n========== ALGORITMO DE KRUSKAL ==========\n");
    printf("Arestas selecionadas:\n\n");

    /*
     * Percorre as arestas em ordem crescente.
     *
     * O algoritmo termina quando seleciona V - 1 arestas
     * ou quando todas as arestas forem analisadas.
     */
    for (int i = 0;
         i < NUM_ARESTAS && quantidadeSelecionada < NUM_VERTICES - 1;
         i++) {

        int origem = arestas[i].origem;
        int destino = arestas[i].destino;
        int peso = arestas[i].peso;

        /*
         * Se os vertices pertencem a conjuntos diferentes,
         * a aresta pode ser adicionada sem formar um ciclo.
         */
        if (unir(&uf, origem, destino)) {

            printf("%d -- %d | Peso: %d\n",
                   origem, destino, peso);

            custoTotal += peso;
            quantidadeSelecionada++;
        }
    }

    printf("\n------------------------------------------\n");

    // Verifica se todos os vertices foram conectados.
    if (quantidadeSelecionada == NUM_VERTICES - 1) {

        printf("Custo total da AGM: %d\n", custoTotal);

    } else {

        printf("O grafo nao e conexo.\n");
        printf("Foi encontrada uma floresta geradora minima.\n");
        printf("Custo total da floresta: %d\n", custoTotal);
    }
}

/*
 * Funcao principal.
 */
int main() {

    algoritmoKruskal();

    return 0;
}
