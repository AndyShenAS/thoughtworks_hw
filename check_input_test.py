# @Author: shenmaoyuan
# @Date:   2018-07-30T13:11:33+09:00
# @Email:  disovery.yuan@gmail.com
# @Last modified by:   shenmaoyuan
# @Last modified time: 2018-07-30T14:56:43+09:00
# @License: Licensed under the Apache License, Version 2.0 (the "License")
# @Copyright: Copyright (c) 2017 XXXXXX, Inc.

import unittest
import rendergrid as rg

class TestInputCheck(unittest.TestCase):

    def setUp(self):
        print('Test execution begins...')

    def test_number_format(self):
        print('Test Invalid number format.')
        command = ['3 3','0,s 0,2;0,0 1,0;0,1 1,1;0,y 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1']
        # command = ['3 3','0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1']
        self.assertEqual('Invalid number format​.',rg.create_maze(command))

    def test_out_range(self):
        print('Test Number out of range​.')
        command = ['3 3','0,-1 0,2;0,0 1,0;0,1 1,1;0,4 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1']
        # command = ['3 3','0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1']
        self.assertEqual('Number out of range​.',rg.create_maze(command))

    def test_command_format(self):
        print('Test Incorrect command format​.')
        command = ['3 3','0,,,,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1']
        # command = ['3 3','0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1']
        self.assertEqual('Incorrect command format​.',rg.create_maze(command))

    def test_maze_format(self):
        print('Test Maze format error.')
        command = ['3 3','0,1 1,0;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1']
        # command = ['3 3','0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1']
        self.assertEqual('Maze format error.',rg.create_maze(command))

    def tearDown(self):
        print('End of test execution...')
if __name__ =='__main__':
    unittest.main()
