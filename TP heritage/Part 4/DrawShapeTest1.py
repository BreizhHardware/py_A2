from Circle1 import Circle1
from Rectangle1 import Rectangle1
from turtle import Turtle, Screen


def drawShapes(shapes, turtle):
    for shape in shapes:
        shape.draw(turtle)


turtle = Turtle()
c = Circle1(x=0, y=100, radius=50, lineThickness=3,
            lineColor="red", fillColor="orange")
r = Rectangle1(x=0, y=-100, width=50, height=200,
               lineThickness=5, lineColor="blue", fillColor="cyan")
shapes = [c, r]
drawShapes(shapes, turtle)
screen = Screen()
screen.exitonclick()