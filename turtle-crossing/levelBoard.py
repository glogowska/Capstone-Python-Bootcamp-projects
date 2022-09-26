from turtle import Turtle


class LevelBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.levels = 0
        self.hideturtle()
        self.goto(-250, 270)
        self.update_level()

    def update_level(self):
        """Updating the status of the 'Level Board' by clearing the last one and increasing the level."""
        self.clear()
        self.levels += 1
        self.write(f"Level {self.levels}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        """Printing a 'GAME OVER' text in the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
