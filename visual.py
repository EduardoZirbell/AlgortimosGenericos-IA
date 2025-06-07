# visual.py

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def plot_caminho(cidade_map, percurso, titulo="Melhor Caminho Encontrado"):
    coordenadas = cidade_map.coordenadas
    percurso = list(percurso) + [percurso[0]]  # Voltar para a cidade inicial

    x = [coordenadas[cidade, 0] for cidade in percurso]
    y = [coordenadas[cidade, 1] for cidade in percurso]

    plt.figure(figsize=(8, 6))
    
    # Plotar o caminho
    plt.plot(x, y, 'o-', color='blue', linewidth=1, markersize=6, label='Caminho')
    
    # Marcar o ponto inicial em verde
    plt.plot(x[0], y[0], 'go', markersize=12, label='Início')
    
    # Marcar o ponto final em vermelho (último ponto antes de voltar ao início)
    plt.plot(x[-2], y[-2], 'ro', markersize=12, label='Fim')

    plt.title(titulo)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    # Formatador para 2 casas decimais nos eixos
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    plt.legend()
    plt.show()
