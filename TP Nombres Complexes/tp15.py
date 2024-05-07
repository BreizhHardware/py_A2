import math
import cmath
import turtle
import time

z = 1 + 3j
print(z.real)
print(z.imag)
print(z.conjugate())
module = abs(4 + 3j)
print(module)
print(complex(1))
print(complex(1, 2))
print(complex(imag=1))
# complex('1+1 j')
# complex ('1 + 1 j')

# math.sqrt(-1)
print(cmath.sqrt(-1))

c = cmath.phase(complex(-1.0, 0.0))
print(c)
c = cmath.phase(complex(-1.0, -0.0))
print(c)

c = cmath.polar(1j)
print(c)

c = cmath.exp(1j * cmath.pi / 2)
print(c)


def triangle():
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)


def carre():
    turtle.left(45)
    turtle.forward(95)
    turtle.left(90)
    turtle.forward(95)
    turtle.left(90)
    turtle.forward(95)
    turtle.left(90)
    turtle.forward(95)
    turtle.left(90)


def pentagon():
    for i in range(5):
        turtle.forward(100)
        turtle.left(72)


def hexagon():
    for i in range(6):
        turtle.forward(100)
        turtle.left(60)


def octogone():
    for i in range(8):
        turtle.forward(100)
        turtle.left(45)


def circle():
    for i in range(20):
        turtle.forward(10)
        turtle.left(360 / 20)


def triangle_filled():
    turtle.begin_fill()
    triangle()
    turtle.end_fill()


def triangle_filled_rotation():
    while True:
        turtle.begin_fill()
        triangle()
        turtle.end_fill()
        turtle.right(math.degrees(math.pi / 10))
        turtle.clear()
        time.sleep(0.5)


def dessiner_racine_n_ieme(n):
    for i in range(n):
        turtle.forward(100)
        turtle.left(360 / n)


# triangle()
# carre()
# pentagon()
# hexagon()
# octogone()
# circle()
# triangle_filled()
triangle_filled_rotation()
# dessiner_racine_n_ieme(5)
# dessiner_racine_n_ieme(900)
