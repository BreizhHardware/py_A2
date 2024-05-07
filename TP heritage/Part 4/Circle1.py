from Shape1 import Shape1


class Circle1(Shape1):
    def __init__(self, x, y, radius, lineThickness=6, lineColor="red", fillColor="green"):
        Shape1.__init__(self, x, y, lineThickness, lineColor, fillColor)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def draw(self, turtle):
        turtle.width(self.lineThickness)
        turtle.pencolor(self.lineColor)
        turtle.fillcolor(self.fillColor)
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()