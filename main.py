from logo import logo

game_on=True
turns=0
moves=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
taken=[]

print(logo)

#Function that lays the X&O grid
def lay_grid():
    grid = []
    counter = 0
    for n in moves:
        counter +=1
        grid.append(n)
        if counter<9:
            if counter%3==0:
                grid.append('\n------\n')
            else:
                grid.append('|')
    print(''.join(grid))

while game_on:
    #Defines the player and his sign
    if turns%2==0:
        player = 1
        sign = 'X'
    else:
        player = 2
        sign = 'O'
    print(f"Player {player} move:")
    column = input("Choose column: ")
    row = input("Choose row: ")
    place = int(column) + (int(row) - 1) * 3 - 1
    #Makes chosing same spot impossible
    while place in taken:
        print("Spot already taken, choose another spot:")
        column=input("Choose column: ")
        row=input("Choose row: ")
        place=int(column)+(int(row)-1)*3 - 1
    taken.append(place)
    moves[place] = sign
    lay_grid()
    turns += 1
    #Checks every win condition at end of player turn to see if he won
    if moves[0]==moves[1]==moves[2]==sign or moves[3]==moves[4]==moves[5]==sign or moves[6]==moves[7]==moves[8]==sign or \
            moves[0]==moves[3]==moves[6]==sign or moves[1]==moves[4]==moves[7]==sign or moves[2]==moves[5]==moves[8]==sign or \
            moves[0]==moves[4]==moves[8]==sign or moves[2]==moves[4]==moves[6]==sign:
        print(f"Player {player} wins")
        break
    #Makes sure the game ends in a tie after the grid is full
    if turns==9:
        print("IT's a draw")
        game_on = False