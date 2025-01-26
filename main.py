def game():
    #endless loop for a game
    while 1>0:
        #creating a board
        st_row = [1,2,3]
        nd_row = [4,5,6]
        rd_row = [7,8,9]
        board =[st_row,nd_row,rd_row]

        #printin out a board
        for x in board:
            print (x)
            
        #taking input from players
        player_one = int(input("Player1 - Enter where would you like to put O:"))
        player_two = int(input("Player2 - Enter where would you like to put X:"))
        diff = True
        while diff:
            #create better checking for input from user
            if(player_one!=player_two and 0<player_one<10 and 0<player_two<10):
                diff = False
            else:
                player_two = int(input("Player2 - Enter again where would you like to put X:"))
        break

game()