/*
 * ============================================================
 * DESAFIO 04 — PONTOS DE ARTICULACAO COM TARJAN
 * ============================================================
 *
 * ENUNCIADO:
 *
 * Desenvolva um programa capaz de identificar os pontos
 * de articulação de um grafo não direcionado.
 *
 * Imagine uma rede de computadores na qual determinados
 * equipamentos conectam diferentes partes da infraestrutura.
 *
 * Se um desses equipamentos falhar, algumas partes da rede
 * poderão ficar desconectadas.
 *
 * O programa deverá:
 *
 * 1. Representar um grafo não direcionado.
 * 2. Percorrer os vértices utilizando DFS.
 * 3. Calcular os tempos de descoberta dos vértices.
 * 4. Calcular os valores low de cada vértice.
 * 5. Identificar os pontos de articulação.
 * 6. Exibir os vértices cuja remoção desconecta o grafo.
 *
 * CONCEITOS:
 *
 * Um ponto de articulação é um vértice cuja remoção,
 * juntamente com suas arestas incidentes, aumenta
 * o número de componentes conexas do grafo.
 *
 * O algoritmo de Tarjan utiliza:
 *
 * descoberta[u]:
 * Momento em que o vértice u foi descoberto pela DFS.
 *
 * low[u]:
 * Menor tempo de descoberta alcançável a partir de u
 * utilizando arestas da árvore DFS e, no máximo,
 * uma aresta de retorno.
 *
 * Regras:
 *
 * 1. Uma raiz da DFS é ponto de articulação quando possui
 *    pelo menos dois filhos na árvore DFS.
 *
 * 2. Um vértice que não é raiz é ponto de articulação
 *    quando algum filho v satisfaz:
 *
 *                  low[v] >= descoberta[u]
 *
 * Complexidade: O(V + E).
 *
 * ============================================================
 */

#include <stdio.h>

#define V 7


/*
 * Representação do grafo por matriz de adjacência.
 *
 * Os vértices representam equipamentos de uma rede.
 *
 * 0 = A
 * 1 = B
 * 2 = C
 * 3 = D
 * 4 = E
 * 5 = F
 * 6 = G
 *
 * O grafo é não direcionado.
 * Portanto, a matriz é simétrica.
 */
int grafo[V][V] = {

    // A  B  C  D  E  F  G
    { 0, 1, 1, 0, 0, 0, 0 }, // A
    { 1, 0, 0, 1, 0, 0, 0 }, // B
    { 1, 0, 0, 1, 0, 0, 0 }, // C
    { 0, 1, 1, 0, 1, 0, 0 }, // D
    { 0, 0, 0, 1, 0, 1, 1 }, // E
    { 0, 0, 0, 0, 1, 0, 0 }, // F
    { 0, 0, 0, 0, 1, 0, 0 }  // G

};


/*
 * Vetores auxiliares utilizados pela DFS.
 */
int descoberta[V];

int low[V];

int pai[V];

int articulacao[V];


/*
 * Contador global do tempo de descoberta.
 */
int tempo = 0;


/*
 * Exibe o nome de um vértice.
 */
void exibirVertice(int vertice) {

    printf("%c", 'A' + vertice);

}


/*
 * DFS modificada para identificar pontos de articulação.
 *
 * Parâmetros:
 *
 * u -> vértice atualmente visitado.
 */
void encontrarArticulacoes(int u) {

    /*
     * Número de filhos do vértice atual na árvore DFS.
     *
     * Essa informação é especialmente importante
     * para identificar pontos de articulação raiz.
     */
    int filhos = 0;


    /*
     * Marca o momento em que o vértice foi descoberto.
     */
    descoberta[u] = ++tempo;

    /*
     * Inicialmente, low recebe o próprio tempo
     * de descoberta.
     */
    low[u] = descoberta[u];


    /*
     * Percorre todos os possíveis vizinhos.
     */
    for (int v = 0; v < V; v++) {

        /*
         * Verifica se existe uma aresta entre u e v.
         */
        if (grafo[u][v] == 1) {


            /*
             * CASO 1 — VÉRTICE AINDA NÃO VISITADO
             *
             * Encontramos um novo filho na árvore DFS.
             */
            if (descoberta[v] == 0) {

                filhos++;

                /*
                 * Registra o pai do vértice v.
                 */
                pai[v] = u;

                /*
                 * Continua a busca recursivamente.
                 */
                encontrarArticulacoes(v);


                /*
                 * Atualiza low[u] considerando
                 * os caminhos encontrados em v.
                 */
                if (low[v] < low[u]) {

                    low[u] = low[v];

                }


                /*
                 * REGRA 1 — VÉRTICE QUE NÃO É RAIZ
                 *
                 * Se low[v] >= descoberta[u],
                 * significa que a subárvore de v não
                 * consegue alcançar um ancestral de u
                 * por uma aresta de retorno.
                 *
                 * Portanto, remover u desconecta essa
                 * subárvore do restante do grafo.
                 */
                if (
                    pai[u] != -1 &&
                    low[v] >= descoberta[u]
                ) {

                    articulacao[u] = 1;

                }

            }


            /*
             * CASO 2 — VÉRTICE JÁ VISITADO
             *
             * Se v não é o pai de u, encontramos
             * uma possível aresta de retorno.
             *
             * Atualizamos low[u] com o tempo de
             * descoberta de v.
             */
            else if (v != pai[u]) {

                if (descoberta[v] < low[u]) {

                    low[u] = descoberta[v];

                }

            }

        }

    }


    /*
     * REGRA 2 — VÉRTICE RAIZ
     *
     * Uma raiz da DFS é ponto de articulação
     * quando possui pelo menos dois filhos.
     *
     * Isso significa que existem pelo menos duas
     * subárvores independentes conectadas por ela.
     */
    if (pai[u] == -1 && filhos > 1) {

        articulacao[u] = 1;

    }

}


/*
 * Inicializa os vetores e executa a DFS.
 *
 * O algoritmo também verifica grafos desconexos,
 * iniciando uma DFS para cada componente ainda não visitada.
 */
void executarTarjan() {

    /*
     * Inicialização dos vetores.
     */
    for (int i = 0; i < V; i++) {

        descoberta[i] = 0;

        low[i] = 0;

        pai[i] = -1;

        articulacao[i] = 0;

    }

    tempo = 0;


    /*
     * Percorre todos os vértices.
     *
     * Caso algum vértice ainda não tenha sido descoberto,
     * ele será a raiz de uma nova DFS.
     */
    for (int i = 0; i < V; i++) {

        if (descoberta[i] == 0) {

            encontrarArticulacoes(i);

        }

    }

}


/*
 * Exibe os pontos de articulação encontrados.
 */
void exibirArticulacoes() {

    int encontrou = 0;

    printf("\n========== PONTOS DE ARTICULACAO ==========\n");

    for (int i = 0; i < V; i++) {

        if (articulacao[i] == 1) {

            printf("Vertice ");

            exibirVertice(i);

            printf(" e um ponto de articulacao.\n");

            encontrou = 1;

        }

    }

    if (!encontrou) {

        printf("Nenhum ponto de articulacao encontrado.\n");

    }

}


/*
 * Exibe os tempos de descoberta e os valores low.
 *
 * Essa função ajuda a visualizar o funcionamento
 * interno do algoritmo de Tarjan.
 */
void exibirInformacoes() {

    printf("\n========== INFORMACOES DA DFS ==========\n");

    printf("Vertice | Descoberta | Low\n");

    printf("----------------------------------------\n");

    for (int i = 0; i < V; i++) {

        printf("   %c    |     %d      | %d\n",
            'A' + i,
            descoberta[i],
            low[i]
        );

    }

}


/*
 * Função principal.
 */
int main() {

    printf("========== ANALISE DE CONECTIVIDADE ==========\n");

    printf("Grafo com vertices A, B, C, D, E, F e G.\n");


    /*
     * Executa o algoritmo de Tarjan.
     */
    executarTarjan();


    /*
     * Exibe os resultados.
     */
    exibirInformacoes();

    exibirArticulacoes();


    return 0;

}