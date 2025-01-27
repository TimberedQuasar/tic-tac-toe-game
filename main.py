import sys, os
def game():
    #creating a board
    st_row = [1,2,3]
    nd_row = [4,5,6]
    rd_row = [7,8,9]
    board =[st_row,nd_row,rd_row]

    #keep track of players moves
    st_player_moves = []
    nd_player_moves = []

    #keep track of rounds
    r = 0

    #condition to win a game
    cond =  ([1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7])

    #endless loop for a game
    win = True
    while win:
        #printing out a board
        for x in board:
            print (x)

        #taking input from players
        player_one = int(input("Player1 - Enter where would you like to put O:"))
        player_two = int(input("Player2 - Enter where would you like to put X:"))

        diff = True
        while diff:
            #!!!CREATE BETTER CHECKING FOR INPUT FROM USER!!!
            if(player_one!=player_two and 0<player_one<10 and 0<player_two<10):
                diff = False
            else:
                player_two = int(input("Player2 - Enter again where would you like to put X:"))
        
        st_player_moves.append(player_one)
        nd_player_moves.append(player_two)

        #checking where to put O and X
        #!!!CREATE CHECKING IF CHARACKTER IS ALREADY THERE!!!
        charackter = "O"
        for x in [player_one, player_two]:
            if(x<4):
                st_row[x-1] = charackter
            elif(x<7):
                nd_row[x-4] = charackter
            else:
                rd_row[x-7] = charackter
            charackter = "X"
        
        #clearing terminal for better visual
        os.system('cls')
        #checking if someone won
        r+=1
        if (r>=3):
            st_player_moves.sort()
            nd_player_moves.sort()
            i=0
            for x in [st_player_moves, nd_player_moves]:
                i+=1
                for y in cond:
                    if x == y:
                        print("Player"+str(i)+ " won")
                        sys.exit()
            
            print("It's a draw")
            sys.exit()

def computer():
    #implementing minmax algorithm
    is_game_won = False
    #value = 0
    is_player_maximizing = True
    moves_left = 8
    #!!!MAKE FUNCTION TAKE ARGUMENTS
    #!!!FIGURE OUT HOW TO CHECK IF GAME HAS ENDED
    #!!!KEEP TRACK OF HOW MANY MOVES HAS LEFT
    def minimax():
        #if the game has ended
        #return the value of outcome
        if (is_game_won):
            return value

        #if it's maximaizing player
        #set value to -infinity
        #for each move you can make call out minimax function
        #and sign max value to variable of set numbers
        #return the value
        if(is_player_maximizing):
            value = float('-inf')
            for x in range(moves_left):
                value = max(value, minimax())
            return value
        
        #if it's minimaizing player
        #set value to infinity
        #for each move you can make call out minimax function
        #and sign min value to variable of set numbers
        #return the value
        else:
            value = float('inf')
            for x in range(moves_left):
                value = min(value, minimax())
            return value



game()