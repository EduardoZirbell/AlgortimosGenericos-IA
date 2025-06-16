import numpy as np

class CidadesMap:
    def __init__(self, arquivo='cidades.mat'):
        # Carrega as coordenadas das cidades a partir do arquivo
        self.coordenadas = np.loadtxt(arquivo).T
        self.num_cidades = self.coordenadas.shape[0]

    def calcular_distancia(self, percurso):
        # Calcula a soma das distâncias entre cidades vizinhas no percurso
        distancia_total = 0
        for i in range(len(percurso)):
            cidade_atual = percurso[i]
            # A próxima cidade é a próxima no percurso, ou a primeira se for a última (fecha o ciclo)
            proxima_cidade = percurso[(i + 1) % len(percurso)]
            # Calcula a distância entre as duas cidades
            distancia = np.linalg.norm(self.coordenadas[cidade_atual] - self.coordenadas[proxima_cidade])
            distancia_total += distancia
        return distancia_total
