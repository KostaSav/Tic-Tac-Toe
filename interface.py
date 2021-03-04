########## Imports ##########
from graphics import *

########## Global Variables ##########
size = 1000
margin = 0.1 * size

## Draw the board using graphics.py,
## with its horizontal and vertical lines.
## Return the board so that other methods can draw on it
def draw_board():
    win = GraphWin("Tic Tac Toe", size, size)
    margin = 0.1 * size
    hor1 = Line(
        Point(margin, (size / 3)),
        Point(size - margin, (size / 3)),
    )
    hor2 = Line(
        Point(margin, (2 * size / 3)),
        Point(size - margin, (2 * size / 3)),
    )
    ver1 = Line(
        Point((size / 3), margin),
        Point((size / 3), size - margin),
    )
    ver2 = Line(
        Point((2 * size / 3), margin),
        Point((2 * size / 3), size - margin),
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
def draw_piece(board, pos, turn):
    if pos == 1:
        center = Point((margin + size / 3) / 2, (margin + size / 3) / 2)
    elif pos == 2:
        center = Point(size / 2, (margin + size / 3) / 2)
    elif pos == 3:
        center = Point((size - margin + 2 * size / 3) / 2, (margin + size / 3) / 2)
    elif pos == 4:
        center = Point((margin + size / 3) / 2, size / 2)
    elif pos == 5:
        center = Point(size / 2, size / 2)
    elif pos == 6:
        center = Point((size - margin + 2 * size / 3) / 2, size / 2)
    elif pos == 7:
        center = Point((margin + size / 3) / 2, (size - margin + 2 * size / 3) / 2)
    elif pos == 8:
        center = Point(size / 2, (size - margin + 2 * size / 3) / 2)
    elif pos == 9:
        center = Point(
            (size - margin + 2 * size / 3) / 2, (size - margin + 2 * size / 3) / 2
        )

    if turn == "cpu":
        nought = Circle(center, margin)
        nought.setOutline("blue")
        nought.setWidth(0.2 * margin)
        nought.draw(board)
    else:
        line1 = Line(
            Point(center.getX() - margin, center.getY() - margin),
            Point(center.getX() + margin, center.getY() + margin),
        )
        line2 = Line(
            Point(center.getX() + margin, center.getY() - margin),
            Point(center.getX() - margin, center.getY() + margin),
        )
        cross = [line1, line2]
        for line in cross:
            line.setOutline("red")
            line.setWidth(0.2 * margin)
            line.draw(board)