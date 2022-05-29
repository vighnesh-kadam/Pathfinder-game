from bank import *


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[
            current
        ]  # this is a dictionary to help get the spot from which a particular cell has come
        current.make_path()
        draw()  # lambda function


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(
            win, GREY, (0, i * gap), (width, i * gap)
        )  #   HORIZONTAL LINES
        for j in range(rows):
            pygame.draw.line(
                win, GREY, (j * gap, 0), (j * gap, width)
            )  #   VERTICAL LINES


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)  # draws small cubes

    draw_grid(win, rows, width)  # draws grid lines vertival and horizontal
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)
