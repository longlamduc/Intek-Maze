#!/usr/bin/env python
import sys
from time import sleep


def load_maze():
    line = sys.stdin.readline().strip()
    maze = []
    while len(line) > 0:
        maze.append(line)
        line = sys.stdin.readline().strip()
    return maze


def find_enemy(maze, name):
    enemy = []
    for x in maze:
        for y in x:
            if y not in ['o', '!', ' ', '#', name]:
                enemy.append(y)
    return enemy


def bfs(maze, start, enemy):
    enemy.append('#')
    queue = [[start]]
    check = set()
    while queue:
        way = queue.pop(0)
        x, y = way[-1]
        if maze[x][y] == '!' and len(way) <= 20 or maze[x][y] == 'o':
            return way
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if maze[x2][y2] not in enemy and (x2, y2) not in check:
                queue.append(way + [(x2, y2)])
                check.add((x2, y2))


def move(way):
    if way[1][0] - way[0][0] == 1:
        print("MOVE DOWN\n")
    elif way[0][0] - way[1][0] == 1:
        print("MOVE UP\n")
    elif way[1][1] - way[0][1] == 1:
        print("MOVE RIGHT\n")
    else:
        print("MOVE LEFT\n")


def main():
    maze = []
    line = sys.stdin.readline()
    while (line != ''):
        if 'HELLO' in line:
            sys.stdout.write("I AM IA\n\n")
        if 'YOU ARE' in line:
            name = line[-2]
            sys.stdout.write("OK\n\n")
        if 'MAZE' in line:
            maze = load_maze()
            enemy = find_enemy(maze, name)
            for x in range(len(maze)):
                for y in range(len(maze[x])):
                    if maze[x][y] == name:
                        start = (x, y)
            way = bfs(maze, start, enemy)
            move(way)
        line = sys.stdin.readline()


main()
