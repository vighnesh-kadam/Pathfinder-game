from tkinter import *
from algos.bfs import *
from algos.djikstras import *
from algos.dfs import *
from algos.astar import *

triala = []
choices = ["a star", "djikstras", "bfs", "dfs"]
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))  # inititalize a surface for display
pygame.display.set_caption("A* Path Finding Algorithm")

# THINGS TO DO:
#     SEARCH NAD UNDERSTAND ALL THE PYGAME FUNCTIONS USED IN PROJECT
#     CHANGE CLASS NAMES AND VARIABLE NAMES LIKE SPOT TO CUBE


def main(win, width):
    # ########
    ROWS = 50
    grid = make_grid(ROWS, width)
    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                print(row, col)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    if opt == 0:
                        astar(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    elif opt == 1:
                        djikstras(
                            lambda: draw(win, grid, ROWS, width), grid, start, end
                        )
                    elif opt == 2:
                        bfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    elif opt == 3:
                        dfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)
                    pygame.quit()


root = Tk()
mylabel = Label(root, text="Select the algorithm you want").pack()
r = IntVar()

Radiobutton(root, text="a star", variable=r, value=0).pack()
Radiobutton(root, text="djikstras", variable=r, value=1).pack()
Radiobutton(root, text="bfs", variable=r, value=2).pack()
Radiobutton(root, text="dfs", variable=r, value=3).pack()

root.mainloop()
opt = r.get()
print("user has chosen: ", choices[opt])

main(WIN, WIDTH)
