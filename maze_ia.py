#!/usr/bin/env python
import sys
maze = []

print("I AM IA\n")
print("OK\n")

print('MOVE UP\n')

def load_maze():
    for i in range(10):
        maze.append(sys.stdin.readline())
    return (''.join(maze))


print(load_maze())
