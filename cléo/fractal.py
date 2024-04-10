import turtle

def KochCurve(turtle, l, n):
    if n == 0:
        turtle.forward(l)  # Move forward by l units
    else:
        l /= n  # Reduce the length of the segment by n
        KochCurve(turtle, l, n-1)
        turtle.left(60)
        KochCurve(turtle, l, n-1)
        turtle.right(120)
        KochCurve(turtle, l, n-1)
        turtle.left(60)
        KochCurve(turtle, l, n-1)


turtle.setup(800, 400)
KochCurve(turtle, 300, 2)
turtle.exitonclick()