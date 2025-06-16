import numpy as np
import random
from individuo import Individuo

class Populacao:
    def __init__(self, tamanho, cidade_map):
        # Cria a população inicial com percursos aleatórios
        self.cidade_map = cidade_map
        self.individuos = [Individuo(np.random.permutation(cidade_map.num_cidades), cidade_map) for _ in range(tamanho)]

    def cruzar(self):
        # Realiza o cruzamento usando Cycle Crossover (CX) e aplica mutação
        nova_geracao = []
        # Cria a roleta: 10 chances para o melhor, 9 para o segundo, ..., 1 para o décimo, 0 para o resto
        chances = [max(10 - i, 0) for i in range(len(self.individuos))]
        roleta = []
        for index, chance in enumerate(chances):
            roleta.extend([index] * chance)

        for _ in range(len(self.individuos) // 2):
            pai1 = self.individuos[random.choice(roleta)]
            pai2 = self.individuos[random.choice(roleta)]
            while pai2 == pai1:
                pai2 = self.individuos[random.choice(roleta)]

            # Cycle Crossover (CX) para gerar dois filhos
            size = len(pai1.percurso)
            filho1_p = [-1] * size
            filho2_p = [-1] * size

            # CX para filho1
            used = set()
            idx = 0
            while len(used) < size:
                if idx in used:
                    idx = next(i for i in range(size) if i not in used)
                start = idx
                while True:
                    filho1_p[idx] = pai1.percurso[idx]
                    used.add(idx)
                    idx = pai1.percurso.index(pai2.percurso[idx])
                    if idx == start:
                        break
                idx = next((i for i in range(size) if i not in used), size)

            # CX para filho2 (inverte os papéis dos pais)
            used = set()
            idx = 0
            while len(used) < size:
                if idx in used:
                    idx = next(i for i in range(size) if i not in used)
                start = idx
                while True:
                    filho2_p[idx] = pai2.percurso[idx]
                    used.add(idx)
                    idx = pai2.percurso.index(pai1.percurso[idx])
                    if idx == start:
                        break
                idx = next((i for i in range(size) if i not in used), size)

            # Cria os filhos e aplica mutação
            filho1 = Individuo(filho1_p, self.cidade_map)
            filho2 = Individuo(filho2_p, self.cidade_map)
            filho1.mutar()
            filho2.mutar()
            nova_geracao.extend([filho1, filho2])

        # Atualiza a população com a nova geração
        self.individuos = nova_geracao[:len(self.individuos)]