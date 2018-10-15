#!/usr/bin/env python
import sys
def load_maze():
    line = sys.stdin.readline()
    maze = []
    if 'MAZE' in line:
        while len(line) > 0:
            line = sys.stdin.readline().strip()
            maze.append(line)
    f = open("maze_map", "w")
    f.write(str(maze))
    f.close()
    return maze



def bfs(maze, start, goal): #start is number and goal is character
    queue = [] # place to hold the point for checking
    before = {} # hold the position of the previous point
    way = [] # give exactly the way from the start point to the goal point
    x = start[0]
    y = start[1]
    check = [[x, y]]
    while maze[x][y] != goal:
        for x2, y2 in ((x - 1, y), (x, y + 1), (x + 1, y), (x,y-1)):
            if maze[x2][y2] != '#' and [x2, y2] not in check:
                before[(x2, y2)] = [x, y]
                queue.append([x2, y2])
                check.append([x2, y2])
        x = queue[0][0]
        y = queue[0][1]
        queue.pop(0)
    t = []
    way.append([x,y])
    while before[(x,y)] != start:
        way.append(before[(x,y)])
        x = before[(x,y)][0]
        y = before[(x,y)][1]
    way.append(before[(x,y)])
    return way #guide to go from start to goal step by step


def move(way):
    f = open("test", "w")
    i = len(way) - 2
    f.write(str(i))
    f.write(str(way) + '\n')
    # while i >= 0:
    x = way[i + 1][0]
    y = way[i + 1][1]
    if way[i][0] - x == 1:
        sys.stdout.write("MOVE DOWN\n\n")
        f.write("MOVE DOWN\n\n")
    elif x - way[i][0] == 1:
        sys.stdout.write("MOVE UP\n\n")
        f.write("MOVE UP\n\n")
    elif way[i][1] - y == 1:
        sys.stdout.write("MOVE RIGHT\n\n")
        f.write("MOVE RIGHT\n\n")
    elif y - way[i][1] == 1:
        sys.stdout.write("MOVE LEFT\n\n")
        f.write("MOVE LEFT\n\n")
        # i -= 1
        # for _ in range(len(way) - 1):
        #     line = sys.stdin.readline()
        # line = sys.stdin.readline()
        # line = sys.stdin.readline()
        # f.write(line)
        # while len(line) > 0:
        #     line = sys.stdin.readline()
        #     f.write(line)
    f.close()

sys.stdin.readline()
sys.stdout.write("I AM IA\n\n")
sys.stdin.readline()
sys.stdin.readline()
sys.stdout.write("OK\n\n")
sys.stdin.readline()
maze = []
maze = load_maze()
start = []
for x in range(len(maze)):
    for y in range(len(maze[x])):
        if maze[x][y] == 'A':
            start = [x, y]

# for i in range(999):
#     load_maze()
#     # way = bfs(maze, start, '!')
#     # if len(way) > 0 and len(way) < 20:
#     #     move(way)
#     # else:
for _ in range(1000):
    way = bfs(maze, start, 'o')
    move (way)
