# from copy import deepcopy
import os
import time

class GameOfLife:
    glider = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (1, 0))
    lightweight_spaceship = ((-2, 0), (-2, -1), (-2, -2), (-1, 1), (-1, -2), (0, -2), (1, -2), (2, 1))
    figure = (glider, lightweight_spaceship)
    def __init__(self, w = 60, h = 23):
        self.w = w
        self.h = h
        self.map = [[0] * w for i in range(h)]
    def initialize(self, p = 1):
        center = (self.h // 2, self.w // 2)
        l = len(self.figure[p - 1])
        for i in range(len(self.figure[p - 1])):
            self.set_cell(center, self.figure[p - 1][i][0], self.figure[p - 1][i][1])
        '''
        if p == 1:
            for i in range(len(self.glider)):
                self.set_cell(center, self.glider[i][0], self.glider[i][1])
        '''    
    def set_cell(self, center, _y, _x):
        # print(center[0] + _y)
        # print(center[1] + _x)
        self.map[center[0] + _y][center[1] + _x] = 1
    def display(self):
        os.system("cls")
        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j] == 1:
                    print('O ', end='')
                # elif map[i][j] == 0:
                #     print("X")
                else:
                    print('  ', end='')
            print("")
        print("")
        print("=" * 10, " new generation ", "=" * 10)
        time.sleep(1)


    def proceed(self, t = 10):
        # self.display()
        for generation in range(t):
            next_gen = GameOfLife(self.w, self.h)
            for i in range(self.h):
                for j in range(self.w):
                    lifes = 0
                    for m in range(-1, 2):   # 8 direction 
                        for n in range(-1, 2):
                            move_x = j + n
                            move_y = i + m
                            if self.w > (move_x) >= 0 and self.h > (move_y) >= 0 and (n or m):
                                lifes += self.map[move_y][move_x]   #  if the cell is alive, its value is 1
                    if self.map[i][j] == 1:
                        if 0 < lifes < 2:
                            next_gen.map[i][j] = 0
                        elif lifes == 2 or lifes == 3:
                            next_gen.map[i][j] = 1
                        elif lifes >= 3:
                            next_gen.map[i][j] = 0
                    else:
                        if lifes == 3:
                            next_gen.map[i][j] = 1
            self = next_gen
            print(generation + 1)
            next_gen.display()



# new_game = GameOfLife(10, 10)

# new_game.initialize(1)
# new_game.display()

print("")

# new_game.proceed(10)
# new_game.display()
