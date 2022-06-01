import os
import numpy as np
from numpy import asarray
from numpy import savetxt
#import calculation_cords_array_3d
from pieces_con import *
from itertools import chain
#import pandas as pd
#import xarray as xa
#extension settings for python vscode on cse computers: C:\Users\330687\AppData\Local\Microsoft\WindowsApps\python3.10.exe or python.exe
class Board():
    #def __init__(self, print, move_x, move_y, move_z):
    def __init__(self):
        self = self
        # self.move_x = move_x
        # self.move_y = move_y
        # self.move_z = move_z
        #self.board_total = self.board_total_init
        #self.take_input()
        #self.array_display_init()
    def array_display_init(self):
        self.boardj = [
        ["5","♜","♞","♚","♞","♜"],
        ["4","♟","♟","♟","♟","♟"],
        ["3"," "," "," "," "," "],
        ["2"," "," "," "," "," "],
        ["1"," "," "," "," "," "],
        ["0","A","B","C","D","E"],
        ]
      #debug board
        # self.boardj = [
        # ["5","♜","♖","♚","♞","♜"],
        # ["4","♟","♟","♟","♟","♟"],
        # ["3"," "," "," "," "," "],
        # ["2"," "," "," "," "," "],
        # ["1"," "," "," "," "," "],
        # ["0","A","B","C","D","E"],
        # ]
      #debug board
        self.boardi = [
        ["5","♞","♝","♛","♞","♝"],
        ["4","♟","♟","♟","♟","♟"],
        ["3"," "," "," "," "," "],
        ["2"," "," "," "," "," "],
        ["1"," "," "," "," "," "],
        ["0","A","B","C","D","E"],
        ]
        self.boardh = [
        ["5"," "," "," "," "," "],
        ["4"," "," "," "," "," "],
        ["3"," "," "," "," "," "],
        ["2"," "," "," "," "," "],
        ["1"," "," "," "," "," "],
        ["0","A","B","C","D","E"],
        ]
        self.boardg = [
        ["5"," "," "," "," "," "],
        ["4"," "," "," "," "," "],
        ["3"," "," "," "," "," "],
        ["2","♙","♙","♙","♙","♙"],
        ["1","♗","♘","♕","♗","♘"],
        ["0","A","B","C","D","E"],
        ]
        # self.boardf = [
        # ["5"," "," "," "," "," "],
        # ["4"," "," "," "," "," "],
        # ["3"," "," "," "," "," "],
        # ["2","♙","♙","♙","♙","♙"],
        # ["1","♖","♘","♔","♘","♖"],
        # ["0","A","B","C","D","E"],
        # ]

        self.boardf = [
        ["5"," "," "," "," "," "],
        ["4"," "," "," "," "," "],
        ["3"," "," "," "," "," "],
        ["2","♙","♙","♙","♙","♙"],
        ["1","♖","♜","♔","♘","♖"],
        ["0","A","B","C","D","E"],
        ]
        self.board_total_init = [self.boardf, self.boardg, self.boardh, self.boardi, self.boardj]
        #return self.boardA, self.boardB, self.boardC, self.boardD, self.boardE
    def print_basic(self):
        #board_total=[self.boardf, self.boardg, self.boardh, self.boardi, self.boardj]
        board_name = ["f", "g", "h", "i", "j"]
        i=0
        for boards in self.board_total_current:
            for row in boards:
                print(row)
            print(board_name[i])
            i = i + 1
            #print(boards.__name__)
            #print(boards.__ne__)
    def reset_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_basic()
        print("""


                Gameplay:
                mv - move a piece, parameters: FROM(z,x,y) TO(z,x,y) 
                r - restart the game, parameters:(singleplayer)or(multiplayer)
                q - quit the game

                version 0.0.1 dev
                lots of little bug in the code
                """)
        
        #self.take_input()
    def save_board(self, input2):
        temp_arry = np.array(self.board_total_current)
        #self.reset_screen()
        #input2 = input("Enter filename:")
        stacked = pd.Panel(temp_arry.swapaxes(1,2)).to_frame().stack().reset_index()
        stacked.columns = ['x', 'y', 'z', 'value']
        # save to disk
        stacked.to_csv('stacked.csv', index=False)
        #np.savetxt(input2+".csv", arr_reshaped, fmt = '%s', encoding="utf-8")
        self.reset_screen()
    def load_board(self, input2):
        self.reset_screen()
        #input2 = input("Enter filename:")

        loaded_arr = np.loadtxt(input2+".csv", encoding="utf-8")
        self.board_total_current = np.reshape(
        loaded_arr.shape[0], loaded_arr.shape[1] // self.board_total.shape[2], self.board_total.shape[2]).tolist()
        self.reset_screen()
        
    def take_input(self):
        input1 = input(":")
        if (input1 == "h") or (input1 == "help") or (input1 == "?"):
            print("""
            Commands:
            h - displays this help menu
            l - loads the board, parameters:(filename)
            p - start/resume the game, parameters:(singleplayer)or(multiplayer)
            q - quit the game
            o - options menu
            """) 
        if input1 == "p":
            self.multiplayer()
    def cords_convert(self, cordsorg):
        for i in range(len(cordsorg)):
            if cordsorg[i] == "A":
                cordsorg[i] = 1
            elif cordsorg[i] == "B":
                cordsorg[i] = 2
            elif cordsorg[i] == "C":
                cordsorg[i] = 3
            elif cordsorg[i] == "D":
                cordsorg[i] = 4
            elif cordsorg[i] == "E":
                cordsorg[i] = 5
#--------------------------------------------------------------
            elif cordsorg[i] == "5":
                cordsorg[i] = 0
            elif cordsorg[i] == "4":
                cordsorg[i] = 1
            elif cordsorg[i] == "3":
                cordsorg[i] = 2
            elif cordsorg[i] == "2":
                cordsorg[i] = 3
            elif cordsorg[i] == "1":
                cordsorg[i] = 4
#-------------------------------------------------------------------------
            elif cordsorg[i] == "f":
                cordsorg[i] = 0
            elif cordsorg[i] == "g":
                cordsorg[i] = 1
            elif cordsorg[i] == "h":
                cordsorg[i] = 2
            elif cordsorg[i] == "i":
                cordsorg[i] = 3
            elif cordsorg[i] == "j":
                cordsorg[i] = 4
        return cordsorg
        pass
    def check_pieces(self, cordsorg, cordsto, player):
        if self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♟":
            i=move().pawn_white_can_move(cordsorg[0], cordsorg[2], cordsorg[1], cordsto[0], cordsto[2], cordsto[1])
            return i     
        elif self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♙" and player == "black":
            i=move().pawn_black_can_move(cordsorg[0], cordsorg[2], cordsorg[1], cordsto[0], cordsto[2], cordsto[1])
            return i
        elif self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♞" or (self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♘" and player == "black"):
            i=move().knight_can_move(cordsorg[0], cordsorg[2], cordsorg[1], cordsto[0], cordsto[2], cordsto[1])
            return i
        elif self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♝" or (self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♗" and player == "black"):
            i=move().bishop_can_move(cordsorg[0], cordsorg[2], cordsorg[1], cordsto[0], cordsto[2], cordsto[1])
            return i
        elif self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♜" or (self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♖" and player == "black"):
            i=move().rook_can_move(cordsorg[0], cordsorg[2], cordsorg[1], cordsto[0], cordsto[2], cordsto[1])
            return i
        elif self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♛" or (self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♕" and player == "black"):
            i=move().queen_can_move(cordsorg[0], cordsorg[2], cordsorg[1], cordsto[0], cordsto[2], cordsto[1])
            return i
        elif self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♚" or (self.board_total_current[cordsorg[0]][cordsorg[2]][cordsorg[1]] == "♔" and player == "black"):
            i=move().king_can_move(cordsorg[0], cordsorg[2], cordsorg[1], cordsto[0], cordsto[2], cordsto[1])
            return i
        else:
            return False
    def array_search(self, piece):
        for i in range(self.board_total.shape[0]):
            for j in range(self.board_total.shape[1]):
                for k in range(self.board_total.shape[2]):
                    if self.board_total[i][j][k] == piece:
                        return [i, j, k]
  
    def wincodition_broken(self):
        if '♚' in chain(*self.board_total_current) == False:
            print("Black wins")
            self.status = "Black wins"
            self.reset_screen()
            return True
        elif '♔' in chain(*self.board_total_current) == False:
            print("White wins")
            self.status = "White wins"
            self.reset_screen()
            return True
        else:
          self.status = "hmmm"

    def wincodition(self):
      list = []
      for i in self.board_total_current:
          for j in i:
            for k in j:
              if k == "♔":
                list.append("yes,white")
              elif k == "♚":
                list.append("yes,black")
              else:
                list.append("no")
      if "yes,white" in list and ("yes,black" in list) != True:
            print("White wins")
            self.status = "White wins"
            self.reset_screen()
            return True
      elif "yes,black" in list and ("yes,white" in list) != True:
            print("Black wins")
            self.status = "Black wins"
            self.reset_screen()
            return True
      else:
        return False
    def multiplayer(self):
        self.array_display_init()
        self.board_total_current = self.board_total_init
        player = "white"
        status = ""
        while True:
            self.reset_screen()
            input1 = input(player+"("+status+")"":")
            if (input1 == "h") or (input1 == "help") or (input1 == "?"):
                print("""
                Gameplay:
                mv - move a piece, parameters: FROM(z,x,y) TO(z,x,y) 
                r - restart the game, parameters:(singleplayer)or(multiplayer)
                q - quit the game

                version 0.0.1 dev
                """)
            #elif input1.find('mv'):
            elif 'mv' in input1:
                cords = input1.split(" ")
                cordsorg = cords[1].split(",")
                cordsto = cords[2].split(",")
                cordsorgcon = self.cords_convert(cordsorg)
                cordstocon = self.cords_convert(cordsto)
                print(self.board_total_current[cordsorgcon[0]][cordsorgcon[2]][cordsorgcon[1]])
                x = self.check_pieces(cordsorgcon, cordstocon, player)
                if x == True:
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♟": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♟"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♞": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♞"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♝": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♝"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♛": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♛"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♚": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♚"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♜": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♜"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♖": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♖"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♕": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♕"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♙": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♙"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♘": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♘"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♔": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♔"
                    # if self.board_total_current[cordsorgcon[0]][cordsorgcon[1]][cordsorgcon[2]] == "♗": self.board_total_current[cordstocon[0]][cordstocon[1]][cordstocon[2]] = "♗"
                    self.board_total_current[cordstocon[0]][cordstocon[2]][cordstocon[1]]=self.board_total_current[cordsorgcon[0]][cordsorgcon[2]][cordsorgcon[1]]
                    self.board_total_current[cordsorgcon[0]][cordsorgcon[2]][cordsorgcon[1]]=" "
                    if player == "white":
                        player = "black"
                    else:
                        player = "white"
                    status = "valid last move"
                else:
                    
                    print("Invalid move")
                    status = "invalid last move"
                    self.reset_screen()
            param = input1.split(" ")
            if 'r' in param[0]:
                if 'singleplayer' in input1:
                    print("not yet done")
                    self.reset_screen()
                if 'multiplayer' in input1:
                    self.array_display_init()
                    self.board_total_current = self.board_total_init
                    player = "white"
                    status = "new game"
                    self.reset_screen()
                else:
                    status = "please specify singleplayer or multiplayer"
            #gewonne = self.wincodition()
            if self.wincodition() == True:
                self.array_display_init()
                self.board_total_current = self.board_total_init
                player = "white"
                #status = "new game"
                status = self.status +", new game"
                self.reset_screen()
            if 'q' in param[0]:
                break
            # if 's' in param[0]:
            #     filename = input1.split(" ")
            #     filename = filename[1]
            #     self.save_board(filename)
            #     status = "saved"
            # if 'l' in param[0]:
            #     filename = input1.split(" ")
            #     filename = filename[1]
            #     self.load_board(filename)
            #     status = "loaded"
        
        pass
i=Board()
i.multiplayer()