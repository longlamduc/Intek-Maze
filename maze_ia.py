#!/usr/bin/env python
import sys
maze = []


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





print("I AM IA\n")
print("OK\n")

print('MOVE UP\n')
print(load_maze())
