def game():
    #creating a board
    st_row = [1,2,3]
    nd_row = [4,5,6]
    rd_row = [7,8,9]
    board =[st_row,nd_row,rd_row]
    win = True
    #endless loop for a game
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
        
        charackter = "O"
        #checking where to put O and X
        #!!!CREATE CHECKING IF CHARACKTER IS ALREADY THERE!!!
        for x in [player_one, player_two]:
            if(x<4):
                st_row[x-1] = charackter
            elif(x<7):
                nd_row[x-4] = charackter
            else:
                rd_row[x-7] = charackter
            charackter = "X"

game()