import random
import numpy as np

class Individuo:
    def __init__(self, percurso, cidade_map):
        self.percurso = np.array(percurso)
        self.cidade_map = cidade_map
        self.distancia = self.cidade_map.calcular_distancia(self.percurso)

    def corrigir_percurso(self):
        cidades_vistas = set()
        for i in range(len(self.percurso)):
            if self.percurso[i] in cidades_vistas:
                for cidade in range(self.cidade_map.num_cidades):
                    if cidade not in cidades_vistas:
                        self.percurso[i] = cidade
                        break
            cidades_vistas.add(self.percurso[i])
        self.distancia = self.cidade_map.calcular_distancia(self.percurso)

    def mutar(self):
        idx1, idx2 = random.sample(range(self.cidade_map.num_cidades), 2)
        self.percurso[idx1], self.percurso[idx2] = self.percurso[idx2], self.percurso[idx1]
        self.distancia = self.cidade_map.calcular_distancia(self.percurso)
