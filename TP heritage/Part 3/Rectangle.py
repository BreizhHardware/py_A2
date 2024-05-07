from Shape import Shape


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        Shape.__init__(self, x, y)
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
        turtle.penup()
        turtle.goto(self.x - self.width // 2, self.y - self.height // 2)
        turtle.pendown()
        turtle.goto(self.x + self.width // 2, self.y - self.height // 2)
        turtle.goto(self.x + self.width // 2, self.y + self.height // 2)
        turtle.goto(self.x - self.width // 2, self.y + self.height // 2)
        turtle.goto(self.x - self.width // 2, self.y - self.height // 2)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()