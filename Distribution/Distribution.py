import numpy as np
import scipy as sp
import math
import random
from scipy.stats import expon
import matplotlib.pyplot as plt



def draw_plot(n, ax : plt.axes):
    # получаем выборку
    X = np.array([expon.rvs(size=n).mean() for i in range(1000)])
    # полючаем параметры нормального распределения
    Lambda = 1
    mu = Lambda
    disp = Lambda / n
    sigma = disp ** 0.5
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - mu) ** 2 / (2 * sigma ** 2))


    ax.hist(X, density=True, label='random sampling')
    ax.plot(x, y, label='theoretical sampling')
    ax.set_xlabel('x', size=7)
    ax.set_ylabel('dansity', size=7)
    ax.set_title(f'normal distribution of {n} elements', size=7 )


if __name__ == "__main__":

    fig, ax = plt.subplots(2, 3, figsize=(11, 9))

    # теоретическое экспоненциальное распределение
    x = np.linspace(0, 10, 1000)
    # случайная выборка
    rvs = expon.rvs(size=1000)

    # строим и подписываем графики
    ax[0, 0].plot(x, np.exp(-x), label='theoretical sampling')
    ax[0, 0].hist(rvs, bins=15, density=True, label='random sampling')
    ax[0, 0].set_xlabel('x', size=7)
    ax[0, 0].set_ylabel('dansity', size=7)
    ax[0, 0].set_title('Exponential distribution', size=7)

    draw_plot(5, ax[1, 0])
    draw_plot(10, ax[0, 1])
    draw_plot(50, ax[1, 1])
    draw_plot(200, ax[0, 2])

    plt.show()


