from populacao import Populacao

class AlgoritmoGenetico:
    def __init__(self, cidade_map, tamanho_populacao=20, num_geracoes=1000):
        self.cidade_map = cidade_map
        self.tamanho_populacao = tamanho_populacao
        self.num_geracoes = num_geracoes
        self.populacao = Populacao(tamanho_populacao, cidade_map)

    def executar(self):
        populacaoInicial = [ind.percurso.copy() for ind in self.populacao.individuos]

        for geracao in range(self.num_geracoes):
            self.populacao.selecionar_melhores(self.tamanho_populacao // 2)
            self.populacao.cruzar()

            melhor = min(self.populacao.individuos, key=lambda ind: ind.distancia)
            print(f"Geração {geracao + 1}: Melhor distância = {melhor.distancia:.2f}")

            melhorFinal = None
            menorDistancia = float('inf')
            populacaoFinal = []

        for individuo in self.populacao.individuos:
            percurso = individuo.percurso.copy()
            populacaoFinal.append(percurso)
            if individuo.distancia < menorDistancia:
                menorDistancia = individuo.distancia
                melhorFinal = individuo

        return {
            "tamanhoPopulacao": self.tamanho_populacao,
            "populacaoInicial": populacaoInicial,
            "populacaoFinal": populacaoFinal,
            "melhorCusto": melhorFinal.distancia,
            "melhorSolucao": melhorFinal.percurso
        }

