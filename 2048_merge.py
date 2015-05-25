"""
First week mini-project for Coursera Principles of Computing

Jari Leppanen 2015

Merge function for 2048 game.
"""

#URL = #user40_s63JVYvick_0.py

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    length = len(line)
    merge_line = [element for element in line if element != 0]
    
    for index in range(0, len(merge_line)-1):
        if merge_line[index] == merge_line[index+1]:
            merge_line[index] *= 2
            merge_line[index+1] = 0
    merge_line = [element for element in merge_line if element != 0]
    while len(merge_line) != length:
        merge_line.append(0)
    
    return merge_line
