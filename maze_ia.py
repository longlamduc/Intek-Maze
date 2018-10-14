#!/usr/bin/env python
import sys
def load_maze():
    maze.clear()
    x = 0
    wall = sys.stdin.readline()
    maze.append(wall)
    line = ""
    while line != wall:
        x += 1
        line = sys.stdin.readline()
        if 'A' in line:
            start = x * 10 + line.index('A')
        maze.append(line)
    return start


def bfs(maze, start, goal): #start is number and goal is character
    queue = [] # place to hold the point for checking
    check = [] # mark if the point is checked
    before = {} # hold the position of the previous point
    way = [] # give exactly the way from the start point to the goal point
    x = start /10
    y = start % 10
    for i in range(len(maze)): #fullfill the check array with 0 means that
        check.append([])# there is no check_ed point
        for j in range(len(maze[i])):
            check[i].append(0)
    check[x][y] = 1
    while maze[x][y] != goal:
        if maze[x - 1][y] != '#' and check[x - 1][y] == 0: #top
            check[x - 1][y] = 1
            before[(x - 1) * 10 + y] = x * 10 + y
            queue.append((x-1) * 10 + y)
        if maze[x][y + 1] != '#' and check[x][y + 1] == 0: #right
            check[x][y + 1] = 1
            before[(x) * 10 + y + 1] = x * 10 + y
            queue.append((x) * 10 + y + 1)
        if maze[x + 1][y] != '#' and check[x + 1][y] == 0: #bottom
            check[x + 1][y] = 1
            before[(x + 1) * 10 + y] = x * 10 + y
            queue.append((x+1) * 10 + y)
        if maze[x][y - 1] != '#' and check[x][y - 1] == 0: #left
            check[x][y - 1] = 1
            before[(x) * 10 + y - 1] = x * 10 + y
            queue.append((x) * 10 + y - 1)
        x = int(queue[0] / 10)
        y = queue[0] % 10
        queue.pop(0)
    way.append(x * 10 + y)
    while (x * 10 + y) != start:
        t = before[x * 10 + y]
        way.append(t)
        x = (int)(t / 10)
        y = t % 10
    return way #guide to go from start to goal step by step


def move(way):
    x = int(way[len(way) - 1] / 10)
    y = way[len(way) - 1] % 10
    for i in reversed(range(len(way))):
        if (int(way[i] / 10)) - x == 1:
            sys.stdout.write("MOVE DOWN\n")
        elif x - int(way[i] / 10) == 1:
            sys.stdout.write("MOVE UP\n")
        elif way[i] % 10 - y == 1:
            sys.stdout.write("MOVE RIGHT\n")
        else:
            sys.stdout.write("MOVE LEFT\n")




sys.stdout.write("I AM IA\n\n")
sys.stdout.write("OK\n\n")
start = load_maze()
maze = []
sys.stdout.write("MOVE LEFT\n\n")
# for i in range(1000):
#     maze = load_maze()
#     way = bfs(maze, start, '!')
#     if len(way) > 0 and len(way) < 20:
#         move(way)
#         start = way[0]
#     else:
#         way = bfs(maze, start, 'o')
#         move(way)
#         start = way[0]
