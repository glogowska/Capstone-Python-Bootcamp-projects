from turtle import Turtle
from colorBlocks import colors
import random


class Block(Turtle):

    def __init__(self, color_num):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.right(90)
        # Setting the position on the screen to a random one,
        # so the blocks appear at different moments of the game
        self.starting_position_x = random.randint(-300, 3000)
        self.starting_position_y = random.randint(-260, 260)
        self.goto(self.starting_position_x, self.starting_position_y)
        self.setheading(180)
        self.color(random.choice(colors[color_num]))

    def move(self):
        """Moving the block by 10 pixels."""
        self.forward(10)
