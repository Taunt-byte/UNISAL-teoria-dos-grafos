/*
 * ============================================================
 * DESAFIO 01 — ALGORITMO DE BELLMAN-FORD
 * ============================================================
 *
 * ENUNCIADO:
 *
 * Implemente o algoritmo de Bellman-Ford para encontrar
 * os menores caminhos entre um vértice de origem e os
 * demais vértices de um grafo direcionado e ponderado.
 *
 * O programa deverá:
 *
 * 1. Representar um grafo por meio de uma lista de arestas.
 * 2. Permitir a utilização de pesos negativos.
 * 3. Calcular as menores distâncias a partir de uma origem.
 * 4. Armazenar os antecessores de cada vértice.
 * 5. Reconstruir os caminhos encontrados.
 * 6. Identificar ciclos negativos alcançáveis pela origem.
 *
 * CONCEITO:
 *
 * Bellman-Ford realiza o relaxamento das arestas V - 1 vezes.
 * Depois, executa uma verificação adicional para identificar
 * a existência de ciclos negativos alcançáveis.
 *
 * Complexidade: O(V * E).
 *
 * ============================================================
 */

#include <stdio.h>
#include <limits.h>

#define V 5
#define E 10

#define INFINITO (LLONG_MAX / 4)

/*
 * Estrutura que representa uma aresta.
 *
 * origem  -> vértice de partida.
 * destino -> vértice de chegada.
 * peso    -> custo da conexão.
 */
typedef struct {
    int origem;
    int destino;
    int peso;
} Aresta;


/*
 * Representação das arestas do grafo.
 *
 * Os vértices são identificados por números:
 *
 * 0 = A
 * 1 = B
 * 2 = C
 * 3 = D
 * 4 = E
 */
Aresta arestas[E] = {
    {0, 1,  6},
    {0, 2,  7},
    {1, 2,  8},
    {1, 3,  5},
    {1, 4, -4},
    {2, 3, -3},
    {2, 4,  9},
    {3, 1, -2},
    {4, 0,  2},
    {4, 3,  7}
};


/*
 * Exibe o nome de um vértice.
 */
void exibirVertice(int vertice) {

    printf("%c", 'A' + vertice);

}


/*
 * Reconstrói o caminho entre a origem e um destino.
 *
 * A reconstrução começa pelo destino e utiliza
 * o vetor anterior para retornar até a origem.
 *
 * O caminho é armazenado temporariamente em um vetor
 * e depois exibido na ordem correta.
 */
void exibirCaminho(int anterior[], int origem, int destino) {

    int caminho[V];

    int tamanho = 0;

    int atual = destino;

    /*
     * Percorre os antecessores até encontrar a origem.
     */
    while (atual != -1 && tamanho < V) {

        caminho[tamanho] = atual;

        tamanho++;

        if (atual == origem) {
            break;
        }

        atual = anterior[atual];
    }

    /*
     * Verifica se foi possível reconstruir o caminho.
     */
    if (tamanho == 0 || caminho[tamanho - 1] != origem) {

        printf("Caminho inexistente.");

        return;
    }

    /*
     * Exibe o vetor na ordem inversa.
     */
    for (int i = tamanho - 1; i >= 0; i--) {

        exibirVertice(caminho[i]);

        if (i > 0) {
            printf(" -> ");
        }
    }

}


/*
 * Implementação do algoritmo de Bellman-Ford.
 */
void bellmanFord(int origem) {

    long long distancia[V];

    int anterior[V];

    /*
     * Inicialização das distâncias.
     *
     * Inicialmente, todos os vértices são considerados
     * inalcançáveis.
     */
    for (int i = 0; i < V; i++) {

        distancia[i] = INFINITO;

        anterior[i] = -1;

    }

    /*
     * A distância da origem até ela mesma é zero.
     */
    distancia[origem] = 0;


    /*
     * ETAPA 1 — RELAXAMENTO DAS ARESTAS
     *
     * Para um grafo com V vértices, são necessárias
     * no máximo V - 1 iterações.
     */
    for (int i = 0; i < V - 1; i++) {

        int houveAtualizacao = 0;

        /*
         * Percorre todas as arestas.
         */
        for (int j = 0; j < E; j++) {

            int u = arestas[j].origem;

            int v = arestas[j].destino;

            int peso = arestas[j].peso;

            /*
             * Não podemos calcular uma distância a partir
             * de um vértice que ainda não foi alcançado.
             */
            if (distancia[u] == INFINITO) {
                continue;
            }

            /*
             * Calcula o custo de chegar ao destino
             * passando pela aresta atual.
             */
            long long novaDistancia = distancia[u] + peso;

            /*
             * Verifica se encontramos um caminho menor.
             */
            if (novaDistancia < distancia[v]) {

                distancia[v] = novaDistancia;

                anterior[v] = u;

                houveAtualizacao = 1;
            }

        }

        /*
         * Otimização:
         *
         * Se nenhuma distância foi modificada,
         * não precisamos continuar as iterações.
         */
        if (!houveAtualizacao) {
            break;
        }

    }


    /*
     * ETAPA 2 — DETECÇÃO DE CICLO NEGATIVO
     *
     * Se ainda for possível diminuir uma distância,
     * existe um ciclo negativo alcançável pela origem.
     */
    for (int i = 0; i < E; i++) {

        int u = arestas[i].origem;

        int v = arestas[i].destino;

        int peso = arestas[i].peso;

        if (distancia[u] == INFINITO) {
            continue;
        }

        if (distancia[u] + peso < distancia[v]) {

            printf("\nCiclo negativo encontrado!\n");

            printf("Nao e possivel determinar menores ");
            printf("caminhos finitos.\n");

            return;
        }

    }


    /*
     * ETAPA 3 — EXIBIÇÃO DOS RESULTADOS
     */
    printf("\n========== BELLMAN-FORD ==========\n");

    printf("Origem: ");

    exibirVertice(origem);

    printf("\n");

    for (int i = 0; i < V; i++) {

        printf("\nDestino: ");

        exibirVertice(i);

        if (distancia[i] == INFINITO) {

            printf("\nDistancia: INALCANCAVEL\n");

        } else {

            printf("\nDistancia minima: %lld\n", distancia[i]);

            printf("Caminho: ");

            exibirCaminho(anterior, origem, i);

            printf("\n");
        }

    }

}


/*
 * Função principal.
 */
int main() {

    int origem = 0;

    printf("========== GRAFO DIRECIONADO ==========\n");

    printf("Vertices: A, B, C, D, E\n");

    printf("Origem selecionada: A\n");

    bellmanFord(origem);

    return 0;
}