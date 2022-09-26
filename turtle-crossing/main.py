import random
from turtle import Screen
import time
from crossingAnimal import Animal
from blocks import Block
from levelBoard import LevelBoard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Animal Crossing")

# setting animation progress to none - from now on, animation controlled by updates in a while loop below
screen.tracer(0)

# Objects creation
animal = Animal()
level_board = LevelBoard()


# Animal movement setup
screen.listen()
screen.onkeypress(fun=animal.up, key="Up")
screen.onkeypress(fun=animal.down, key="Down")

# Starting time of which the program will refresh itself
sleeping_time = 0.28

# Two while loops - outer one for managing levels and inner one for managing the game in a certain level
level_on = True
while level_on:
    # blocks move faster in every next level
    sleeping_time *= 0.9
    # creating a different color palette for different levels
    random_color = random.randint(0, 9)

    # adding block objects to the game
    blocks = []
    for num in range(level_board.levels * 40):
        new_block = Block(random_color)
        blocks.append(new_block)

    game_is_on = True
    while game_is_on:
        time.sleep(sleeping_time)

        # animation update after each round of the moving blocks and the crossing animal
        screen.update()
        # moving pieces and spawning them again on the right -  after the block went out of the screen
        for piece in blocks:
            if piece.xcor() < - 330:
                piece.goto(piece.starting_position_x + 900, piece.starting_position_y)
            piece.move()

        # detecting collision with a block
        for collision in blocks:
            if abs(animal.ycor() - collision.ycor()) <= 10 and abs(animal.xcor() - collision.xcor()) <= 20:
                level_on = False
                level_board.game_over()
                game_is_on = False

        # detecting the  finish line and changing the level to the next one
        if animal.ycor() >= 280:
            level_board.update_level()
            animal.starting_position()
            # removing blocks from the current level
            for blo in blocks:
                blo.hideturtle()
                del blo

            game_is_on = False

screen.exitonclick()
