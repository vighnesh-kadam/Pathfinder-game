from actions import *


def dfs(draw, grid, start, end):
    print("inside dfs")
    stackk = []
    came_from = {}
    stackk.append(start)
    vis = []
    for i in range(len(grid)):
        vis.append([])
        for j in range(len(grid[i])):
            vis[i].append(-1)
    c = 0
    while len(stackk) > 0:
        print("inside while ")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = stackk.pop()
        if vis[current.row][current.col] != -1:
            continue
        if current != start:
            current.make_closed()
        vis[current.row][current.col] = 0
        c = c + 1
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
            print(c)
            came_from[neighbour] = current
            if neighbour == end:
                reconstruct_path(came_from, end, draw)
                end.make_end()
                draw()
                return True
            else:
                if c % 50 == 0:
                    draw()
                stackk.append(neighbour)
                neighbour.make_open()
