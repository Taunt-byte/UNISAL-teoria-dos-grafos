
/*
===========================================================
Projeto: Teoria dos Grafos
Assunto: Representação de Grafos
Linguagem: C
Estrutura: Lista de Adjacência

Descrição:
    O programa representa um grafo não direcionado e não
    ponderado utilizando uma lista de adjacência.

    A estrutura é implementada por meio de structs e
    vetores estáticos em linguagem C.

    Cada posição da lista representa um vértice.
    Cada vetor interno armazena os vértices adjacentes,
    ou seja, aqueles que possuem uma conexão direta.

Funcionalidades:
    1. Inicializar a estrutura do grafo.
    2. Exibir todos os vértices e suas conexões.
    3. Listar os vértices existentes.
    4. Consultar os vértices adjacentes a um vértice.

Estruturas utilizadas:
    - Struct: organiza os dados de cada vértice.
    - Vetores: armazenam os vértices adjacentes.
    - Ponteiros: permitem acessar o grafo pelas funções.

Tipo de grafo:
    Não direcionado e não ponderado.

Representação:
    Lista de adjacência com vetores estáticos.

Autor: Lucas Neves
===========================================================
*/


#include <stdio.h>


// =========================================================
// DEFINIÇÃO DE CONSTANTES
// =========================================================

// Quantidade total de vértices existentes no grafo.
#define NUM_VERTICES 6

// Quantidade máxima de adjacências que cada vértice
// pode armazenar.
#define MAX_ADJACENTES 6


// =========================================================
// DEFINIÇÃO DAS ESTRUTURAS
// =========================================================

// Estrutura responsável por representar a lista
// de adjacência de um único vértice.
//
// vertices: armazena os vértices conectados diretamente.
// quantidade: informa quantos adjacentes estão cadastrados.

typedef struct {

    int vertices[MAX_ADJACENTES];

    int quantidade;

} ListaAdjacencia;


// Estrutura geral responsável por representar o grafo.
//
// Cada posição do vetor lista representa um vértice
// e contém sua respectiva lista de adjacência.

typedef struct {

    ListaAdjacencia lista[NUM_VERTICES];

} Grafo;


// =========================================================
// FUNÇÃO: INICIALIZAR O GRAFO
// =========================================================

void definirGrafo(Grafo *grafo) {

    /*
    Matriz auxiliar utilizada para cadastrar as conexões.

    Cada linha representa um vértice.
    Cada elemento representa um vértice adjacente.

    Exemplo:
        {2, 5} significa que o vértice 1 está conectado
        diretamente aos vértices 2 e 5.
    */

    int adjacentes[NUM_VERTICES][MAX_ADJACENTES] = {

        {2, 5},       // Vértice 1
        {1, 3, 5},    // Vértice 2
        {2, 4},       // Vértice 3
        {3, 5, 6},    // Vértice 4
        {1, 2, 4},    // Vértice 5
        {4}           // Vértice 6

    };


    // Quantidade de conexões existentes em cada vértice.
    //
    // Essa informação é necessária porque nem todos
    // os vértices possuem a mesma quantidade de adjacentes.

    int quantidades[NUM_VERTICES] = {2, 3, 2, 3, 3, 1};


    // Percorre todos os vértices do grafo.
    for (int i = 0; i < NUM_VERTICES; i++) {

        // Registra a quantidade de adjacentes do vértice atual.
        grafo->lista[i].quantidade = quantidades[i];


        // Percorre as conexões existentes no vértice atual.
        for (int j = 0; j < quantidades[i]; j++) {

            // Copia cada vértice adjacente para sua
            // respectiva lista de adjacência.
            grafo->lista[i].vertices[j] = adjacentes[i][j];

        }
    }
}


// =========================================================
// FUNÇÃO: EXIBIR A ESTRUTURA DO GRAFO
// =========================================================

void mostrarGrafo(const Grafo *grafo) {

    printf("\n========== ESTRUTURA DO GRAFO ==========\n");


    // Percorre todos os vértices existentes.
    for (int i = 0; i < NUM_VERTICES; i++) {

        // Exibe o número do vértice.
        //
        // O índice começa em zero, por isso somamos 1
        // para apresentar os vértices de 1 até 6.
        printf("Vertice %d: ", i + 1);


        // Percorre e exibe os vértices adjacentes.
        for (int j = 0; j < grafo->lista[i].quantidade; j++) {

            printf("%d ", grafo->lista[i].vertices[j]);

        }

        printf("\n");
    }
}


// =========================================================
// FUNÇÃO: EXIBIR OS VÉRTICES EXISTENTES
// =========================================================

void mostrarVertices() {

    printf("\n========== VERTICES DO GRAFO ==========\n");


    // Percorre a quantidade total de vértices.
    for (int i = 0; i < NUM_VERTICES; i++) {

        // Exibe o número do vértice.
        printf("%d ", i + 1);

    }

    printf("\n");
}


// =========================================================
// FUNÇÃO: ENCONTRAR VÉRTICES ADJACENTES
// =========================================================

void encontrarAdjacentes(const Grafo *grafo) {

    // Variável responsável por armazenar
    // o vértice informado pelo usuário.
    int vertice;


    // Solicita o vértice que será consultado.
    printf("\nInforme o vertice para encontrar os adjacentes: ");


    // Lê o valor informado pelo usuário.
    //
    // Verifica se a leitura foi realizada corretamente.
    if (scanf("%d", &vertice) != 1) {

        printf("\nEntrada invalida!\n");

        return;
    }


    // Verifica se o vértice informado está dentro
    // do intervalo permitido pelo grafo.
    if (vertice < 1 || vertice > NUM_VERTICES) {

        printf("\nVertice nao encontrado.\n");

        return;
    }


    // Converte o número do vértice para o índice do vetor.
    //
    // O usuário informa vértices de 1 até 6,
    // mas os vetores em C começam no índice 0.
    int indice = vertice - 1;


    // Exibe os vértices adjacentes ao vértice escolhido.
    printf("\nVertices adjacentes a %d: ", vertice);


    // Percorre a lista de adjacência do vértice informado.
    for (int i = 0; i < grafo->lista[indice].quantidade; i++) {

        // Exibe cada conexão encontrada.
        printf("%d ", grafo->lista[indice].vertices[i]);

    }

    printf("\n");
}


// =========================================================
// FUNÇÃO PRINCIPAL
// =========================================================

int main() {

    // Declara uma variável do tipo Grafo.
    //
    // A estrutura possui espaço suficiente para armazenar
    // todos os vértices e suas respectivas conexões.
    Grafo grafo;


    // Inicializa o grafo com as conexões cadastradas.
    //
    // O operador & fornece o endereço de memória
    // da estrutura para a função definirGrafo().
    definirGrafo(&grafo);


    // Exibe a estrutura completa do grafo.
    mostrarGrafo(&grafo);


    // Apresenta todos os vértices existentes.
    mostrarVertices();


    // Permite consultar os vértices adjacentes
    // a partir de um vértice informado pelo usuário.
    encontrarAdjacentes(&grafo);


    // Finaliza a execução do programa.
    return 0;
}
