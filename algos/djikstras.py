from actions import *
from queue import *
import sys


def djikstras(draw, grid, start, end):
    c = 0
    came_from = {}
    dist = []
    vis = []
    print("in djk", c)
    for i in range(len(grid)):
        vis.append([])
        dist.append([])
        for j in range(len(grid[i])):
            vis[i].append(-1)
            dist[i].append(sys.maxsize)
    dist[start.row][start.col] = 0
    # vis[start.row][start.col] = 0;
    pq = PriorityQueue()
    pq.put((dist[start.row][start.col], start))
    # print(pq.get()[1])
    while not pq.empty():
        print("inside 1", c)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = pq.get()[1]
        # cdist=pq.get()[1]
        print("stat", vis[current.row][current.col])
        if vis[current.row][current.col] == -1:
            print("inside 2", c)
            vis[current.row][current.col] = 0

            if current == end:
                print("inside 3", c)
                reconstruct_path(came_from, end, draw)
                end.make_end()
                draw()
                return True
            for n in current.neighbors:
                c = c + 1
                print("inside 3", c)

                if (
                    dist[current.row][current.col] + 1 < dist[n.row][n.col]
                    and vis[n.row][n.col] == -1
                ):
                    came_from[n] = current
                    dist[n.row][n.col] = dist[current.row][current.col] + 1
                    pq.put((dist[n.row][n.col], n))
                    n.make_open()
                    if c % 50 == 0:
                        draw()

                if n == end:
                    reconstruct_path(came_from, end, draw)
                    end.make_end()
                    draw()
                    return True

            if current != start:
                print("inside 4", c)
                current.make_closed()
    print("inside 1", c)
    return False
