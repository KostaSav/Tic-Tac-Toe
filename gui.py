########## Imports ##########
from graphics import *
import config

## Draw the board using graphics.py,
## with its horizontal and vertical lines.
## Return the board so that other methods can draw on it
def draw_board():
    win = GraphWin("Tic Tac Toe", config.SIZE, config.SIZE)
    config.MARGIN = 0.1 * config.SIZE
    hor1 = Line(
        Point(config.MARGIN, (config.SIZE / 3)),
        Point(config.SIZE - config.MARGIN, (config.SIZE / 3)),
    )
    hor2 = Line(
        Point(config.MARGIN, (2 * config.SIZE / 3)),
        Point(config.SIZE - config.MARGIN, (2 * config.SIZE / 3)),
    )
    ver1 = Line(
        Point((config.SIZE / 3), config.MARGIN),
        Point((config.SIZE / 3), config.SIZE - config.MARGIN),
    )
    ver2 = Line(
        Point((2 * config.SIZE / 3), config.MARGIN),
        Point((2 * config.SIZE / 3), config.SIZE - config.MARGIN),
    )
    hor1.draw(win)
    hor2.draw(win)
    ver1.draw(win)
    ver2.draw(win)
    # win.getMouse()  # Pause to view result
    # win.close()  # Close window when done
    return win


## Draw a X or a O in each turn,
## using the board returned from draw_board()
def draw_piece(board, pos, piece):
    if pos == 1:
        center = Point(
            (config.MARGIN + config.SIZE / 3) / 2, (config.MARGIN + config.SIZE / 3) / 2
        )
    elif pos == 2:
        center = Point(config.SIZE / 2, (config.MARGIN + config.SIZE / 3) / 2)
    elif pos == 3:
        center = Point(
            (config.SIZE - config.MARGIN + 2 * config.SIZE / 3) / 2,
            (config.MARGIN + config.SIZE / 3) / 2,
        )
    elif pos == 4:
        center = Point((config.MARGIN + config.SIZE / 3) / 2, config.SIZE / 2)
    elif pos == 5:
        center = Point(config.SIZE / 2, config.SIZE / 2)
    elif pos == 6:
        center = Point(
            (config.SIZE - config.MARGIN + 2 * config.SIZE / 3) / 2, config.SIZE / 2
        )
    elif pos == 7:
        center = Point(
            (config.MARGIN + config.SIZE / 3) / 2,
            (config.SIZE - config.MARGIN + 2 * config.SIZE / 3) / 2,
        )
    elif pos == 8:
        center = Point(
            config.SIZE / 2, (config.SIZE - config.MARGIN + 2 * config.SIZE / 3) / 2
        )
    elif pos == 9:
        center = Point(
            (config.SIZE - config.MARGIN + 2 * config.SIZE / 3) / 2,
            (config.SIZE - config.MARGIN + 2 * config.SIZE / 3) / 2,
        )

    if piece == "O":
        nought = Circle(center, config.MARGIN)
        nought.setOutline("blue")
        nought.setWidth(0.2 * config.MARGIN)
        nought.draw(board)
    elif piece == "X":
        line1 = Line(
            Point(center.getX() - config.MARGIN, center.getY() - config.MARGIN),
            Point(center.getX() + config.MARGIN, center.getY() + config.MARGIN),
        )
        line2 = Line(
            Point(center.getX() + config.MARGIN, center.getY() - config.MARGIN),
            Point(center.getX() - config.MARGIN, center.getY() + config.MARGIN),
        )
        cross = [line1, line2]
        for line in cross:
            line.setOutline("red")
            line.setWidth(0.2 * config.MARGIN)
            line.draw(board)