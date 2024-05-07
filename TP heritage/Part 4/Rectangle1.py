from Shape1 import Shape1


class Rectangle1(Shape1):
    def __init__(self, x, y, width, height, lineThickness=2, lineColor="blue", fillColor="yellow"):
        Shape1.__init__(self, x, y, lineThickness, lineColor, fillColor)
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def draw(self, turtle):
        turtle.width(self.lineThickness)
        turtle.pencolor(self.lineColor)
        turtle.fillcolor(self.fillColor)
        turtle.penup()
        turtle.goto(self.x - self.width // 2, self.y - self.height // 2)
        turtle.begin_fill()
        turtle.pendown()
        turtle.goto(self.x + self.width // 2, self.y - self.height // 2)
        turtle.goto(self.x + self.width // 2, self.y + self.height // 2)
        turtle.goto(self.x - self.width // 2, self.y + self.height // 2)
        turtle.goto(self.x - self.width // 2, self.y - self.height // 2)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()