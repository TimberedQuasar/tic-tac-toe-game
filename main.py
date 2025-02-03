import sys, os, time

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
        #handling game ending in draw
        if(moves_left == 0):
            return "DRAW"
        else:
            return False
    else:
        return False

#printing out who won
def is_game_over(moves_left: int, player_moves: list, which_player: int):
    #checking is game over
    is_game_ended = check_win(moves_left, player_moves)
    if (is_game_ended == True):
        printing_out_board()
        print("Player"+str(which_player)+ " won")
        sys.exit()
    elif(is_game_ended == "DRAW"):
        printing_out_board()
        print("It's a draw")
        sys.exit()
    else:
        return False
    
#handling player movement
def player(player_moves: list, which_player: int, move: int):
        if(which_player==1):
            charackter = "O"
        else:
            charackter = "X"
        #taking input from players
        while True:
            try:
                printing_out_board()
                player = int(input("Player"+ str(which_player) + " - Enter where would you like to put "+charackter+":"))
                if player in possible_moves:
                    break
                else:
                    os.system('cls')
                    print ("You can't make that move")
                    time.sleep(2)

            except ValueError:
                os.system('cls')
                print("Please input valid number for charackter to place")
                time.sleep(2)
        #keep track of player moves
        player_moves.append(player)
        updating_board(player, which_player)
        possible_moves.remove(player)
        move -=1
        is_game_over(move, player_moves, which_player)
        return move, player_moves

#implementing minmax algorithm
def minimax(current_depth: int, moves_left: int, first_player_moves: list, second_player_moves: list):

    #list o movements that can be make
    available_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    available_moves = [x for x in available_moves if x not in first_player_moves and x not in second_player_moves]

    #checking which player has moved
    moves_left += 1
    if(moves_left%2 != 0):
        is_player_maximizing = True
        player_moves = first_player_moves
    else:
        is_player_maximizing = False
        player_moves = second_player_moves
    
    moves_left -= 1
    #checking if someone won -> if true return value of outcome and best current move
    game_over = check_win(moves_left, player_moves)
    if (game_over == True):
        if (is_player_maximizing):
            #!!! THIS MAKE SENS????????
            return 10 - current_depth, player_moves[-1]
        else:
            return current_depth - 10, player_moves[-1]
    elif (game_over == "DRAW"):
        return 0, player_moves[-1]
    else:
        #checking which player will be moving
        if(moves_left%2 != 0):
            is_player_maximizing = True
            player_moves = first_player_moves
        else:
            is_player_maximizing = False
            player_moves = second_player_moves
    #if it's maximaizing player
    #set value to -infinity
    #for each move you can make call out minimax function
    #and sign max value to variable of set numbers
    #return the value

        #set of rules for maximizing player
        if(is_player_maximizing):
            value = [float('-inf'), 0]

            for x in range(moves_left):
                player_moves.append(available_moves[x])
                data = minimax(current_depth+1, moves_left-1, first_player_moves, second_player_moves)
                #if value does not change best move should also stay intact
                #if player has a better outcome best move should stay intact
                if(value[0] < max(value[0], data[0]) ):
                    value[0] = max(value[0], data[0])
                    value[1] = available_moves[x]
                player_moves.pop()
            return value
    
        
    #if it's minimaizing player
    #set value to infinity
    #for each move you can make call out minimax function
    #and sign min value to variable of set numbers
    #return the value

        #set of rules for minimizing player
        else:
            value = [float('inf'), 0]

            for x in range(moves_left):
                player_moves.append(available_moves[x])
                data = minimax(current_depth+1, moves_left-1, first_player_moves, second_player_moves)
                if(value[0] > min(value[0], data[0])):
                    value[0] = min(value[0], data[0])
                    value[1] = available_moves[x]
                player_moves.pop()
            return value
    

def game():
    #creating a board
    global st_row, nd_row, rd_row, board, possible_moves
    st_row = [1,2,3]
    nd_row = [4,5,6]
    rd_row = [7,8,9]
    board =[st_row,nd_row,rd_row]

    #keep track of players moves
    st_player_moves = []
    nd_player_moves = []

    #keep track of how many moves left
    m = 9
    possible_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #letting player decide vs who he wants to play
    option = 0
    try:
        option = int(input("Would like to play with other player(1) or computer(2)?"))
    except ValueError:
        while (option != "1" and option != "2"):
            os.system('cls')
            option = input("Please, input valid number.\n- 1 to play vs other player \n- 2 to play vs computer\n:")

    if(int(option)==1):
    #endless loop for a game
        while True:
            m, st_player_moves = player(st_player_moves, 1, m)
            m, nd_player_moves = player(nd_player_moves, 2, m)
    else:
        while True:
            m, st_player_moves = player(st_player_moves, 1, m)
            nd_player_moves.append(minimax(0, m, st_player_moves, nd_player_moves)[1])
            updating_board(nd_player_moves[-1], 2)
            m -=1
            is_game_over(m, nd_player_moves, 2)

game()