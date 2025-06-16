from populacao import Populacao

class AlgoritmoGenetico:
    def __init__(self, mapa, tam_pop=20, geracoes=10000, elitismo=False):
        # Inicializa o algoritmo genético com ou sem elitismo
        self.mapa = mapa
        self.tam_pop = tam_pop
        self.geracoes = geracoes
        self.elitismo = elitismo
        self.pop = Populacao(tam_pop, mapa)

    def executar(self):
        # Salva a população inicial
        pop_inicial = [ind.percurso.copy() for ind in self.pop.individuos]
        # Encontra o melhor indivíduo inicial
        melhor = min(self.pop.individuos, key=lambda ind: ind.distancia)

        for g in range(self.geracoes):
            if self.elitismo:
                # Salva o melhor indivíduo da geração atual
                melhor_geracao = min(self.pop.individuos, key=lambda ind: ind.distancia)
                self.pop.cruzar()
                # Substitui o pior indivíduo pelo melhor da geração anterior
                self.pop.individuos.sort(key=lambda ind: ind.distancia, reverse=True)
                self.pop.individuos[0] = melhor_geracao
            else:
                self.pop.cruzar()
            print(f"Geração {g + 1}: Melhor distância = {melhor.distancia:.2f}")

            melhor_geracao = min(self.pop.individuos, key=lambda ind: ind.distancia)
            if melhor_geracao.distancia < melhor.distancia:
                melhor = melhor_geracao

        # Seleciona os 10 melhores indivíduos da população final
        pop_final = [ind.percurso.copy() for ind in self.pop.individuos[:10]]

        # Retorna os resultados convertendo para inteiros comuns
        return {
            "tam_pop": self.tam_pop,
            "pop_inicial": [[int(x) for x in ind] for ind in pop_inicial],
            "pop_final": [[int(x) for x in ind] for ind in pop_final],
            "melhor_dist": melhor.distancia,
            "melhor_caminho": [int(x) for x in melhor.percurso]
        }

