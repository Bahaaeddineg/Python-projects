import curses
import random

# Prompt the user to choose between Easy and Hard game
while True:
    z = input('Choose between Hard and Easy Game: ')
    if z not in ['Easy', 'Hard']:
        print('Please choose the level of the game')
    else:
        # Assign the corresponding time interval based on the chosen level
        if z == 'Easy':
            y = 100
            break
        if z == 'Hard':
            y = 45
            break

# Define a class called Game
class Game():
    def __init__(self):
        global z
        global y

    def Snake(self):
        # Initialize the curses library
        screen = curses.initscr()
        curses.curs_set(0)
        sh, sw = screen.getmaxyx()
        w = curses.newwin(sh, sw, 0, 0)
        w.keypad(1)
        w.timeout(y)

        # Set the initial position of the snake
        snk_x = sw // 4
        snk_y = sh // 2
        snake = [[snk_y, snk_x], [snk_y, snk_x - 1], [snk_y, snk_x - 2]]

        # Set the initial position of the food
        food = [sh // 2, sw // 2]
        w.addch(food[0], food[1], curses.ACS_PI)

        # Set the initial direction of the snake
        key = curses.KEY_RIGHT

        while True:
            next_key = w.getch()
            key = key if next_key == -1 else next_key

            # Check if the snake hits the boundary of the screen
            if snake[0][0] in [0, sh] or snake[0][1] in [0, sw]:
                curses.endwin()
                quit()

            # Check if the snake collides with itself
            if snake[0] in snake[1:]:
                if z == 'Easy':
                    pass
                else:
                    break

            next_position = [snake[0][0], snake[0][1]]

            # Update the position of the snake based on the key input
            if key == curses.KEY_UP:
                next_position[0] -= 1
            if key == curses.KEY_DOWN:
                next_position[0] += 1
            if key == curses.KEY_RIGHT:
                next_position[1] += 1
            if key == curses.KEY_LEFT:
                next_position[1] -= 1

            snake.insert(0, next_position)

            # Check if the snake eats the food
            if snake[0] == food:
                food = None

                # Generate a new random position for the food
                while food is None:
                    nf = [random.randint(1, sh - 1), random.randint(1, sw - 1)]

                    if nf not in snake:
                        food = nf
                    else:
                        None

                food = [random.randint(1, sh - 1), random.randint(1, sw - 1)]

                x = 0
                while x < 100:
                    w.addch(food[0], food[1], curses.ACS_PI)
                    x += 2
            else:
                # Remove the tail of the snake
                tail = snake.pop()
                w.addch(tail[0], tail[1], ' ')

            # Draw the snake on the screen
            w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

        print('Game over')

# Create an instance of the Game class
x = Game()

# Start the snake game
x.Snake()

print('Game over')
