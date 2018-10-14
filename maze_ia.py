#!/usr/bin/env python
import sys
maze = []
def load_maze():
    line = sys.stdin.readline()
    maze = []
    if 'MAZE' in line:
        while len(line) > 0:
            line = sys.stdin.readline().strip()
            maze.append(list(line))



def bfs(maze, start, goal): #start is number and goal is character
    queue = [] # place to hold the point for checking
    before = {} # hold the position of the previous point
    way = [] # give exactly the way from the start point to the goal point
    x = start[0]
    y = start[1]
    check = [(x, y)]
    while maze[x][y] != goal:
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if maze[x2][y2] != '#' and (x2, y2) not in check:
                before[(x2, y2)] = [x, y]
                queue.append([x2, y2])
                check.append((x2, y2))
        x = queue[0][0]
        y = queue[0][1]
        queue.pop(0)
    way.append([x, y])
    t = []
    while (x, y) != start:
        t = before[(x, y)]
        way.append(t)
        x = t[0]
        y = t[1]
    return way #guide to go from start to goal step by step


def move(way):
    x = way[len(way) - 1][0]
    y = way[len(way) - 1][1]
    for i in reversed(range(len(way)) - 1):
        x = way[i + 1][0]
        y = way[i + 1][1]
        if way[i][0] - x == 1:
            sys.stdout.write("MOVE DOWN\n\n")
        elif way[i][0] == 1:
            sys.stdout.write("MOVE UP\n\n")
        elif way[i][i] - y == 1:
            sys.stdout.write("MOVE RIGHT\n\n")
        else:
            sys.stdout.write("MOVE LEFT\n\nS")


sys.stdout.write("I AM IA\n\n")
sys.stdout.write("OK\n\n")
load_maze()
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
way = bfs(maze, start, 'o')
move(way)
