from cidades_map import CidadesMap
from algoritmo_genetico import AlgoritmoGenetico
import visual 

if __name__ == '__main__':
    mapa = CidadesMap('cidades.mat')
    ag = AlgoritmoGenetico(mapa, tamanho_populacao=20, num_geracoes=1000)
    resultado = ag.executar()
    
    print("---------------------------------------------")
    print("Resultados do Algoritmo Genético:")
    print(f"Tamanho da População: {resultado['tamanhoPopulacao']}")
    print(f"Número de Cidades: {mapa.num_cidades}")

    print("\nPopulação Inicial:")
    for i, ind in enumerate(resultado['populacaoInicial']):
        print(f"  Indivíduo {i+1}: {ind}")

    print("\nPopulação Final:")
    for i, ind in enumerate(resultado['populacaoFinal']):
        print(f"  Indivíduo {i+1}: {ind}")

    print(f"\nMelhor Custo: {float(resultado['melhorCusto']):.2f}")
    print(f"Melhor Solução: {resultado['melhorSolucao']}")

    visual.plot_caminho(mapa, resultado['melhorSolucao'])
