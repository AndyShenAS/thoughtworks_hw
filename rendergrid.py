# @Author: shenmaoyuan
# @Date:   2018-07-30T05:33:33+09:00
# @Email:  disovery.yuan@gmail.com
# @Last modified by:   shenmaoyuan
# @Last modified time: 2018-07-30T09:42:55+09:00
# @License: Licensed under the Apache License, Version 2.0 (the "License")
# @Copyright: Copyright (c) 2017 XXXXXX, Inc.

import maze

def create_maze(command):
    size = [int(num) for num in command[0].split(' ')]
    conn = [[(int(cell.split(',')[0]), int(cell.split(',')[1])) for cell in twocell.split(' ')] for twocell in command[1].split(';')]
    mz = maze.Maze(size, conn)
    return mz
    # return str(conn) + '\n'


def render_grid(inputfp = "data/input.txt", outputfp = "data/output.txt"):
    f = open(inputfp, 'r')
    lines = f.readlines()
    f.close()
    lines = [line.strip('\n') for line in lines]
    lines = [line.strip('\r') for line in lines]
    mazeText = ''
    for i in range(len(lines)//3 + 1):
        command = []
        command.append(lines[i*3])
        command.append(lines[i*3 + 1])
        mz = create_maze(command)
        mazeText += mz.render() + '\n'
        # mazeText += mz + '\n'
    f = open(outputfp, 'w')
    f.write(mazeText)
    f.close()



if __name__ == "__main__":
    inputfp = "data/input.txt"
    outputfp = "data/output.txt"
    render_grid(inputfp, outputfp)
