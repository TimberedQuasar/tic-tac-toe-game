import sys, os

#printing out a board
def printing_out_board():
    os.system('cls')
    for x in board:
        print (x)

#checking where to put O and X
def updating_board(where_to_put_mark, which_player_move):
        if(which_player_move==1):
            charackter = "O"
        else: 
            charackter = "X"

        if(where_to_put_mark<4):
            st_row[where_to_put_mark-1] = charackter
        elif(where_to_put_mark<7):
            nd_row[where_to_put_mark-4] = charackter
        else:
            rd_row[where_to_put_mark-7] = charackter

#function checking if game has ended
#return true if game has ended and number of player who won
#!!! CREATE BETTER CHECKING IF SOMEONE WON
#!!! WHAT IF LIST WILL HAVE SOMETHING LIKE (1,4,2,3)
def check_win(moves_left, player_moves):
    #condition to win a game
    cond =  ([1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7])

    if (moves_left<=4):
        for x in cond:
            if(all(number in player_moves for number in x)):
                return True
            
    elif(moves_left==0):    
        return True
    else:
        return False

#printing out who won
def is_game_over(moves_left, player_moves, which_player):
    is_game_ended = check_win(moves_left, player_moves)
    if (is_game_ended):
        printing_out_board()
        print("Player"+str(which_player)+ " won")
        sys.exit()
    elif(is_game_ended and moves_left == 0):
        printing_out_board()
        print("It's a draw")
        sys.exit()
    else:
        print('')

def game():
    #creating a board
    global st_row, nd_row, rd_row, board
    st_row = [1,2,3]
    nd_row = [4,5,6]
    rd_row = [7,8,9]
    board =[st_row,nd_row,rd_row]

    #keep track of players moves
    st_player_moves = []
    nd_player_moves = []

    #keep track of how many moves left
    m = 9

    #endless loop for a game
    while True:
        printing_out_board()

        #taking input from players
        player_one = int(input("Player1 - Enter where would you like to put O:"))
        #!!!TO DO checking input from the player
        #keep track of player moves
        st_player_moves.append(player_one)

        updating_board(player_one, 1)
        m-=1
        is_game_over(m, st_player_moves, 1)
        printing_out_board()

        player_two = int(input("Player2 - Enter where would you like to put X:"))
        #!!!TO DO checking input from the player
        nd_player_moves.append(player_two)

        updating_board(player_two, 2)
        m-=1
        is_game_over(m, nd_player_moves, 2)

        #handling input from user
        #!!!CREATE CHECKING IF CHARACKTER IS ALREADY THERE!!!
        #!!!CREATE BETTER CHECKING FOR INPUT FROM USER!!!
        #diff = True
        #while diff:
        #    if(player_one!=player_two and 0<player_one<10 and 0<player_two<10):
        #        diff = False
        #    else:
        #        player_two = int(input("Player2 - Enter again where would you like to put X:"))

game()

#function for a computer player
#def computer():

#implementing minmax algorithm
def minimax(moves_left, first_player_moves, second_player_moves):
    #!!!MAKE FUNCTION TAKE ARGUMENTS
    #!!!KEEP TRACK OF HOW MANY MOVES HAS LEFT
    #if the game has ended
    #return the value of outcome
    game_over, who_won = check_win(moves_left, first_player_moves, second_player_moves)
    if (game_over):
        if (who_won == 1):
            return 1
        elif (who_won == 2):
            return -1
        else:
            return 0
        
    if(moves_left%2!=0):
        is_player_maximizing = True
    else:
        is_player_maximizing = False
    #if it's maximaizing player
    #set value to -infinity
    #for each move you can make call out minimax function
    #and sign max value to variable of set numbers
    #return the value
    if(is_player_maximizing):
        value = float('-inf')
        for x in range(moves_left):
            moves_left -= 1
            value = max(value, minimax(moves_left, first_player_moves, second_player_moves))
        return value
        
    #if it's minimaizing player
    #set value to infinity
    #for each move you can make call out minimax function
    #and sign min value to variable of set numbers
    #return the value
    else:
        value = float('inf')
        for x in range(moves_left):
            moves_left -= 1
            value = min(value, minimax(moves_left, first_player_moves, second_player_moves))
        return value