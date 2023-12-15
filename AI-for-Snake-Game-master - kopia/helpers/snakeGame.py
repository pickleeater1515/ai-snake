#**************************************************************************************
#snakeGame.py
#Module with the SnakeGame class that is instantiated in playSnakeGame.py to play
#the game, and is a super class for the SnakeGameGATest and SnakeGameGATrain classes.
#*************************************************************************************

import pygame
import random
import collections
from helpers import neuralNetwork  as nn
from helpers import geneticAlgorithm as ga 
from helpers.snake import Snake


class SnakeGame():
	"""Class framework for creating the Snake Game.

	Attributes:
		self.width: The width of the pygame screen.
		self.height: The height of the pygame screen.
		self.grid_start_y: The y position that indicicates where the game grid begins (since the score info is above the grid).
		self.play = An attribute to determine if the game is being played.
		self.restart = An attribute to determine if the snake got a game over and needs to start over.
		self.clock = A pygame Clock object.
		self.fps = The frames per second of the game.
		self.rows = The number of rows in the game grid.
		self.cols = The number of columns in the game grid.
		self.snake = A Snake object representing the snake in the game.
		self.fruit_pos = The position of the frit in the grid, in (row,column) format.
		self.score = The current score in the game based on how much fruit has been eaten.
		self.high_score = The highest score achieved since the module was opened.
	"""

	def __init__(self, fps):
		"""Initializes the SnakeGame class."""

		self.width = 225
		self.height = 290
		self.grid_start_y = 60 
		self.rows = 12
		self.cols = 12
		self.win = pygame.display.set_mode((self.width, self.height))
		self.play = 1
		self.restart = False
		self.clock = pygame.time.Clock()
		self.fps = fps
		self.snake = Snake(self.rows,self.cols)
		self.fruit_pos = (0,0)
		self.generate_fruit()
		self.score = 0
		self.high_score = 0
		

		#snake color/eye
		self.eyer = 0
		self.eyeg = 0
		self.eyeb = 0
		
		self.snaker = 138
		self.snakeg = 195
		self.snakeb = 76

		#line color
		self.liner = 0
		self.lineg = 0
		self.lineb = 0



		
		
	def redraw_window(self):
		"""Function to update the pygame window every frame, called from playSnakeGame.py."""

		self.win.fill(pygame.Color(20, 20, 20))
		self.draw_data_window()
		self.draw_grid()
		self.draw_grid_updates()
		pygame.display.update()

	def draw_data_window(self):
		"""Function to draw the segment of the pygame window with the score and high score."""

		pygame.draw.rect(self.win, pygame.Color(2, 2, 2), (0,0,self.width, -self.grid_start_y))

		#Add the score and high score
		font = pygame.font.SysFont('Comic Sans', 13)
		score_text = font.render('Score: ' + str(self.score),1, (255,255,255))
		high_score_text = font.render('High score: ' + str(self.high_score), 1, (255,255,255))
		self.win.blit(score_text, (20, 25))
		self.win.blit(high_score_text, (self.width -120, 25))

	def draw_grid(self):
		"""Function to draw the grid in the pygame window where the game is played."""

		space_col = self.width//self.cols
		space_row = (self.height - self.grid_start_y)//self.rows

		for i in range(self.rows):
			#draw horizontal line
			pygame.draw.line(self.win, pygame.Color(self.liner,self.lineg,self.lineb), (0, space_row*i + self.grid_start_y),  (self.width, space_row*i + self.grid_start_y))

		for i in range(self.cols):
			#draw vertical line
			pygame.draw.line(self.win, pygame.Color(self.liner,self.lineg,self.lineb), (space_col*i, self.grid_start_y), (space_col*i, self.height))

		#draw last lines so they are not cut off
		pygame.draw.line(self.win, pygame.Color(self.liner,self.lineg,self.lineb), (space_col*self.rows-2, self.grid_start_y), (space_col*self.rows-2, self.height))
		pygame.draw.line(self.win, pygame.Color(self.liner,self.lineg,self.lineb), (0, self.height -2),  (self.width, self.height -2))

	def generate_fruit(self):
		"""Function to generate a new random position for the fruit."""

		fruit_row = random.randrange(0,self.rows)
		fruit_col = random.randrange(0,self.cols)

		#Continually generate a location for the fruit until it is not in the snake's body
		while (fruit_row, fruit_col) in self.snake.body:

			fruit_row = random.randrange(0,self.rows)
			fruit_col = random.randrange(0,self.cols)


		self.fruit_pos = (fruit_row,fruit_col)

	def move_snake(self):
		"""Function to allow the user to move the snake with the arrow keys."""
		
		keys = pygame.key.get_pressed()

		#Determine which arrow key the user selected
		if keys[pygame.K_LEFT]:
			direct = "left"
		elif keys[pygame.K_UP]:
			direct = "up"
		elif keys[pygame.K_RIGHT]:
			direct = "right"
		elif keys[pygame.K_DOWN]:
			direct = "down"
		else:
			if len(self.snake.directions) == 0:
				#Move right at beginning of game
				direct = "right"
			else:
				#Otherwise continue with previous direction if no key pressed
				direct = self.snake.directions[0]

		self.snake.directions.appendleft(direct)
		if len(self.snake.directions) > len(self.snake.body):
			self.snake.directions.pop()

		self.snake.update_body_positions()


	def draw_grid_updates(self):
		"""Function called from redraw_window() to update the grid area of the window."""

		space_col = self.width//self.cols
		space_row = (self.height - self.grid_start_y)//self.rows

		#Draw the fruit
		fruit_y = self.fruit_pos[0]
		fruit_x = self.fruit_pos[1]
		pygame.draw.rect(self.win, pygame.Color(240,100,100), (space_col*fruit_x+1, self.grid_start_y + space_row*fruit_y+1, space_col-1, space_row-1))

		#Draw the updated snake since last movement
		for pos in self.snake.body:
			pos_y = pos[0]
			pos_x = pos[1]
			
			pygame.draw.rect(self.win, pygame.Color(self.snaker,self.snakeg,self.snakeb), (space_col*pos_x+1, self.grid_start_y + space_row*pos_y+1, space_col-1, space_row-1))

		
		head = self.snake.body[0]
		head_y = head[0]
		head_x = head[1]
		head_dir = self.snake.directions[0]

		#Draw eyes on the head of the snake, determining which direction they should face
		

			#if head facing left
		if head_dir == "left":
			#draw left eye
			pygame.draw.circle(self.win, pygame.Color(self.eyer, self.eyeg, self.eyeb), (space_col*head_x+space_col//10, self.grid_start_y + space_row*head_y + (space_row*4)//5), 3)
			#draw right eye
			pygame.draw.circle(self.win, pygame.Color(self.eyer, self.eyeg, self.eyeb), (space_col*head_x+space_col//10, self.grid_start_y + space_row*head_y + space_row//5), 3)
		#if head facing up
		elif head_dir == "up":
			#draw left eye
			pygame.draw.circle(self.win, pygame.Color(self.eyer, self.eyeg, self.eyeb), (space_col*head_x+space_col//5, self.grid_start_y + space_row*head_y + space_row//10), 3)
			#draw right eye
			pygame.draw.circle(self.win, pygame.Color(self.eyer, self.eyeg, self.eyeb), (space_col*head_x+(space_col*4)//5, self.grid_start_y + space_row*head_y + space_row//10), 3)
		#if head facing right
		elif head_dir == "right":
			#draw left eye
			pygame.draw.circle(self.win, pygame.Color(self.eyer, self.eyeg, self.eyeb), (space_col*head_x+(space_col*9)//10, self.grid_start_y + space_row*head_y + space_row//5), 3)
			#draw right eye
			pygame.draw.circle(self.win, pygame.Color(self.eyer, self.eyeg, self.eyeb), (space_col*head_x+(space_col*9)//10, self.grid_start_y + space_row*head_y + (space_row*4)//5), 3)
		#if head is facing down
		else:
			#draw left eye
			pygame.draw.circle(self.win, pygame.Color(self.eyer, self.eyeg, self.eyeb), (space_col*head_x+space_col//5, self.grid_start_y + space_row*head_y + (space_row*9)//10), 3)
			#draw right eye
			pygame.draw.circle(self.win, pygame.Color(self.eyer, self.eyeg, self.eyeb), (space_col*head_x+(space_col*4)//5, self.grid_start_y + space_row*head_y + (space_row*9)//10), 3)



	def check_collisions(self):
		"""Function that consecutively calls all the functions that detect collisions."""

		self.check_fruit_collision()
		self.check_wall_collision()
		self.check_body_collision()

	def check_fruit_collision(self):
		"""Function that detects and handles if the snake has collided with a fruit."""

		#If we found a fruit
		if self.snake.body[0] == self.fruit_pos:
			#Add the new body square to the tail of the snake
			self.snake.extend_snake()
			#Generate a new fruit in a random position
			self.generate_fruit()
			
			self.score += 1

	def check_wall_collision(self):
		"""Function that checks and handles if the snake has collided with a wall."""

		#Only need to check the colisions of the head of the snake
		head = self.snake.body[0]
		head_y = head[0]
		head_x = head[1]

		#If there is a wall collision, game over
		if head_x == self.cols or head_y == self.rows or head_x < 0 or head_y < 0:
			self.game_over()

	def check_body_collision(self):
		"""Function that checks and handles if the snake has collided with its own body."""

		if len(self.snake.body) > 1:
			#Only need to check the colisions of the head of the snake
			head = self.snake.body[0]
			body_without_head = self.snake.body[1:]

			if head in body_without_head:
				self.game_over()

	def event_handler(self):
		"""Function for cleanly handling the event of the user quitting."""

		for event in pygame.event.get():
			#Check if user has quit the game
			if event.type == pygame.QUIT:
				self.run = False
				pygame.quit()
				quit()

	def game_over(self):
		"""Function that restarts the game upon game over."""

		self.snake = Snake(self.rows,self.cols)
		self.generate_fruit()
		self.restart = True
		if self.score > self.high_score:
			self.high_score = self.score
		self.score = 0