import cmath
import turtle
import time

turtle.speed('fastest')
def get_racine(radius, number):
    out = []
    com = cmath.sqrt(radius ** 2 - (radius / 2) ** 2)
    for i in range(number):
        com = com * cmath.exp(2j * cmath.pi / number)
        out.append(com)
    return out


def printminicircle(x, y, radius=3):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.filling()
    turtle.fillcolor(0, 0, 0)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw():
    i = 1
    path = get_racine(100, 60)
    while i > -1:
        for point in path:
            printminicircle(point.real, point.imag)
            time.sleep(1)
        turtle.clear()
        i = i + 1

if __name__ == '__main__':
    draw()

