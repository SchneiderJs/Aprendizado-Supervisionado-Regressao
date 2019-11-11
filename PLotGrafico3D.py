import pandas as pd
import numpy as np
from math import sqrt
def correlacao(x, y):
    x_hat = np.average(x)
    y_hat = np.average(y)

    n = sum((x-x_hat)*(y-y_hat))
    d = sqrt(sum((x-x_hat)*(x-x_hat)) * sum((y-y_hat) *(y-y_hat)))

    return n / d

def regressao(x, y):
    x_hat = np.average(x)
    y_hat = np.average(y)

    a = (sum((x-x_hat)*(y-y_hat)))/(sum((x-x_hat)*(x-x_hat)))
    b = y_hat - a*x_hat

    return (a, b)

def get_predictions(a, b, points):
    line = []
    for p in points:
        line.append(a*p + b)
    return line

def plot_regression_3d(ptosX, ptosY, ptosZ, title):
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib
    import matplotlib.pyplot as plt
    # obtem resultados
    c = correlacao(ptosX, ptosY)
    a, b = regressao(ptosX, ptosY)

    ptos = [min(ptosX), max(ptosX)]
    line = get_predictions(a, b, ptos)

    # inicializacao
    ax = plt.subplot(111, projection="3d")

    # legendas
    ax.set_xlabel("Independente X", fontsize = 10)
    ax.set_ylabel("Dependente Y", fontsize = 10)
    ax.set_title(title, fontsize = 15)

    # plota os pontos
    ax.scatter(ptosX, ptosY, ptosZ, s = 20, color = "black", marker = "o")

    # plota reta
    plt.plot(ptos, line, color = "blue", linestyle="solid", linewidth=1)

    #plota coeficientes
    
    #exibe
    plt.show()
    pass

data = pd.read_csv('Dados/data.csv', header=None, names=['Tamanho', 'Quartos', 'Preco'])
data.head()

X = data[['Tamanho','Quartos']]
Y = data[['Preco']]

plot_regression_3d(X['Quartos'], X["Tamanho"], Y['Preco'], 'Quartos x Preço')
