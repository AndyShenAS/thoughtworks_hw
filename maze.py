# @Author: shenmaoyuan
# @Date:   2018-07-30T04:37:01+09:00
# @Email:  disovery.yuan@gmail.com
# @Last modified by:   shenmaoyuan
# @Last modified time: 2018-08-01T04:23:59+09:00
# @License: Licensed under the Apache License, Version 2.0 (the "License")
# @Copyright: Copyright (c) 2017 XXXXXX, Inc.

class Maze(object):
    """Maze base class.
    """
    def __init__(self, size, conn):
        self.size = size
        self.conn = conn
        self.matrix = self._get_maze_matrix()
        # if self.matrix == 'Maze format error.':
        #     return self.matrix

    def _get_maze_matrix(self):
        matrix = []
        for i in range(self.size[0]):
            matrix.append([0]*(2*self.size[1] + 1))
            row = []
            for j in range(self.size[1]):
                row.append(0)
                row.append(1)
            row.append(0)
            matrix.append(row)
        matrix.append([0]*(2*self.size[1] + 1))
        # print(matrix)
        for con in self.conn:
            vec = (con[1][0]-con[0][0], con[1][1]-con[0][1])
            if abs(vec[0]) + abs(vec[1]) != 1:
                print('  Maze format error.')
                return 'Maze format error.'
            """Check if the connection of maze is correct​.
            """
            coordinate = (2*con[0][0] + 1 + vec[0], 2*con[0][1] + 1 + vec[1])
            # print('vec',vec)
            # print('coordinate',coordinate)
            matrix[coordinate[0]][coordinate[1]] = 1
        return matrix

    def render(self):
        """Render the grid
        """
        mazeText = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j]:
                    mazeText += '[R] '
                else:
                    mazeText += '[W] '
            mazeText += '\n'
        return mazeText
