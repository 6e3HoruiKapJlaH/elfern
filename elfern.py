import sys
import copy
import random

def create_deck():
    a = [ "♦", "♣", "♥", "♠"]
    b = ["Т", "K", "Д", "В", "10", "9", "8", "7"]
    c = []

    for i in a:
        for j in b:
            c.append([j]+[i])
    random.shuffle(c)
    return c
def check(current, new):
    b = ["Т", "K", "Д", "В", "10", "9", "8", "7"]
    curr_index = b.index(current)
    new_index = b.index(new)
    return (curr_index > new_index)

def calculate_ovners(arr):
    return arr.count('10')+arr.count('В')+arr.count('Д')+arr.count('K')+arr.count('Т')

class Elfern():
    def __init__(self):
        c = create_deck()

        self.player_hand =c[:6]
        c=c[6:]
        self.ai_hand = c[:6]
        c=c[6:]

        self.board = c[:]

        self.player_turn = True

        self.current_board = []
        self.current_suit = ""

        self.player_card = None



    
    def minimax(self, depth, alpha, beta, minimizing_ai, min_turn = 0, max_turn = 0):
        if self.caclulate_is_player_win():
            player , ai = self.caclulate_is_player_win()
            return (ai - player), min_turn, max_turn

        elif (depth==0):
            return (calculate_ovners(self.ai_hand[0])-((int(self.player_card)*2)-1)*calculate_ovners(self.current_board)), min_turn, max_turn



        #AI turn
        if not self.player_turn:
            max_evaluation = -1000
            max_turn = 0


            
            for child in range(len(self.ai_hand)-1):

                temp_class = copy.deepcopy(self)
                temp_class.make_turn(child)

                eval = temp_class.minimax(depth-1, alpha, beta, True, min_turn, max_turn)

                    
                if max_evaluation < eval[0]:
                    max_evaluation = eval[0]
                    max_turn = child

                alpha = max(alpha, eval[0])
                if beta <= alpha:
                    break
            return max_evaluation, min_turn, max_turn
        
        #Player turn
        else:
            min_evaluation = 1000
            min_turn = 0



            for child in range(len(self.player_hand)-1):

                temp_class = copy.deepcopy(self)
                temp_class.make_turn(child)


                eval = temp_class.minimax(depth-1, alpha, beta, False, min_turn, max_turn)

                if min_evaluation > eval[0]:
                    min_evaluation = eval[0]
                    min_turn = child

                beta = min(beta, eval[0])
                if beta <= alpha:
                    break
            return min_evaluation, min_turn, max_turn


    def caclulate_is_player_win(self):
        if len(self.board)>0:
            return False
        else:
            player = calculate_ovners(self.player_hand)
            ai = calculate_ovners(self.ai_hand)
            return player, ai


    def check_is_end_game(self):
        if len(self.current_board) == 16:
            self.player_turn = self.player_turn
            if self.player_card:
                self.player_hand.append(self.current_board)
                self.ai_hand.append(self.board[0])
                self.board.pop(0)
                if len(self.board)>0:
                    self.player_hand.append(self.board[0])
                    self.board.pop(0)
            else:
                self.ai_hand.append(self.current_board)
                self.player_hand.append(self.board[0])
                self.board.pop(0)
                if len(self.board)>0:
                    self.ai_hand.append(self.board[0])
                    self.board.pop(0)

            self.current_board=[]
            self.player_card = None

        elif len(self.ai_hand) == 0 or len(self.player_hand)==0:
            self.player_turn = bool((len(self.current_board))%2)^(self.player_turn)
            if self.player_card:
                self.player_hand.append(self.current_board)
                self.ai_hand.append(self.board[0])
                self.board.pop(0)
                if len(self.board)>0:
    
                    self.player_hand.append(self.board[0])
                    self.board.pop(0)
            else:
                self.ai_hand.append(self.current_board)
                self.player_hand.append(self.board[0])
                self.board.pop(0)
                if len(self.board)>0:
                    self.ai_hand.append(self.board[0])
                    self.board.pop(0)
            self.current_board=[]
            self.player_card = None

        else:
            self.player_turn = not self.player_turn






    def make_turn(self, position):
        if self.player_turn== True:
            
            n = self.player_hand[position]
            self.player_hand.pop(position)
            if len(self.current_board)<=0:
                #self.current_board.append(n)
                self.current_board.append(n)

                self.player_card = True
                k = self.caclulate_is_player_win()
                if not k:


                    self.check_is_end_game()

            else: 
                if self.current_board[0][1] == n[1] and check(self.current_board[0][0], n[0]):
                    self.current_board.insert(0,n)
                    self.player_card = True
                    k = self.caclulate_is_player_win()
                    if not k:
                        self.check_is_end_game()
                else:
                    #self.current_board.append(n)
                    self.current_board.insert(0,n)

                    k = self.caclulate_is_player_win()
                    if not k:
                        self.check_is_end_game()

            
            
        else:
            n = self.ai_hand[position]

            self.ai_hand.pop(position)

            if len(self.current_board)<=0:
                #self.current_board.append([n])
                self.current_board.append(n)

                self.player_card = False
                k = self.caclulate_is_player_win()
                if not k:
                    self.check_is_end_game()
            else:
                print((self.current_board))
                if self.current_board[0][1] == n[1] and check(self.current_board[0][0], n[0]):
                    self.current_board.insert(0,n)
                    self.player_card = False
                    k = self.caclulate_is_player_win()
                    if not k:
                        self.check_is_end_game()
                else:
                    #self.current_board.append(n)
                    self.current_board.insert(0,n)

                    k = self.caclulate_is_player_win()
                    if not k:
                        self.check_is_end_game()

            





