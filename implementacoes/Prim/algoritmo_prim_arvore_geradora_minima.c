
/*
 * ============================================================
 * PROJETO: Algoritmo de Prim
 * LINGUAGEM: C
 * AUTOR: Lucas Neves
 *
 * DESCRIÇÃO:
 * Implementação do algoritmo de Prim utilizando uma matriz
 * de adjacência para encontrar a Árvore Geradora Mínima (AGM).
 *
 * FUNCIONALIDADES:
 * - Representação de grafo por matriz de adjacência.
 * - Busca da aresta de menor peso.
 * - Construção da Árvore Geradora Mínima.
 * - Exibição das arestas selecionadas e do custo total.
 *
 * TIPO DE GRAFO:
 * - Não direcionado.
 * - Ponderado.
 * - Conexo.
 *
 * COMPLEXIDADE:
 * O(V²), utilizando matriz de adjacência.
 * ============================================================
 */

#include <stdio.h>
#include <limits.h>

#define NUM_VERTICES 5

/*
 * Representação do grafo por matriz de adjacência.
 *
 * Cada posição matriz[i][j] representa o peso da aresta
 * entre os vértices i e j.
 *
 * O valor 0 indica que não existe uma aresta entre eles.
 */
int grafo[NUM_VERTICES][NUM_VERTICES] = {
    {0, 2, 0, 6, 0},
    {2, 0, 3, 8, 5},
    {0, 3, 0, 0, 7},
    {6, 8, 0, 0, 9},
    {0, 5, 7, 9, 0}
};

/*
 * Encontra o vértice ainda não incluído na árvore
 * que possui a menor chave (menor custo de conexão).
 */
int encontrarMenorChave(int chave[], int incluido[]) {

    int menor = INT_MAX;
    int indiceMenor = -1;

    for (int i = 0; i < NUM_VERTICES; i++) {

        if (!incluido[i] && chave[i] < menor) {
            menor = chave[i];
            indiceMenor = i;
        }
    }

    return indiceMenor;
}

/*
 * Implementação do algoritmo de Prim.
 */
void algoritmoPrim() {

    /*
     * pai[i] armazena o vértice predecessor de i na AGM.
     *
     * chave[i] armazena o menor peso conhecido para
     * conectar o vértice i à árvore.
     *
     * incluido[i] indica se o vértice já foi selecionado.
     */
    int pai[NUM_VERTICES];
    int chave[NUM_VERTICES];
    int incluido[NUM_VERTICES];

    // Inicializa os vetores.
    for (int i = 0; i < NUM_VERTICES; i++) {
        chave[i] = INT_MAX;
        incluido[i] = 0;
        pai[i] = -1;
    }

    // Começa pelo vértice 0.
    chave[0] = 0;

    /*
     * A cada iteração, selecionamos um vértice
     * que ainda não pertence à árvore.
     */
    for (int contador = 0; contador < NUM_VERTICES - 1; contador++) {

        int u = encontrarMenorChave(chave, incluido);

        // Verifica se o grafo possui vértices alcançáveis.
        if (u == -1) {
            break;
        }

        // Inclui o vértice selecionado na árvore.
        incluido[u] = 1;

        /*
         * Atualiza os custos dos vértices adjacentes.
         *
         * Se encontramos uma aresta mais barata para
         * alcançar um vértice, atualizamos sua chave e pai.
         */
        for (int v = 0; v < NUM_VERTICES; v++) {

            if (grafo[u][v] != 0 &&
                !incluido[v] &&
                grafo[u][v] < chave[v]) {

                pai[v] = u;
                chave[v] = grafo[u][v];
            }
        }
    }

    // Exibe as arestas que formam a Árvore Geradora Mínima.
    int custoTotal = 0;

    printf("\n========== ARVORE GERADORA MINIMA ==========\n");
    printf("Aresta\tPeso\n");

    for (int i = 1; i < NUM_VERTICES; i++) {

        if (pai[i] == -1) {
            printf("Vertice %d nao conectado ao grafo principal.\n", i);
            continue;
        }

        printf("%d - %d\t%d\n",
               pai[i], i, grafo[i][pai[i]]);

        custoTotal += grafo[i][pai[i]];
    }

    printf("--------------------------------------------\n");
    printf("Custo total: %d\n", custoTotal);
}

/*
 * Função principal.
 */
int main() {

    algoritmoPrim();

    return 0;
}
