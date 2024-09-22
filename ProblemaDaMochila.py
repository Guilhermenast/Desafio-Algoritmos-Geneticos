import numpy as np
import random

def funcao_objetivo(individuo, pesos_e_valores, peso_maximo):
    valor_total = sum(valores * individuo[i] for i, (peso, valores) in enumerate(pesos_e_valores))
    peso_total = sum(peso * individuo[i] for i, (peso, valores) in enumerate(pesos_e_valores))
    
    if peso_total > peso_maximo:
        return 0 
    return valor_total

def gerar_individuo(tamanho):
    return [random.randint(0, 1) for _ in range(tamanho)]

def gerar_populacao(tamanho_populacao, tamanho_individuo):
    return [gerar_individuo(tamanho_individuo) for _ in range(tamanho_populacao)]

def selecao_torneio(populacao, fitness, tamanho_torneio=3):
    selecionados = random.sample(list(zip(populacao, fitness)), tamanho_torneio)
    selecionados.sort(key=lambda x: x[1], reverse=True)  
    return selecionados[0][0]

def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i] 
    return individuo

def crossover(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

def algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos=150, geracoes=50, taxa_mutacao=0.01):
    tamanho_individuo = len(pesos_e_valores)
    populacao = gerar_populacao(numero_de_cromossomos, tamanho_individuo)
    resultados = []
    
    for geracao in range(geracoes):
        fitness = [funcao_objetivo(ind, pesos_e_valores, peso_maximo) for ind in populacao]
        
        melhor_indice = np.argmax(fitness)
        melhor_individuo = populacao[melhor_indice]
        melhor_valor = fitness[melhor_indice]
        
        resultados.append([melhor_valor, melhor_individuo])
        
        print(f"Geração {geracao + 1}: Valor = {melhor_valor}, Indivíduo = {melhor_individuo}")
        
        nova_populacao = []
        
        while len(nova_populacao) < numero_de_cromossomos:
            pai1 = selecao_torneio(populacao, fitness)
            pai2 = selecao_torneio(populacao, fitness)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutacao(filho1, taxa_mutacao))
            nova_populacao.append(mutacao(filho2, taxa_mutacao))

        populacao = nova_populacao[:numero_de_cromossomos]
    
    return resultados 

# Exemplo de entrada
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300],
                   [12, 50], [25, 75], [50, 100], [100, 400]]
peso_maximo = 100
numero_de_cromossomos = 150
geracoes = 50

# Executando o algoritmo genético
resultados = algoritmo_genetico(pesos_e_valores, peso_maximo, numero_de_cromossomos, geracoes)

# Obtendo o melhor resultado da última geração
melhor_valor_final, melhor_individuo_final = resultados[-1]

# Imprimindo o resultado final
print("\nResultado Final:")
print(f"Soma dos Valores: {melhor_valor_final}, Indivíduo: {melhor_individuo_final}")
