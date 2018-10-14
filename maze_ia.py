#!/usr/bin/env python
import sys
def load_maze():
    maze = []
    wall = sys.stdin.readline()
    maze.append(wall)
    line = ""
    while line != wall:
        line = sys.stdin.readline()
        maze.append(line)
    return maze


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
            print("MOVE DOWN\n\n")
        elif x - int(way[i] / 10) == 1:
            print("MOVE UP\n\n")
        elif way[i] % 10 - y == 1:
            print("MOVE RIGHT\n\n")
        else:
            print("MOVE LEFT\n\n")




print("I AM IA\n\n")
print("OK\n\n")
maze = load_maze()
for i in maze:
    for j in maze[i]:
        if maze[i][j] != '#' and maze[i][j] != ' ':
            if maze[i][j] != 'o' and maze[i][j] != '!':
                start = i * 10 + j
while True:
    maze = load_maze()
    way = bfs(maze, start, '!')
    if len(way) > 0 and len(way) < 20:
        move(way)
        start = way[0]
    else:
        way = bfs(maze, start, 'o')
        move(way)
        start = way[0]
