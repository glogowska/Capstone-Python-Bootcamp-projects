from turtle import Turtle


class Animal(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)

    def starting_position(self):
        self.goto(0, -280)
