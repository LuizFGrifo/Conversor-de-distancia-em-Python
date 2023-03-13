# Conversor de Unidades de Comprimento

Este projeto consiste em um simples programa que realiza a conversão entre as unidades de comprimento anos luz e quilômetros (km). O programa foi desenvolvido em Python e contém as seguintes funções:

### float_input(prompt)

Essa função recebe um prompt e lê a entrada do usuário como uma string. Em seguida, tenta converter a string em um número float, substituindo as vírgulas por pontos para garantir a compatibilidade com o padrão americano. Se a conversão não for possível, a função imprime uma mensagem de erro e solicita uma nova entrada. A função retorna o número float quando a entrada é válida.

### anoLuzKm()

Essa função solicita ao usuário que digite a quantidade de anos luz que deseja converter em quilômetros (km). A função utiliza a fórmula 1 ano luz = 9,461e+12 km para realizar a conversão. Em seguida, imprime o resultado formatado com três casas decimais.

### kmAnoLuz()

Essa função solicita ao usuário que digite a quantidade de quilômetros (km) que deseja converter em anos luz. A função utiliza a fórmula 1 km = 9,461e-13 anos luz para realizar a conversão. Em seguida, imprime o resultado sem formatação.

### Como utilizar o programa

Ao executar o programa, o usuário é apresentado com o menu de opções:

********* Bem vindo ao conversor de unidade de comprimento !!! *********

0 - sair\
1 - converter anos luz para km\
2 - converter km para anos luz\
:

O usuário pode escolher uma das opções digitando o número correspondente e pressionando Enter. Se a opção escolhida for inválida, o programa imprime uma mensagem de erro e solicita uma nova entrada.

Caso a opção escolhida seja "sair", o programa é encerrado. Caso contrário, a função correspondente é chamada e o usuário pode realizar a conversão desejada.

### Requisitos do sistema

O programa foi desenvolvido em Python 3 e não requer nenhuma biblioteca adicional para ser executado. O usuário deve ter o Python 3 instalado em seu sistema para executar o programa.