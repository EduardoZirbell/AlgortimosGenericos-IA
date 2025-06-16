from cidades_map import CidadesMap
from algoritmo_genetico import AlgoritmoGenetico
import visual 

# Executa o algoritmo genético e exibe os resultados
if __name__ == '__main__':
    mapa = CidadesMap('cidades.mat')
    ag = AlgoritmoGenetico(mapa, tam_pop=20, geracoes=10000, elitismo=False)
    resultado = ag.executar()
    
    print("---------------------------------------------")
    print("Resultados do Algoritmo Genético:")
    print(f"Tamanho da População: {resultado['tam_pop']}")
    print(f"Número de Cidades: {mapa.num_cidades}")

    print("\nPopulação Inicial:")
    for i, ind in enumerate(resultado['pop_inicial']):
        custo = mapa.calcular_distancia(ind)
        print(f"  Indivíduo {i+1}: {ind} | Custo: {custo:.2f}")

    print("\nPopulação Final:")
    for i, ind in enumerate(resultado['pop_final']):
        custo = mapa.calcular_distancia(ind)
        print(f"  Indivíduo {i+1}: {ind} | Custo: {custo:.2f}")

    print(f"\nMelhor Custo: {float(resultado['melhor_dist']):.2f}")
    print(f"Melhor Solução: {resultado['melhor_caminho']}")

    visual.plot_caminho(mapa, resultado['melhor_caminho'])
