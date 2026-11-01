/*
 * ============================================================
 * DESAFIO 03 — FLUXO MAXIMO COM EDMONDS-KARP
 * ============================================================
 *
 * ENUNCIADO:
 *
 * Desenvolva um programa que calcule o fluxo máximo
 * de uma rede direcionada.
 *
 * Imagine uma rede de distribuição composta por centros
 * conectados por rotas com capacidades limitadas.
 *
 * O programa deverá:
 *
 * 1. Representar a rede por uma matriz de capacidades.
 * 2. Definir um vértice de origem e um vértice de destino.
 * 3. Encontrar caminhos aumentantes utilizando BFS.
 * 4. Identificar o gargalo de cada caminho.
 * 5. Atualizar as capacidades residuais.
 * 6. Calcular o fluxo máximo da rede.
 *
 * CONCEITOS:
 *
 * O fluxo máximo representa a maior quantidade de fluxo
 * que pode sair da origem e chegar ao destino.
 *
 * Edmonds-Karp utiliza BFS para encontrar caminhos
 * aumentantes na rede residual.
 *
 * A capacidade residual indica quanto fluxo adicional
 * ainda pode passar por determinada conexão.
 *
 * Complexidade: O(V * E²).
 *
 * ============================================================
 */

#include <stdio.h>

#define V 6

#define MIN(a, b) ((a) < (b) ? (a) : (b))


/*
 * Identificação dos vértices.
 */
const char *vertices[V] = {
    "Origem",
    "A",
    "B",
    "C",
    "D",
    "Destino"
};


/*
 * Matriz de capacidades.
 *
 * capacidade[i][j] representa a capacidade máxima
 * da conexão direcionada entre i e j.
 */
int capacidade[V][V] = {

    // O   A   B   C   D   T
    { 0, 16, 13,  0,  0,  0 },
    { 0,  0, 10, 12,  0,  0 },
    { 0,  4,  0,  0, 14,  0 },
    { 0,  0,  9,  0,  0, 20 },
    { 0,  0,  0,  7,  0,  4 },
    { 0,  0,  0,  0,  0,  0 }

};


/*
 * Procura um caminho aumentante utilizando BFS.
 *
 * A matriz residual contém as capacidades disponíveis
 * após os fluxos anteriores.
 *
 * O vetor pai armazena o antecessor de cada vértice.
 *
 * Retorna:
 * 1 -> caminho encontrado.
 * 0 -> caminho não encontrado.
 */
int buscarCaminho(
    int residual[V][V],
    int origem,
    int destino,
    int pai[V]
) {

    int fila[V];

    int inicio = 0;

    int fim = 0;

    int visitado[V] = {0};


    /*
     * Inicializa os antecessores.
     *
     * -1 indica que o vértice ainda não possui pai.
     */
    for (int i = 0; i < V; i++) {

        pai[i] = -1;

    }


    /*
     * Insere a origem na fila.
     */
    fila[fim++] = origem;

    visitado[origem] = 1;


    /*
     * Executa a BFS.
     */
    while (inicio < fim) {

        int atual = fila[inicio++];

        /*
         * Analisa todos os possíveis vizinhos.
         */
        for (int vizinho = 0; vizinho < V; vizinho++) {

            /*
             * Só podemos utilizar arestas com capacidade
             * residual positiva.
             *
             * Também evitamos visitar novamente um vértice.
             */
            if (
                residual[atual][vizinho] > 0 &&
                !visitado[vizinho]
            ) {

                visitado[vizinho] = 1;

                pai[vizinho] = atual;

                /*
                 * Se encontramos o destino,
                 * podemos encerrar a busca.
                 */
                if (vizinho == destino) {

                    return 1;

                }

                fila[fim++] = vizinho;

            }

        }

    }

    return 0;

}


/*
 * Calcula o fluxo máximo utilizando Edmonds-Karp.
 */
int edmondsKarp(int origem, int destino) {

    int residual[V][V];

    int pai[V];

    int fluxoMaximo = 0;


    /*
     * Copia a matriz original para a matriz residual.
     *
     * Dessa maneira, preservamos as capacidades originais.
     */
    for (int i = 0; i < V; i++) {

        for (int j = 0; j < V; j++) {

            residual[i][j] = capacidade[i][j];

        }

    }


    /*
     * ETAPA 1 — ENCONTRAR CAMINHOS AUMENTANTES
     *
     * O algoritmo continua enquanto existir um caminho
     * com capacidade residual positiva.
     */
    while (
        buscarCaminho(
            residual,
            origem,
            destino,
            pai
        )
    ) {

        /*
         * Inicialmente, o gargalo é considerado infinito.
         *
         * INT_MAX representa o maior inteiro positivo.
         */
        int gargalo = 2147483647;

        int atual = destino;


        /*
         * ETAPA 2 — ENCONTRAR O GARGALO
         *
         * Percorre o caminho do destino até a origem.
         *
         * O gargalo é a menor capacidade residual
         * encontrada entre as arestas do caminho.
         */
        while (atual != origem) {

            int anterior = pai[atual];

            gargalo = MIN(
                gargalo,
                residual[anterior][atual]
            );

            atual = anterior;

        }


        /*
         * ETAPA 3 — ATUALIZAR AS CAPACIDADES RESIDUAIS
         */
        atual = destino;

        printf("\nCaminho aumentante encontrado: ");

        /*
         * Exibe o caminho na ordem origem -> destino.
         *
         * Para isso, reconstruímos o caminho em um vetor.
         */
        int caminho[V];

        int tamanho = 0;

        int temporario = destino;

        while (temporario != origem) {

            caminho[tamanho++] = temporario;

            temporario = pai[temporario];

        }

        caminho[tamanho++] = origem;

        for (int i = tamanho - 1; i >= 0; i--) {

            printf("%s", vertices[caminho[i]]);

            if (i > 0) {
                printf(" -> ");
            }

        }

        printf("\nGargalo do caminho: %d\n", gargalo);


        /*
         * Atualiza as capacidades residuais.
         *
         * A aresta utilizada perde capacidade.
         *
         * A aresta reversa ganha capacidade residual,
         * permitindo que o algoritmo desfaça parte
         * de fluxos anteriores quando necessário.
         */
        while (atual != origem) {

            int anterior = pai[atual];

            residual[anterior][atual] -= gargalo;

            residual[atual][anterior] += gargalo;

            atual = anterior;

        }


        /*
         * Acumula o fluxo enviado pelo caminho.
         */
        fluxoMaximo += gargalo;

    }


    return fluxoMaximo;

}


/*
 * Função principal.
 */
int main() {

    int origem = 0;

    int destino = 5;


    printf("========== REDE DE DISTRIBUICAO ==========\n");

    printf("Origem: %s\n", vertices[origem]);

    printf("Destino: %s\n", vertices[destino]);


    /*
     * Executa o algoritmo.
     */
    int resultado = edmondsKarp(origem, destino);


    /*
     * Exibe o resultado final.
     */
    printf("\n========== RESULTADO FINAL ==========\n");

    printf("Fluxo maximo da rede: %d\n", resultado);

    return 0;

}