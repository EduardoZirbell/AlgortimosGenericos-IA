import numpy as np

class CidadesMap:
    def __init__(self, arquivo='cidades.mat'):
        self.coordenadas = np.loadtxt(arquivo).T
        self.num_cidades = self.coordenadas.shape[0]

    def calcular_distancia(self, percurso):
        distancia = 0
        for i in range(len(percurso)):
            cidade_atual = percurso[i]
            proxima_cidade = percurso[(i + 1) % len(percurso)]
            dx = self.coordenadas[ cidade_atual, 0] - self.coordenadas[proxima_cidade, 0]
            dy = self.coordenadas[ cidade_atual, 1] - self.coordenadas[proxima_cidade, 1]
            distancia += np.sqrt(dx ** 2 + dy ** 2)
        return distancia
