import numpy as np
import pygame
import sys
import math

BLUE = (42,173,199)
BLACK = (0,0,0)
PINK = (248,174,196)
GREEN = (227,247,152)

ROW_COUNT = 6
COLUMN_COUNT = 7

def new_game():
	game = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return game

def drop_piece(game, row, column, position):
	game[row][column] = position

def location (game, column):
	return game[ROW_COUNT-1][column] == 0

def it_ok(game, column):
	for row in range(ROW_COUNT):
		if game[row][column] == 0:
			return row

def vue_game(game):
	print(np.flip(game, 0))

def victory(game, position):

	# Verification que les 4 sont alignés horizontalement
	for col in range(COLUMN_COUNT-3):
		for row in range(ROW_COUNT):
			if game[row][col] == position and game[row][col+1] == position and game[row][col+2] == position and game[row][col+3] == position:
				return True
		#Verification que les 4 sont alignés verticalement
	for col in range(COLUMN_COUNT):
		for row in range(ROW_COUNT-3):
			if game[row][col] == position and game[row+1][col] == position and game[row+2][col] == position and game[row+3][col] == position:
				return True

	# Diagonals ok 
	for col in range(COLUMN_COUNT-3):
		for row in range(ROW_COUNT-3):
			if game[row][col] == position and game[row+1][col+1] == position and game[row+2][col+2] == position and game[row+3][col+3] == position:
				return True

	# Check negatively sloped diaganols
	for col in range(COLUMN_COUNT-3):
		for row in range(3, ROW_COUNT):
			if game[row][col] == position and game[row-1][col+1] == position and game[row-2][col+2] == position and game[row-3][col+3] == position:
				return True

def draw_board(board):
	for col in range(COLUMN_COUNT):
		for row in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (col*SQUARESIZE, row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(col*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), CIRCLE)
	
	for col in range(COLUMN_COUNT):
		for row in range(ROW_COUNT):		
			if board[row][col] == 1:
				pygame.draw.circle(screen, PINK, (int(col*SQUARESIZE+SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2)), CIRCLE)
			elif board[row][col] == 2: 
				pygame.draw.circle(screen, GREEN, (int(col*SQUARESIZE+SQUARESIZE/2), height-int(row*SQUARESIZE+SQUARESIZE/2)), CIRCLE)
	pygame.display.update()


board = new_game()
vue_game(board)
game_over = False
turn = 0

#tentative minitueur 
#frame_count = 0
#frame_rate = 60
#start_time = 90
background = pygame.image.load('logo.png')
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Connect 4 by gomar")






SQUARESIZE = 50

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

CIRCLE = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)

pygame.display.update()

font = pygame.font.SysFont("monospace", 30)

#AJOUT DE LA MUSIQUE (J'AI FAIS TOUTE SEULE)
MUSIQUE = pygame.mixer.music.load("naps.ogg")
pygame.mixer.music.play(1, 0.0)




	
while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, PINK, (posx, int(SQUARESIZE/2)), CIRCLE)
			else: 
				pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), CIRCLE)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == 0:
				posx = event.pos[0]
				column = int(math.floor(posx/SQUARESIZE))

				if location(board, column):
					row = it_ok(board, column)
					drop_piece(board, row, column, 1)

					if victory(board, 1):
						text = font.render("Player 1 wins!!", 1, PINK)
						screen.blit(text, (40,10))
						game_over = True


			# # Ask for Player 2 Input
			else:				
				posx = event.pos[0]
				column = int(math.floor(posx/SQUARESIZE))

				if location(board, column):
					row = it_ok(board, column)
					drop_piece(board, row, column, 2)

					if victory(board, 2):
						text = font.render("Player 2 wins!!", 1, GREEN)
						screen.blit(text, (40,10))
						game_over = True

			vue_game(board)
			draw_board(board)

			turn += 1
			turn = turn % 2


#TENTATIVE MINUTEUR 
#while not done:
    #for event in pygame.event.get():  
        #if event.type == pygame.QUIT:  
            #done = True  


    #total_seconds = frame_count // frame_rate
 	#minutes = total_seconds // 60
 	#seconds = total_seconds % 60

    #output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
 

    #text = font.render(output_string, True, BLACK)
    #screen.blit(text, [250, 250])
     #frame_count += 1
 

			if game_over:
				pygame.time.wait(3000)

