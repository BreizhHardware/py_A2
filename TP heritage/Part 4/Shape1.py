class Shape1:
    def __init__(self, x, y, lineThickness = 1, lineColor = "black", fillColor = "white"):
        self.x = x
        self.y = y
        self.lineThickness = lineThickness
        self.lineColor = lineColor
        self.fillColor = fillColor

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getLineThickness(self):
        return self.lineThickness

    def setLineThickness(self, lineThickness):
        self.lineThickness = lineThickness

    def getLineColor(self):
        return self.lineColor

    def setLineColor(self, lineColor):
        self.lineColor = lineColor

    def getFillColor(self):
        return self.fillColor

    def setFillColor(self, fillColor):
        self.fillColor = fillColor