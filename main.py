import sys, os

#printing out a board
def printing_out_board():
    #clearing terminal for better visual
    os.system('cls')
    for x in board:
        print (x)

#updating board
def updating_board(where_to_put_mark: int, which_player_move: int):
        #define which player has moved
        if(which_player_move == 1):
            charackter = "O"
        else: 
            charackter = "X"

        #defing where to put charackter on the board
        if(where_to_put_mark < 4):
            st_row[where_to_put_mark - 1] = charackter
        elif(where_to_put_mark < 7):
            nd_row[where_to_put_mark - 4] = charackter
        else:
            rd_row[where_to_put_mark - 7] = charackter

#function checking if game has ended
#return true if game has ended
def check_win(moves_left: int, player_moves: list):
    #conditions to win a game
    cond =  ([1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7])

    if (moves_left<=4):
        for x in cond:
            #verifying is player list of moves has numbers from conditions
            if(all(number in player_moves for number in x)):
                return True
        return False
    #handling game ending in draw
    elif(moves_left==0):     
        return True
    else:
        return False

#printing out who won
def is_game_over(moves_left: int, player_moves: list, which_player: int):
    #checking is game over
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
        return None
    
#handling player movement
def player(player_moves: list, which_player: int, move: int):
        printing_out_board()
        if(which_player==1):
            charackter = "O"
        else:
            charackter = "X"
        #taking input from players
        player = int(input("Player"+ str(which_player) + " - Enter where would you like to put "+charackter+":"))
        #!!!TO DO checking input from the player
        #keep track of player moves
        player_moves.append(player)
        updating_board(player, which_player)
        is_game_over(move, player_moves, which_player)
        return move-1, player_moves

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

        #letting player decide vs who he wants to play
        option = int(input("Would like to play with other player(1) or computer(2)?"))

        if(option == 1):
            m, st_player_moves = player(st_player_moves, 1, m)
            m, nd_player_moves = player(nd_player_moves, 2, m)
        else:
            m, st_player_moves = player(st_player_moves, 1, m)
            #m, nd_player_moves = minimax(m, st_player_moves, nd_player_moves)

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

#implementing minmax algorithm
def minimax(moves_left: int, first_player_moves: list, second_player_moves: list):
    #if the game has ended return the value of outcome and the best current move

    #list o movemnts you can make
    available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    available_moves = [x for x in available_moves if x not in first_player_moves and x not in second_player_moves]

    #checking which player whill be moving
    if(moves_left%2 != 0):
        is_player_maximizing = True
        player_moves = first_player_moves
    else:
        is_player_maximizing = False
        player_moves = second_player_moves
    
    game_over = check_win(moves_left, player_moves)

    if (game_over and moves_left > 0 ):
        if (is_player_maximizing):
            return 1, player_moves[-1]
        else:
            return -1, player_moves[-1]
    elif (game_over and moves_left == 0):
        return 0, player_moves[-1]
    else:
    
    #if it's maximaizing player
    #set value to -infinity
    #for each move you can make call out minimax function
    #and sign max value to variable of set numbers
    #return the value
        value = float('-inf')
        best_move = None
        if(is_player_maximizing):
            
            for x in range(moves_left):
                player_moves.append(available_moves[x])
                data = minimax(moves_left-1, first_player_moves, second_player_moves)
                value = max(value, data[0])
                best_move = data[1]
                player_moves.pop()
            return value, best_move
    
        
    #if it's minimaizing player
    #set value to infinity
    #for each move you can make call out minimax function
    #and sign min value to variable of set numbers
    #return the value
        else:
            value = float('inf')
            best_move = None
            for x in range(moves_left):
                player_moves.append(available_moves[x])
                data = minimax(moves_left-1, first_player_moves, second_player_moves)
                value = min(value, data[0])
                best_move = data[1]
                player_moves.pop()
            return value, best_move