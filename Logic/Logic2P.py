from Graphic.Position import *
from Graphic.Player import *


class Logic2P:

    def __init__(self):
        # horizontal walls
        self.hwalls = [[False for i in range(9)] for j in range(8)]
        # vertical walls
        self.vwalls = [[False for i in range(8)] for j in range(9)]

    def isHwall(self, r, c):
        if r >= 8 or c < 0 or c > 8 or r < 0:
            return False
        if c == 0:
            return self.hwalls[r][c]
        return self.hwalls[r][c] or self.hwalls[r][c - 1]

    def isVwall(self, r, c):
        # print(r, c)
        if c >= 8 or r < 0 or r > 8 or c < 0:
            return False
        if r == 0:
            return self.vwalls[r][c]
        return self.vwalls[r][c] or self.vwalls[r - 1][c]

    def possibleMoves(self, player1, player2):
        pm = []

        def goUp():
            if player1.pos.row == 0 or self.isHwall(player1.pos.row - 1, player1.pos.col):
                return
            if player2.pos.row == player1.pos.row - 1 and player2.pos.col == player1.pos.col:
                if player1.pos.row == 1 or self.isHwall(player1.pos.row - 2, player1.pos.col):
                    if not(player1.pos.col == 0 or self.isVwall(player1.pos.row - 1, player1.pos.col - 1)):
                        pm.append(Position(player1.pos.row - 1, player1.pos.col - 1))
                    if not(player1.pos.col == 8 or self.isVwall(player1.pos.row - 1, player1.pos.col)):
                        pm.append(Position(player1.pos.row - 1, player1.pos.col + 1))
                else:
                    pm.append(Position(player1.pos.row - 2, player1.pos.col))
            else:
                pm.append(Position(player1.pos.row - 1, player1.pos.col))

        def goDown():
            if player1.pos.row == 8 or self.isHwall(player1.pos.row, player1.pos.col):
                return
            if player2.pos.row == player1.pos.row + 1 and player2.pos.col == player1.pos.col:
                if player1.pos.row == 7 or self.isHwall(player1.pos.row + 1, player1.pos.col):
                    if not(player1.pos.col == 0 or self.isVwall(player1.pos.row + 1, player1.pos.col - 1)):
                        pm.append(Position(player1.pos.row + 1, player1.pos.col - 1))
                    if not(player1.pos.col == 8 or self.isVwall(player1.pos.row + 1, player1.pos.col)):
                        pm.append(Position(player1.pos.row + 1, player1.pos.col + 1))
                else:
                    pm.append(Position(player1.pos.row + 2, player1.pos.col))
            else:
                pm.append(Position(player1.pos.row + 1, player1.pos.col))

        def goLeft():
            if player1.pos.col == 0 or self.isVwall(player1.pos.row, player1.pos.col - 1):
                return
            if player2.pos.row == player1.pos.row and player2.pos.col == player1.pos.col - 1:
                if player1.pos.col == 1 or self.isVwall(player1.pos.row, player1.pos.col - 2):
                    if not(player1.pos.row == 0 or self.isHwall(player1.pos.row - 1, player1.pos.col - 1)):
                        pm.append(Position(player1.pos.row - 1, player1.pos.col - 1))
                    if not(player1.pos.row == 8 or self.isHwall(player1.pos.row, player1.pos.col - 1)):
                        pm.append(Position(player1.pos.row + 1, player1.pos.col - 1))
                else:
                    pm.append(Position(player1.pos.row, player1.pos.col - 2))
            else:
                pm.append(Position(player1.pos.row, player1.pos.col - 1))

        
