from random import randint
import time

board = []
ships = []

def create_board(size):
	board = []
	for i in range(size):
		board.append(["O"] * size)
	return board

def print_board(board):
	print "  0 1 2 3 4 5 6 7 8 9"
	i = 0
	for row in board:
		print str(i) + " " + " ".join(row)
		i += 1

def create_ship(board,ships):
	
	exists = True
	while(exists):
		exists = False
		col = randint(0, len(board) - 1) 
		row = randint(0, len(board) - 1)
		ship = {
			"col": col,
			"row": row
		}
		for s in ships:
			if(s["col"] == ship["col"] and s["row"] == ship["row"]):
				exists = True

	ships.append(ship)
	return ships

def hit(board,ships,col,row):
	time.sleep(1)
	for ship in ships:
		if(col == ship['col'] and row == ship['row']):
			return True
	return False


board = create_board(10)
number_of_ships = 10
for a in range(number_of_ships):
	ships = create_ship(board, ships)
lives = 10

print " "

while(lives > 0):
	if(number_of_ships == 0):
		print "Congratulations! You won!!!"
		break
	print_board(board)
	col = int(raw_input("Col: "))
	row = int(raw_input("Row: "))
        if(col > 9 or row > 9):
                print "You're off board miss waky smartiepants"
                continue
	if(board[col][row] == "X"):
		print "You already choose that one"
		continue

	if(hit(board, ships, col, row)):
		print "Congratulations! you hit one ship"
		board[col][row] = "W"
		number_of_ships -= 1
	else: 
		lives -= 1
		board[col][row] = "X"
		print "Better luck next time!"

print_board(board)
if(lives == 0):
	print "Game over"
