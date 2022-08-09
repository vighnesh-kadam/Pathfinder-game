from bank import *
from queue import *
from actions import *


def bfs(draw, grid, start, end):
    mq = Queue()
    came_from = {}
    mq.put(start)
    vis = []
    for i in range(len(grid)):
        vis.append([])
        for j in range(len(grid[i])):
            vis[i].append(-1)
    c = 0
    print("size of rows mq", len(vis))
    print("size of cols ", len(vis[0]))
    while not mq.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = mq.get()
        if vis[current.row][current.col] != -1:
            continue
        if current != start:
            current.make_closed()
        vis[current.row][current.col] = 0
        c = c + 1
        print("coords", current.row, current.col)
        print("val of c:", c)
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            # draw()
            return True

        for neighbour in current.neighbors:
            if vis[neighbour.row][neighbour.col] != -1:
                print("revisit")
                continue
            c = c + 1
            came_from[neighbour] = current
            if neighbour == end:
                reconstruct_path(came_from, end, draw)
                end.make_end()
                draw()
                return True
            else:
                if c % 50 == 0:
                    draw()
                mq.put(neighbour)
                neighbour.make_open()
