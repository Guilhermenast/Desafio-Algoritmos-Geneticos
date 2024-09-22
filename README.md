# Algoritmos Genéticos em Python

Este repositório contém implementações de algoritmos genéticos para resolver problemas de otimização, incluindo a minimização de uma função matemática e o problema da mochila.

## Estrutura do Projeto

O projeto contém dois arquivos principais:

1. **ValordeXnaFuncao.py**: 
   - **Descrição**: Implementa um algoritmo genético para encontrar o valor mínimo da função \( f(x) = x^3 - 6x + 14 \) em um intervalo definido. 
   - **Funcionamento**: O algoritmo utiliza uma população de indivíduos representados em binário, realiza seleção, mutação e crossover para otimizar a solução ao longo de várias gerações.
   - **Parâmetros**: 
     - `num_geracoes`: Número de gerações a serem processadas.
     - `taxa_mutacao`: Probabilidade de mutação em cada indivíduo.
     - `tipo_crossover`: Tipo de crossover a ser utilizado (1 ou 2).
     - `elitismo`: Indica se a estratégia de elitismo será aplicada.
     - `percentual_elite`: Percentual de indivíduos que serão mantidos na próxima geração.

2. **ProblemaDaMochila.py**: 
   - **Descrição**: Resolve o problema da mochila, onde o objetivo é maximizar o valor total de itens que podem ser colocados em uma mochila, respeitando um limite de peso.
   - **Funcionamento**: O algoritmo gera uma população de cromossomos, avalia sua aptidão com base no valor total dos itens que não excedem o peso máximo, e aplica operações de seleção, mutação e crossover ao longo de várias gerações.
   - **Parâmetros**: 
     - `pesos_e_valores`: Lista de pares de peso e valor de cada item.
     - `peso_maximo`: Limite de peso que a mochila pode suportar.
     - `numero_de_cromossomos`: Número de indivíduos na população.
     - `geracoes`: Número de gerações para o algoritmo evoluir.

## Como Executar
Para executar os scripts, certifique-se de ter o Python instalado em sua máquina. Em seguida, execute os arquivos da seguinte maneira:

python ValordeXnaFuncao.py

python ProblemaDaMochila.py
