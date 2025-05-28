import numpy as np
cidade = np.loadtxt('cidades.mat')

pop_size = 20
n_cidades = 20
cidade = cidade.T

populacao = np.array([np.random.permutation(n_cidades) for _ in range(pop_size)])

print(populacao)
# Adiciona a primeira cidade no final do percurso (volta à cidade inicial)
tour = np.concatenate([populacao, populacao[:, [0]]], axis=1) # Axis=1 indica que estamos concatenando ao longo das colunas

def calcular_distancia(cromossomo):
    dist = 0
    for i in range(n_cidades):
        k = cromossomo[i]
        k1 = cromossomo[(i+1)]
        dx = cidade[k, 0] - cidade[k1, 0]
        dy = cidade[k, 1] - cidade[k1, 1]
        dist += np.sqrt(dx**2 + dy**2)
    return dist
distancias = []
for i in range(len(tour)):
    distancias.append(calcular_distancia(tour[i]))

distancias.sort(reverse=True)
print(distancias)
print('-------------------')
distancias = distancias[:10]
print(distancias)