import multiprocessing as mp
import pygame
from helpers.snakeGameGATrain import SnakeGameGATrain
from helpers import geneticAlgorithm as ga 



def main():
	"""Function to train the genetic algorithm for creating intelligent Snake Game agents."""
	game_fps = 999999999
	chroms_per_gen = 500
	num_inputs = 8
	num_hidden_layer_nodes = 20
	bits_per_weight = 9
	num_outputs = 4
	total_bits = ((num_inputs+1)*num_hidden_layer_nodes + num_hidden_layer_nodes*(num_hidden_layer_nodes+1) + num_outputs*(num_hidden_layer_nodes + 1))*bits_per_weight
	population = ga.genPopulation(chroms_per_gen, total_bits)
	game = SnakeGameGATrain(game_fps, population, chroms_per_gen, bits_per_weight, num_inputs, num_hidden_layer_nodes, num_outputs)
	
	pygame.font.init()

	while game.play:

		game.clock.tick(game.fps)
		
		game.move_snake()
		game.check_collisions()
		#check if snake is killed for not eating a fruit in a while
		game.update_frames_since_last_fruit()
		game.frames_alive += 1

		if game.restart == True:
			game.restart = False
			continue
		
		game.redraw_window()
		
		game.event_handler()
		
main()