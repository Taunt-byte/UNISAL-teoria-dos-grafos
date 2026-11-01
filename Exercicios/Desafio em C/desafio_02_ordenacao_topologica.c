/*
 * ============================================================
 * DESAFIO 02 — ORDENACAO TOPOLOGICA COM ALGORITMO DE KAHN
 * ============================================================
 *
 * ENUNCIADO:
 *
 * Desenvolva um programa capaz de organizar tarefas de
 * um projeto considerando suas dependências.
 *
 * Imagine um projeto de desenvolvimento de software no qual
 * determinadas atividades precisam ser concluídas antes
 * que outras possam começar.
 *
 * O programa deverá:
 *
 * 1. Representar as tarefas como vértices.
 * 2. Representar as dependências como arestas direcionadas.
 * 3. Calcular o grau de entrada dos vértices.
 * 4. Encontrar uma ordem válida de execução.
 * 5. Identificar dependências circulares.
 *
 * CONCEITO:
 *
 * A ordenação topológica é aplicável a grafos direcionados
 * acíclicos, também conhecidos como DAGs.
 *
 * O algoritmo de Kahn utiliza uma fila para processar
 * os vértices que possuem grau de entrada igual a zero.
 *
 * Complexidade: O(V + E).
 *
 * ============================================================
 */

#include <stdio.h>

#define V 6

/*
 * Representação dos vértices:
 *
 * 0 = Planejamento
 * 1 = Modelagem
 * 2 = Documentacao
 * 3 = Desenvolvimento
 * 4 = Testes
 * 5 = Implantacao
 */
const char *tarefas[V] = {
    "Planejamento",
    "Modelagem",
    "Documentacao",
    "Desenvolvimento",
    "Testes",
    "Implantacao"
};


/*
 * Matriz de adjacência.
 *
 * matriz[i][j] = 1 significa que existe uma aresta
 * direcionada de i para j.
 *
 * Uma dependência A -> B significa que A precisa
 * ser concluída antes de B.
 */
int grafo[V][V] = {

    // P  M  D  D  T  I
    { 0, 1, 1, 0, 0, 0 }, // Planejamento
    { 0, 0, 0, 1, 0, 0 }, // Modelagem
    { 0, 0, 0, 1, 0, 0 }, // Documentacao
    { 0, 0, 0, 0, 1, 0 }, // Desenvolvimento
    { 0, 0, 0, 0, 0, 1 }, // Testes
    { 0, 0, 0, 0, 0, 0 }  // Implantacao

};


/*
 * Calcula o grau de entrada de cada vértice.
 *
 * O grau de entrada representa a quantidade
 * de arestas que chegam até determinado vértice.
 */
void calcularGrauEntrada(int grauEntrada[]) {

    /*
     * Inicializa todos os graus com zero.
     */
    for (int i = 0; i < V; i++) {

        grauEntrada[i] = 0;

    }

    /*
     * Percorre a matriz de adjacência.
     *
     * Quando encontramos uma aresta i -> j,
     * incrementamos o grau de entrada de j.
     */
    for (int i = 0; i < V; i++) {

        for (int j = 0; j < V; j++) {

            if (grafo[i][j] == 1) {

                grauEntrada[j]++;

            }

        }

    }

}


/*
 * Executa o algoritmo de Kahn.
 *
 * A fila é implementada manualmente utilizando um vetor.
 *
 * Retorna:
 * 1 -> ordenação topológica encontrada.
 * 0 -> o grafo possui ciclo.
 */
int ordenacaoTopologica() {

    int grauEntrada[V];

    int fila[V];

    int ordem[V];

    int inicio = 0;

    int fim = 0;

    int quantidadeProcessada = 0;


    /*
     * Calcula o grau de entrada de todos os vértices.
     */
    calcularGrauEntrada(grauEntrada);


    /*
     * ETAPA 1 — INICIALIZAÇÃO DA FILA
     *
     * Os vértices com grau de entrada zero
     * não possuem dependências pendentes.
     */
    for (int i = 0; i < V; i++) {

        if (grauEntrada[i] == 0) {

            fila[fim] = i;

            fim++;

        }

    }


    /*
     * ETAPA 2 — PROCESSAMENTO DOS VÉRTICES
     */
    while (inicio < fim) {

        /*
         * Remove o primeiro elemento da fila.
         */
        int atual = fila[inicio];

        inicio++;


        /*
         * Adiciona o vértice à ordenação.
         */
        ordem[quantidadeProcessada] = atual;

        quantidadeProcessada++;


        /*
         * Percorre os vizinhos do vértice atual.
         */
        for (int vizinho = 0; vizinho < V; vizinho++) {

            if (grafo[atual][vizinho] == 1) {

                /*
                 * A dependência correspondente à aresta
                 * atual -> vizinho foi resolvida.
                 *
                 * Portanto, diminuímos o grau de entrada.
                 */
                grauEntrada[vizinho]--;

                /*
                 * Se o grau de entrada chegou a zero,
                 * o vértice está disponível para execução.
                 */
                if (grauEntrada[vizinho] == 0) {

                    fila[fim] = vizinho;

                    fim++;

                }

            }

        }

    }


    /*
     * ETAPA 3 — VERIFICAÇÃO DE CICLO
     *
     * Se todos os vértices foram processados,
     * o grafo é um DAG.
     *
     * Caso contrário, existe uma dependência circular.
     */
    if (quantidadeProcessada != V) {

        printf("\nErro: dependencias circulares encontradas.\n");

        printf("Nao existe uma ordenacao topologica valida.\n");

        return 0;

    }


    /*
     * ETAPA 4 — EXIBIÇÃO DA ORDEM
     */
    printf("\n========== ORDEM DE EXECUCAO ==========\n");

    for (int i = 0; i < quantidadeProcessada; i++) {

        printf("%d. %s\n", i + 1, tarefas[ordem[i]]);

    }

    return 1;

}


/*
 * Exibe as dependências cadastradas.
 */
void exibirDependencias() {

    printf("\n========== DEPENDENCIAS ==========\n");

    for (int i = 0; i < V; i++) {

        for (int j = 0; j < V; j++) {

            if (grafo[i][j] == 1) {

                printf("%s -> %s\n", tarefas[i], tarefas[j]);

            }

        }

    }

}


/*
 * Função principal.
 */
int main() {

    printf("========== SISTEMA DE DEPENDENCIAS ==========\n");

    exibirDependencias();

    ordenacaoTopologica();

    return 0;
}