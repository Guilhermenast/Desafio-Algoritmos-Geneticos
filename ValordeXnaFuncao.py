import numpy as np
import random

def funcao_objetivo(x):
    return x**3 - 6*x + 14

def decodificar_individuo(individuo_bin, intervalo=(-10, 10)):
    max_bin = 2**len(individuo_bin) - 1
    decimal = int(''.join(map(str, individuo_bin)), 2)
    return intervalo[0] + decimal * (intervalo[1] - intervalo[0]) / max_bin

def gerar_individuo(tamanho_cromossomo):
    return [random.randint(0, 1) for _ in range(tamanho_cromossomo)]

def gerar_populacao(tamanho_populacao, tamanho_cromossomo):
    return [gerar_individuo(tamanho_cromossomo) for _ in range(tamanho_populacao)]

def selecao_torneio(populacao, fitness, tamanho_torneio=3):
    selecionados = random.sample(list(zip(populacao, fitness)), tamanho_torneio)
    selecionados.sort(key=lambda x: x[1])
    return selecionados[0][0] 

def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  
    return individuo

def crossover(pai1, pai2, tipo_crossover=1):
    if tipo_crossover == 1:
        ponto_corte = random.randint(1, len(pai1) - 1)
        return pai1[:ponto_corte] + pai2[ponto_corte:], pai2[:ponto_corte] + pai1[ponto_corte:]
    else:
        ponto1 = random.randint(1, len(pai1) - 2)
        ponto2 = random.randint(ponto1 + 1, len(pai1) - 1)
        return (pai1[:ponto1] + pai2[ponto1:ponto2] + pai1[ponto2:], 
                pai2[:ponto1] + pai1[ponto1:ponto2] + pai2[ponto2:])

def aplicar_elitismo(populacao, fitness, percentual_elite):
    num_elite = int(len(populacao) * percentual_elite)
    elite_indices = np.argsort(fitness)[:num_elite]
    return [populacao[i] for i in elite_indices]

def algoritmo_genetico(tamanho_populacao=10, tamanho_cromossomo=16, 
                       num_geracoes=100, taxa_mutacao=0.01, tipo_crossover=1, 
                       metodo_selecao='torneio', elitismo=False, percentual_elite=0.1):
    
    populacao = gerar_populacao(tamanho_populacao, tamanho_cromossomo)
    
    for geracao in range(num_geracoes):
        fitness = [funcao_objetivo(decodificar_individuo(ind)) for ind in populacao]
        
        melhor_indice = np.argmin(fitness)
        melhor_individuo = populacao[melhor_indice]
        melhor_x = decodificar_individuo(melhor_individuo)
        melhor_valor = funcao_objetivo(melhor_x)
        
        print(f"Geração {geracao + 1}: x = {melhor_x:.4f}, f(x) = {melhor_valor:.4f}")
        
        nova_populacao = []
        
        if elitismo:
            elite = aplicar_elitismo(populacao, fitness, percentual_elite)
            nova_populacao.extend(elite)
        
        while len(nova_populacao) < tamanho_populacao:

            if metodo_selecao == 'torneio':
                pai1 = selecao_torneio(populacao, fitness)
                pai2 = selecao_torneio(populacao, fitness)
            
            filho1, filho2 = crossover(pai1, pai2, tipo_crossover)
            
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            
            nova_populacao.append(filho1)
            if len(nova_populacao) < tamanho_populacao:
                nova_populacao.append(filho2)
        
        populacao = nova_populacao
    
    fitness_final = [funcao_objetivo(decodificar_individuo(ind)) for ind in populacao]
    melhor_indice = np.argmin(fitness_final)
    melhor_individuo = populacao[melhor_indice]
    melhor_x = decodificar_individuo(melhor_individuo)
    melhor_valor = funcao_objetivo(melhor_x)
    
    print("\nMelhor solução encontrada:")
    print(f"x = {melhor_x:.4f}, f(x) = {melhor_valor:.4f}")

algoritmo_genetico(num_geracoes=50, taxa_mutacao=0.01, tipo_crossover=1, elitismo=True, percentual_elite=0.2)