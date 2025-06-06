import numpy as np
import random
from individuo import Individuo

class Populacao:
    def __init__(self, tamanho, cidade_map):
        self.cidade_map = cidade_map
        self.individuos = [Individuo(np.random.permutation(cidade_map.num_cidades), cidade_map) for _ in range(tamanho)]

    def selecionar_melhores(self, n):
        self.individuos.sort(key=lambda ind: ind.distancia)
        self.individuos = self.individuos[:n]

    def cruzar(self):
        nova_geracao = []
        chances = np.arange(len(self.individuos), 0, -1)
        roleta = []
        for index, chance in enumerate(chances):
            roleta.extend([index] * chance)

        for _ in range(len(self.individuos) // 2):
            indice_indice_pai1 = self.individuos[random.choice(roleta)]
            indice_pai2 = self.individuos[random.choice(roleta)]
            while indice_pai2 == indice_indice_pai1:
                indice_pai2 = self.individuos[random.choice(roleta)]

            posicao_crossover = random.randint(1, self.cidade_map.num_cidades - 1)
            filho1 = Individuo(indice_indice_pai1.percurso.copy(), self.cidade_map)
            filho2 = Individuo(indice_pai2.percurso.copy(), self.cidade_map)
            filho1.percurso[posicao_crossover], filho2.percurso[posicao_crossover] = filho2.percurso[posicao_crossover], filho1.percurso[posicao_crossover]
            filho1.corrigir_percurso()
            filho2.corrigir_percurso()
            filho1.mutar()
            filho2.mutar()
            nova_geracao.extend([filho1, filho2])
        self.individuos = nova_geracao
