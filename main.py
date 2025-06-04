import numpy as np
import random

# Carrega as coordenadas das cidades
cidades = np.loadtxt('cidades.mat').T

tamanho_populacao = 20
num_cidades = 20

# Gera a população inicial (cada indivíduo é uma permutação das cidades)
populacao = np.array([np.random.permutation(num_cidades) for _ in range(tamanho_populacao)])

# Fecha o ciclo do percurso adicionando a primeira cidade ao final
percursos = np.concatenate([populacao, populacao[:, [0]]], axis=1)

def calcular_distancia(percurso):
    distancia = 0
    for i in range(num_cidades):
        cidade_atual = percurso[i]
        proxima_cidade = percurso[(i + 1) % num_cidades]
        dx = cidades[cidade_atual, 0] - cidades[proxima_cidade, 0]
        dy = cidades[cidade_atual, 1] - cidades[proxima_cidade, 1]
        distancia += np.sqrt(dx**2 + dy**2)
    return distancia

def corrigir_percurso(percurso):
    cidades_vistas = set()
    for i in range(num_cidades):
        if percurso[i] in cidades_vistas:
            for cidade in range(num_cidades):
                if cidade not in cidades_vistas:
                    percurso[i] = cidade
                    break
        cidades_vistas.add(percurso[i])
    return percurso


def mutacao(percurso):
    # Seleciona dois índices aleatórios para trocar
    idx1, idx2 = random.sample(range(num_cidades), 2)
    percurso[idx1], percurso[idx2] = percurso[idx2], percurso[idx1]
    return percurso
geracoes = 0
# Simula um loop para evitar que o código seja interrompido prematuramente
while (geracoes < 10000):

    # Atualize percursos para refletir a população atual
    percurso = np.concatenate([populacao, populacao[:, [0]]], axis=1)

    # Calcula as distâncias de cada percurso
    distancias = np.array([calcular_distancia(cromossomo) for cromossomo in populacao])
    indices_ordenados = np.argsort(distancias)
    populacao = populacao[indices_ordenados]
    distancias = distancias[indices_ordenados]

    # print("População ordenada pelas distâncias:")
    populacao = populacao[:10]
    # print(populacao)
    # print("Distâncias ordenadas:")
    distancias = distancias[:10]
    # print(np.round(distancias, 2))

    # Cria a roleta proporcional à posição (melhor tem mais chances)
    chances = np.arange(len(populacao), 0, -1)  # [10, 9, ..., 1] se len(populacao)=10
    roleta = []
    for index, chance in enumerate(chances):
        roleta.extend([index] * chance)

    populacaoFilhos = []
    for i in range(5):
        # Seleciona dois pais aleatoriamente pela roleta, garantindo que sejam diferentes
        indice_pai1 = random.choice(roleta)
        indice_pai2 = random.choice(roleta)
        while indice_pai2 == indice_pai1:
            indice_pai2 = random.choice(roleta)
        pai1 = populacao[indice_pai1]
        pai2 = populacao[indice_pai2]

        # Gerar uma posição aleatória para o crossover entre 1 e num_cidades-1
        posicao_crossover = random.randint(1, num_cidades - 1)

        # Copia os pais para os filhos
        filho1 = pai1.copy()
        filho2 = pai2.copy()

        # Troca apenas o valor na posição do ponto de crossover
        filho1[posicao_crossover], filho2[posicao_crossover] = filho2[posicao_crossover], filho1[posicao_crossover]

        # Corrige duplicatas nos filhos para garantir permutação válida    
        filho1 = corrigir_percurso(filho1)
        filho2 = corrigir_percurso(filho2)

        # Realiza mutação trocando duas cidades aleatórias
        filho1 = mutacao(filho1)
        filho2 = mutacao(filho2)

        # Adiciona os filhos à população secundária para após gerar todos os 10 filhos, adicionar à população principal
        populacaoFilhos.extend([filho1, filho2])

        # print(f'Pais: {pai1}, {pai2}')
        # print(f'Filhos: {filho1}, {filho2}')
        # print(f'Distâncias: {calcular_distancia(filho1)}, {calcular_distancia(filho2)}')
        # print('-' * 40)
    # Adiciona os filhos à população principal, substituindo os pais anteriores
    populacao = np.array(populacaoFilhos)
    print("Geração:", geracoes + 1)
    geracoes += 1

# Calcula as distâncias finais
distancias_finais = np.array([calcular_distancia(cromossomo) for cromossomo in populacao])
indices_ordenados = np.argsort(distancias_finais)
populacao = populacao[indices_ordenados]
distancias_finais = distancias_finais[indices_ordenados]
print('População final:')
print(populacao)
print('Distâncias finais:')
print(np.round(distancias_finais, 2))