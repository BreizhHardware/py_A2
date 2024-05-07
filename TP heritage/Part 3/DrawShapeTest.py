from Circle import Circle
from Rectangle import Rectangle
from turtle import Turtle


def drawShapes(shapes, turtle):
    for shape in shapes:
        shape.draw(turtle)


turtle = Turtle()
c = Circle(x=0, y=100, radius=50)
r = Rectangle(x=0, y=-100, width=50, height=200)
shapes = [c, r]
drawShapes(shapes, turtle)
turtle.exitonclick()