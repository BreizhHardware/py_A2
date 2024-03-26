import matplotlib.pyplot as plot
import numpy as np
import math


def generer_abscisses(a, b, n):
    return np.linspace(a, b, n)


def tracer_courbe(f, a, b, n):
    x = generer_abscisses(a, b, n)
    y = f(x)
    plot.plot(x, y)
    plot.show()


def f1(x):
    return 2 * x + 3


def f2(x):
    return x ** 2


def plusieurs_courbes():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    plot.plot(x, y1, 'b', x, y2, 'r')
    plot.show()


def dessiner_cercle(x, y, r):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = x + r * np.cos(theta)
    y = y + r * np.sin(theta)
    plot.axis("equal")
    plot.plot(x, y)
    return plot


def cercle_dans_cercle():
    plot.axis("equal")
    fig, ax = plot.subplots()
    for i in range(10):
        cercle = dessiner_cercle(0, 0, i + 1)
        ax.add_patch(cercle)
    plot.show()




# Jeu de test
print(generer_abscisses(1, 10, 4))
print(generer_abscisses(1, 10, 10))
tracer_courbe(f1, -5, 20, 100)
tracer_courbe(f2, -2, 2, 100)
plusieurs_courbes()
l = [1, 42, -3]
a = np.array(l)
print(a)  # affiche [1 42 -3]
cos_a = np.cos(a)  # notez qu’il s’agit bien de np.cos() et pas de math.cos()
print(cos_a)  # affiche [ 0.54030231 -0.66939722 -0.9899925 ]
cercle = dessiner_cercle(0, 0, 1)
cercle.show()
cercle_dans_cercle()