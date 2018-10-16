#!/usr/bin/env python
import sys
def load_maze():
    line = sys.stdin.readline().strip()
    maze = []
    while len(line) > 0:
        maze.append(line)
        line = sys.stdin.readline().strip()
    return maze



def bfs(maze, start, goal): #start is number and goal is character
    queue = [] # place to hold the point for checking
    before = {} # hold the position of the previous point
    way = [] # give exactly the way from the start point to the goal point
    x = start[0]
    y = start[1]
    while maze[x][y] != goal:
        for x2, y2 in ((x - 1, y), (x, y + 1), (x + 1, y), (x,y-1)):
            if maze[x2][y2] != '#' and [x2, y2] not in queue:
                before[(x2, y2)] = [x, y]
                queue.append([x2, y2])
        x = queue[0][0]
        y = queue[0][1]
        queue.pop(0)
    t = []
    way.append([x,y])
    while before[(x,y)] != start:
        way.append(before[(x,y)])
        x = before[(x,y)][0]
        y = before[(x,y)][1]
        if [x, y] == start:
            break
    way.append(before[(x,y)])
    return way #guide to go from start to goal step by step


def move(way):
    i = len(way) - 2
    x = way[i + 1][0]
    y = way[i + 1][1]
    if way[i][0] - x == 1:
        sys.stdout.write("MOVE DOWN\n\n")
    elif x - way[i][0] == 1:
        sys.stdout.write("MOVE UP\n\n")
    elif way[i][1] - y == 1:
        sys.stdout.write("MOVE RIGHT\n\n")
    elif y - way[i][1] == 1:
        sys.stdout.write("MOVE LEFT\n\n")



def main():
    maze = []
    start = []
    way = []
    line = sys.stdin.readline()
    while (line != ''):
        f = open("test1", "a")
        f.write(line)
        f.close()
        if 'HELLO' in line:
            sys.stdout.write("I AM IA\n\n")
            sys.stdin.readline()
        if 'ARE' in line:
            sys.stdout.write("OK\n\n")
            sys.stdin.readline()
        if 'MAZE' in line:
            maze = load_maze()
            f = open("test", "w")
            f.write(str(maze))
            f.close()
            for x in range(len(maze)):
                for y in range(len(maze[x])):
                    if maze[x][y] == 'A':
                        start = [x, y]
                        f = open("test", "a")
                        f.write(str(start))
                        f.close()
                # f = open("test", "a")
                # f.write(str(start))
                # f.close()
    # way = bfs(maze, start, '!')
    # f = open("test", "a")
    # f.write(str(way))
    # f.close()
    # if len(way) > 0 and len(way) < 20:
    #     move(way)
    # else:
            way = bfs(maze, start, 'o')
            f = open("test", "a")
            f.write(str(way))
            f.close()
            move (way)
        line = sys.stdin.readline()
def test():
    line = sys.stdin.readline()
    f = open("test_line", "a")
    f.write(line)
    f.close
    if 'HELLO' in line:
        sys.stdout.write("I AM IA\n\n")
        sys.stdin.readline()
    line = sys.stdin.readline()
    f = open("test_line", "a")
    f.write(line)
    f.close
    if 'ARE' in line:
        sys.stdout.write("OK\n\n")
        sys.stdin.readline()
    line = sys.stdin.readline()
    f = open("test_line", "a")
    f.write(line)
    f.close
main()
