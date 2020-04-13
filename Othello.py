#Othello
import numpy as np
import pdb
import random
import time




SQUARE_WEIGHTS = [
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
    [0, 120, -20,  20,   5,   5,  20, -20, 120,   0],
    [0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0],
    [0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0],
    [0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0],
    [0,   5,  -5,   3,   3,   3,   3,  -5,   5,   0],
    [0,  20,  -5,  15,   3,   3,  15,  -5,  20,   0],
    [0, -20, -40,  -5,  -5,  -5,  -5, -40, -20,   0],
    [0, 120, -20,  20,   5,   5,  20, -20, 120,   0],
    [0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
]

def create_dict():
  thisdict = {
    # Corners
    "00": 16.16,
    "07": 16.16,
    "70": 16.16,
    "77": 16.16,

    # Buffers
    "01": -3.03,
    "10": -4.12,
    "11": -1.81,

    "06": -3.03,
    "17": -4.12,
    "16": -1.81,

    "71": -3.03,
    "60": -4.12,
    "61": -1.81,

    "76": -3.03,
    "67": -4.12,
    "66": -1.81,

    # Edges
    "02": 0.99,
    "03": 0.43,
    "04": 0.43,
    "05": 0.99,

    "72": 0.99,
    "73": 0.43,
    "74": 0.43,
    "75": 0.99,

    "20": 1.33,
    "30": 0.63,
    "40": 0.63,
    "50": 1.33,

    "27": 1.33,
    "37": 0.63,
    "47": 0.63,
    "57": 1.33,

    # Normals
    "12": -0.08,
    "13": -0.27,
    "14": -0.27,
    "15": -0.08,

    "21": -0.04,
    "22": 0.51,
    "23": 0.07,
    "24": 0.07,
    "25": 0.51,
    "26": -0.04,

    "31": -0.18,
    "32": -0.04,
    "33": -0.01,
    "34": -0.01,
    "35": -0.04,
    "36": -0.18,
    
    "41": -0.18,
    "42": -0.04,
    "43": -0.01,
    "44": -0.01,
    "45": -0.04,
    "46": -0.18,
    
    "51": -0.04,
    "52": 0.51,
    "53": 0.07,
    "54": 0.07,
    "55": 0.51,
    "56": -0.04,
    
    "62": -0.08,
    "63": -0.27,
    "64": -0.27,
    "65": -0.08,
  }
  return thisdict





directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
BLACK = -1
WHITE = 1
TOP = 4
weights = create_dict()
def main():
	# play_game_random()
	play_game_with_human()
	
				
		

#TODO____

#Send the original coordinates for the best flip instead of returning the one frpm the last node

#________
#Initial call: min_max(current_position, TOP,-99999,99999, True)

def legal_moves(board, marker):
	moves = []
	for i in range(8):
		for j in range(8):
			available_move = is_valid_move(i,j,marker, board)
			if available_move:
				moves.append(available_move[0])
	return moves






def play_game_with_human():
	player = 2
	human = input("What color do you want to play? Enter WHITE or BLACK \n")
	if human == "BLACK":
		player = 0
	elif human == "WHITE":
		player = 1
	move_time = float(input("How much maximum time should the AI use for each move? Enter nubmber in seconds\n")) - 0.1
	board = newBoard()
	alpha = -99999
	beta = 99999
	depth = TOP
	if player == 0:
		print("The moves are to be entered on the form 'xy' where x is the row and y the column moving from 0 to 7 \n \n")
		while not game_over(board):
			legal_input = False
			if np.count_nonzero(board) > 56:
				depth = 10

			if player:
				start_time = time.time()
				move = first_min_max(start_time, board, depth, alpha, beta, player, move_time)
				
			else:
				print(board)
				print('\n')
				moves = legal_moves(board, -1)
				if len(moves) < 1:
					print("You can't make any moves, opponents turn\n")
					move = "nomove"
				else:
					print("Available moves:\n", moves)

					human_move = input("What move do you want to make? Enter coordinates \n")
					move = is_valid_move(int(human_move[0]),int(human_move[1]), -1, board)
			if move:
				if move != "nomove":
					board = flip(board, move, player)
				move = None
			else:
				print("YOU CAN'T MAKE THAT MOVE, EXITING")
				return
			player = 1 - player
	else:
		print("The moves are to be entered on the form 'xy' where x is the row and y the column moving from 0 to 7 \n \n")
		while not game_over(board):
			if np.count_nonzero(board) > 56:
					depth = 10

			if player:
				print(board)
				print('\n')
				moves = legal_moves(board, 1)
				if len(moves) < 1:
					print("You can't make any moves, opponents turn\n")
					move = "nomove"
				else:
					print("Available moves:\n", moves)
					human_move = input("What move do you want to make? Enter coordinates \n")
					move = is_valid_move(int(human_move[0]),int(human_move[1]), 1, board)
				if move:
					if move != "nomove":
						board = flip(board, move, player)
					move = None
				else:
					print("YOU CAN'T MAKE THAT MOVE, EXITING")
					return
				
				
			else:
				start_time = time.time()
				move = first_min_max(start_time, board, depth, alpha, beta, player, move_time)
			if move:
				board = flip(board, move, player)
			player = 1 - player
	print("Game is over! The winner is: ")
	ones = np.count_nonzero(board == 1)
	zeros = np.count_nonzero(board == -1)
	if ones > zeros:
		print("WHITE, with", ones, " points against", zeros )
	elif zeros > ones:
		print("BLACK, with", zeros, " points against", ones )
	elif ones == zeros:
		"no one. The game ended with equal points"

def tree(player, board):
	move_list = []
	for i in range(8):
		for j in range(8):
			valid_move = is_valid_move(i,j,player, board)
			if valid_move:
				move_list.append(valid_move)
	return move_list




def play_game_random():
	player = 1
	iterations = 20
	
	wins = 0

	for i in range(iterations):
		board = newBoard()
		alpha = -99999
		beta = 999999
		depth = TOP
		print("Round: ", i,"...")
		game_start = time.time()
		while not game_over(board):
			if np.count_nonzero(board) > 56:
				depth = 10

			if player:
				start_time = time.time()
				move = first_min_max(start_time, board, depth, alpha, beta, player)
				
			else:
				move = opponent_random_move(board, player)
			if move:
				board = flip(board, move, player)
			player = 1 - player
		print("Time to play game", i + 1, ": ", time.time() - game_start, "seconds")



		value = np.sum(board)
		print("The winner is: ")
		if value > 0:
			print("WHITE.")
			wins += 1
		elif value < 0:
			print("BLACK.")
		else:
			print("no one")
		print('\n')
		print(board)
	print(wins, "/", iterations)









def first_min_max(start_time, board, depth, alpha, beta, player, nbr_of_moves = 0, move_time = 10):
	board = board.copy()
	chosen_move = None
	if player:
		max_eval = -99999
		move_list = tree(player, board)
		for move in move_list:
			eval_ = min_max(start_time, flip(board,move,player), depth - 1, alpha, beta, False, len(move_list), move_time)

			max_eval = max(max_eval, eval_)
			if(max_eval == eval_):
				chosen_move = move

			alpha = max(alpha,eval_)
			if beta <= alpha:
				break
		return chosen_move
	else:
		min_eval = 99999
		move_list = tree(player, board)
		for move in move_list:
			eval_ = min_max(start_time, flip(board,move,player), depth - 1, alpha, beta, True, len(move_list), move_time)
			min_eval = min(min_eval, eval_)
			if(min_eval == eval_):
				chosen_move = move
			beta = min(beta, eval_)
			if beta <= alpha:
				break
		return chosen_move
	return None

def min_max(start_time, board, depth, alpha, beta, player, nbr_of_moves, move_time = 10):
	
	if time.time() - start_time > move_time:
		return evaluate(board, nbr_of_moves)

	board = board.copy()
	if depth == 0 or game_over(board):
		return evaluate(board, nbr_of_moves)
	if player:
		max_eval = -99999
		move_list = tree(player, board)
		for move in move_list:
			eval_ = min_max(start_time, flip(board,move,player), depth - 1, alpha, beta, False, len(move_list), move_time)
			max_eval = max(max_eval, eval_)
			alpha = max(alpha,eval_)
			if beta <= alpha:
				break
		return max_eval
	else:
		min_eval = 99999
		move_list = tree(player, board)
		for move in move_list:
			eval_ = min_max(start_time, flip(board,move,player), depth - 1, alpha, beta, True, len(move_list), move_time)
			min_eval = min(min_eval, eval_)
			beta = min(beta, eval_)
			if beta <= alpha:
				break
		return min_eval




def game_over(board):
	end_game = False
	for i in range(8):
		for j in range(8):
			if is_valid_move(i, j, 1,board):
				return False
			if is_valid_move(i,j, -1, board):
				return False
	return True





def opponent_random_move(board, player):
	board = board.copy()
	marker_places = []
	values = []
	children = []
	for i in range(8):
		for j in range(8):
			flip_coord = is_valid_move(i,j,player,board)
			if flip_coord:
				marker_places.append(flip_coord)
	if len(marker_places) < 1:
		return None
	return random.choice(marker_places)
	

def flip(board,flip_coord,player):
	board = board.copy()
	if player:
		for i,j in flip_coord:
			board[i,j] = 1
	else:
		for i,j in flip_coord:
			board[i,j] = -1
	return board
	

def evaluate(board, nbr_of_moves):


	if np.count_nonzero(board) < 20:
		return nbr_of_moves
	elif np.count_nonzero(board) < 52:
		sum = 0
		for i in range(8):
			for j in range(8):
				#sum += board[i,j] * SQUARE_WEIGHTS[i][j]
				sum += board[i,j] * weights[str(i) + str(j)]
		return sum
	else:
		return np.sum(board)



def newBoard():
	board = np.zeros((8,8))
	board[3,3] = 1
	board[3,4] = -1
	board[4,3] = -1
	board[4,4] = 1
	return board
	

def is_Onboard(x,y):
	return x >= 0 and x < 8 and y >= 0 and y < 8




def is_valid_move(x,y,marker, board):

	#Returns a list of markers to be flipped or False

	flip_coordinates = []
	if not is_Onboard(x,y) or board[x,y] != 0:
		return False

	if marker == 1:
		enemy = -1
	else:
		enemy = 1
		marker = -1
	start_x = x
	start_y = y

	
	for directionX, directionY in directions:
		foundOpponent = False
		maybe_flip = []
		x = start_x
		y = start_y
		x += directionX
		y += directionY
		if is_Onboard(x,y) and board[x,y] == enemy:
			foundOpponent = True
			maybe_flip.append([x,y])

			x += directionX
			y += directionY
		while(foundOpponent and is_Onboard(x,y)):
			if board[x,y] == 0:
				break
			if board[x,y] == marker:
				for element in maybe_flip:
					flip_coordinates.append(element)
				break;
			maybe_flip.append([x,y])
			x += directionX
			y += directionY
	if len(flip_coordinates) < 1:
		return False
	return [[start_x,start_y]] + flip_coordinates


main()





# def tree_maker(root, player, depth, skip = False):
# 	root.board = root.board.copy()

# 	if depth < 1:
# 		root.value = evaluate(root.board)
# 		return root.value
# 	marker_places = []
# 	values = []
# 	root.children = []
# 	for i in range(8):
# 		for j in range(8):
# 			flip_coord = is_valid_move(i,j,player,root.board)
# 			if flip_coord:
# 				root.children.append(new_Node(flip(root.board, flip_coord, player)))
# 				marker_places.append(flip_coord)
# 				# node1 = new_Node(flip(board, flip_coord, player))
# 				# print(tree_maker(node1, node1.board, - player, depth - 1))
	
# 	if len(marker_places) < 1:
# 		if skip == True:
# 			return root.value
# 		skip = True
# 		root.children.append(new_Node(root.board))

# 	for element in root.children:
# 		values.append(tree_maker(element, - player, depth - 1, skip))

# 	root.value = min_max(values, player)
	

# 	return root.value

# def first_tree_maker(root, player, depth, skip = False):
# 	root.board = root.board.copy()
# 	marker_places = []
# 	values = []
# 	root.children = []
# 	for i in range(8):
# 		for j in range(8):
# 			flip_coord = is_valid_move(i,j,player,root.board)
# 			if flip_coord:
# 				root.children.append(new_Node(flip(root.board, flip_coord, player)))
# 				marker_places.append(flip_coord)

# 	if len(root.children) < 1:
# 		if skip:
# 			return evaluate(root.board), None
# 		skip = True
# 		return evaluate(root.board), 0
	
# 	for element in root.children:
# 		values.append(tree_maker(element, - player, depth - 1))
# 	root.value = min_max(values, player)
	
# 	return root.value, marker_places[values.index(root.value)]







# def play_game():
# 	player = WHITE
# 	wins = 0
# 	iterations = 20
# 	for i in range(iterations):
# 		end_game = False
# 		board = newBoard()
# 		depth = TOP
# 		skip = False
# 		root = Node([], board, None)

# 		while not end_game:
# 			value , move = first_tree_maker(root, player, depth, skip)
# 			if move == None:
# 				end_game = terminate(root)
# 				skip = False
# 			elif move:
# 				root.board = flip(root.board, move, player)
# 				skip = False
# 			elif move == 0:
# 				skip = True
			
# 			#player = -player
# 			op_move = opponent_random_move(root.board, -player)
# 			if op_move != None:
# 				root.board = flip(root.board, op_move, -player)
# 			print(root.	board)
# 			print(value)

# 		if np.sum(root.board) > 0:
# 			wins += 1

# 	print(wins, ' / ', iterations)
