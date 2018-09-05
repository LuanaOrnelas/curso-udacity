import turtle

def draw_square():
    janela = turtle.Screen()
    janela.bgcolor("red")

    lila = turtle.Turtle()
    lila.forward(100)
    lila.right(90)
    lila.forward(100)
    lila.right(90)
    lila.forward(100)
    lila.right(90)
    lila.forward(100)
    lila.right(90)

    janela.exitonclick()


draw_square()