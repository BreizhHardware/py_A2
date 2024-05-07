from Shape import Shape


class Circle(Shape):
    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def draw(self, turtle):
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()