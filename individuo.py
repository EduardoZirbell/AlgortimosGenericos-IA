import numpy as np
import random

class Individuo:
    def __init__(self, percurso, cidade_map):
        # Cria um indivíduo com um percurso e calcula sua distância
        self.percurso = list(percurso)
        self.cidade_map = cidade_map
        self.distancia = self.cidade_map.calcular_distancia(self.percurso)

    def mutar(self):
        # Troca duas cidades de lugar no percurso (mutação simples)
        i, j = random.sample(range(len(self.percurso)), 2)
        self.percurso[i], self.percurso[j] = self.percurso[j], self.percurso[i]
        # Atualiza a distância após a mutação
        self.distancia = self.cidade_map.calcular_distancia(self.percurso)
