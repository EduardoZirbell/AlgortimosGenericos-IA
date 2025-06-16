import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def plot_caminho(cidade_map, percurso, titulo="Melhor Caminho Encontrado"):
    # Pega as coordenadas das cidades
    coordenadas = cidade_map.coordenadas
    # Adiciona a cidade inicial no final do percurso para fechar o ciclo
    percurso = list(percurso) + [percurso[0]]

    # Separa as coordenadas X e Y de cada cidade do percurso
    x = [coordenadas[cidade, 0] for cidade in percurso]
    y = [coordenadas[cidade, 1] for cidade in percurso]

    plt.figure(figsize=(8, 6))

    # Desenha o caminho ligando as cidades
    plt.plot(x, y, 'o-', color='blue', linewidth=1, markersize=6, label='Caminho')

    # Marca o ponto inicial em verde
    plt.plot(x[0], y[0], 'go', markersize=12, label='Início')

    # Marca o ponto final em vermelho (última cidade antes de voltar ao início)
    plt.plot(x[-2], y[-2], 'ro', markersize=12, label='Fim')

    # Escreve o número de cada cidade em cima do ponto dela
    for idx, cidade in enumerate(percurso[:-1]):  # Ignora o último, que é repetido
        plt.text(
            coordenadas[cidade, 0],
            coordenadas[cidade, 1],
            str(cidade),
            fontsize=10,
            ha='center',
            va='center',
            color='black',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', boxstyle='round,pad=0.2')
        )

    plt.title(titulo)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    # Deixa os números dos eixos com 2 casas decimais
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    plt.legend()
    plt.show()
