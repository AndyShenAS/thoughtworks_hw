# @Author: shenmaoyuan
# @Date:   2018-07-30T05:33:33+09:00
# @Email:  disovery.yuan@gmail.com
# @Last modified by:   shenmaoyuan
# @Last modified time: 2018-07-30T15:02:08+09:00
# @License: Licensed under the Apache License, Version 2.0 (the "License")
# @Copyright: Copyright (c) 2017 XXXXXX, Inc.

import maze

def check_num_range(size, conn):
    """Check if Number out of range​.
    """
    for num in size:
        if num < 0:
            return True
    for con in conn:
        for i in range(2):
            for j in range(2):
                if con[i][j] < 0 or con[i][j] > size[j] - 1:
                    return True
    return False

def check_command_format(command):
    """Check command format
    """
    if len(command[0].split(' ')) != 2:
        return True
    for twocell in command[1].split(';'):
        for cell in twocell.split(' '):
            if len(cell.split(',')) != 2:
                return True
    return False

def create_maze(command):
    """Create the maze from two-line commands
    """
    if check_command_format(command):
        print('Incorrect command format​.​')
        return 'Incorrect command format​.'
    try:
        size = [int(num) for num in command[0].split(' ')]
        conn = [[(int(cell.split(',')[0]), int(cell.split(',')[1])) for cell in twocell.split(' ')] for twocell in command[1].split(';')]
    except Exception as e:
        # print('ValueError:',str(e))
        print('Invalid number format​.')
        return 'Invalid number format​.'
    if check_num_range(size, conn):
        print('Number out of range​.')
        return 'Number out of range​.'
    mz = maze.Maze(size, conn)
    if mz.matrix == 'Maze format error.':
        return mz.matrix
    return mz
    # return str(conn) + '\n'


def render_grid(inputfp = "data/input.txt", outputfp = "data/output.txt"):
    """Create the maze from two-line commands
    """

    try:
        f = open(inputfp, 'r')
        lines = f.readlines()
        f.close()
    except Exception as e:
        print('File Error:',str(e))
    finally:
        f.close()
    lines = [line.strip('\n') for line in lines]
    lines = [line.strip('\r') for line in lines]
    mazeText = ''
    for i in range(len(lines)//3 + 1):
        command = []
        command.append(lines[i*3])
        command.append(lines[i*3 + 1])
        mz = create_maze(command)
        if i < len(lines)//3:
            mazeText += mz.render() + '\n'
        else:
            mazeText += mz.render()
        # mazeText += mz + '\n'
    try:
        f = open(outputfp, 'w')
        f.write(mazeText)
        f.close()
    except Exception as e:
        print('File Error:',str(e))
    finally:
        f.close()



if __name__ == "__main__":
    inputfp = "data/input.txt"
    outputfp = "data/output.txt"
    render_grid(inputfp, outputfp)
