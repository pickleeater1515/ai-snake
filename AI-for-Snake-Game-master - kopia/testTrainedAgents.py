import pygame
from helpers.snakeGameGATest import SnakeGameGATest


def main():
	"""Function to test the best agents trained with the genetic algorithm to play the snake game."""

	print("\nA few notes:")
	print("If it seems like the snake dies suddenly, it is probably because the snake dies whenever it decides")
	print("to move in the direction opposite to where its head is facing.")
	print("Also, snakes will automatically die if they do not eat a fruit for a certain amount of time.")
	print("Finally, the game will automatically restart whenever the snake dies.")
	print("\nNow, which snake agent would you like to observe?")
	print("Each agent to choose from generates unique patterns of movement.")
	#Loop until user selects a valid option
	while True:
		input_num = input("Type a number from 1-3: ")
		#Determine which menu option was selected.
		if input_num == "1" or input_num == "1.":
			chrom = '0000110010100010011101111111101010001001000110000101111010110010011011110101111110001110111010010000100010000111011100010110011100101101110110110111111110010101100010001010111110010000001101000000101000010010110101101100001110001001110110001100100000001110010010001110000101010111111110010001101101100111011100110100011000000101100101001001011100101011000001001000100100101111001001110010000010101101100110100100001010000011001000100101011011000111010101100011111100011110100100011110110010101111010111100001101000000011110000011010001111000011011110000001101101101010000100110110100010011000110000000100011011011101000010100101111001111101100111000111001010111101001101111101100100111011101001001000000010000001010001011110101010100111110111111110011000011010100010101111001110010011111010011010111000111000000000111111011111011000110110100111011111100101000000010010110010111001101100000110010110011110111011000000111110101000110111001111110111001000001011110010010000100111010001110000101001101111000100010011110100111000010010001101001000001011010000001001010101111100001101100011011110111011101111110000000100011000011001011100011111111101111000000011010010100101000000100000010000011100000011111100110010000111000000111101101110101001100101011111110101001010000000011011111010110110010111100100010111010000101001001101000010011111000000101000000101111000111000101101100110100001000111010011001101110000011010001000001101001010100101000011000010111110101010110101111011100001111011100101101101000110011101001001100000110111111011111000000111101011011111011110001100111000010111100011011000100011000001111110011000011010001100001000100100100111111111111010111010111011011101010011111000010000110110111101001100100110100100101001101011110101100000000100101001100001011000110011000110011110011000101000110000011000100110100100010011010000110100100100000100001001110010000101001100101101000111011110000100011110001010011001101101000010000100010010011111100010110000001010100011100110000101111101100011011101000110110101111110111001'
			break
		elif input_num == "2" or input_num == "2.":
			chrom = '0011001100110011011011010100111110100111011110001011100100010101011111011100011010010110111010110000000010000110011101110101000100111110110110100111110111010101100001011011111000111001000001110010100000010010001111111111010110001011010001111100011100000100010010011110000001011001111110000000010001111101011111100101001100010111000011111001111111110100010010011000000001011111000001100111110010111101100010000101000110101001000110100001100100010100111001100010110100101101110110101110001010111111010100000001100000000000110001001111111011001001011111110001000000011110010101100110011101001100100011001100001100110111100111110011110011101000100000101110111111011001101110010111110111100111100010001001101111110100011100111111011011100101110010101010111110001101100011111000000000000001111111000000010111011000000100000110001011111101011110000110101011100101100111000010111010011110111010011100001100000000110101100101101100000100100101001110101000101001001010000011010100000101000101110001110000010010000100010110100100011000000100011100110011101011010010000100110001110000001001011100111011000000110101110111100100100111010010101000010110101111110100100010010000000100110001100101001111110110010011101001110000110110011110110111001111100001100111011111101001101110001000010111110001000110000110110011000110010001100010001110000111110101000001111101011000001000001101111011001111101101101011010101000000110111011111011010101100100010011010000111010101110111100000110001110010011110010000001111100100011011010001110011111001011110001011011111111111101101101111010000110001110110001101100100000000111111110110000000110101100100011011011101111000000101111110110010101001001100011110000101111000000010100111101000100110111100101100010110101011100010100111100001001001101101111011000111111010010111011000101010110100100000011010000101100011000000110111100111101100010000110101110111001100011000001100011101000001100000010000101001101011000110000101100011001111101010110001100000100110100101001100101011101111010011110110000111111111101110'
			break
		elif input_num == "3" or input_num == "3.":
			chrom = '0000110000100010011101110111101010000001000110010101100000110010011011110101111010001110111010010000111010000100011100010110011100101101110110110111111110111100100010011010111110010010001100000000101000010010010111111100001110001001110111011100100000001101010000001111100001010111111110000001001101100111011101000100001110100101000101001001011100111010010001001010100100100111000001110000000010110101100110100000000110001001010000100101011001010010010101110001111100011110100100011110110010101110010110100001001100000011110000001010001111000011011111000000110101101110000100110011101011001001110100000100111010101101000111100001011011011000100110100111001010111101001101111101100100110011100001001001000010000010011101100110101011000100110111111111011110011110100010101011000101010011110001011110111111110000000000111100001111111100010100100110011111000110100000110010110010011011100001000101000110011100101111100000010011101000110111111111110111001000001011100010010000110111000101010001000011101111000101101001110100101000011000101111011000001111011000101101010101111110001101110011011110111111101111110000000100011000011001111100011111111101111000001011010010110101000000100000010011111000000011111100110010000111000100101111001110100000100100001111110101001010001000001011110010110111010111100100100011010000101101001101000000011111000000101001100101111000111000100101001110101001000110010011001101110000011010000000000100011010100101000011000010110110101010110001111001111001111010000101110101000101000101000001101010110111111011111000000111101000011111011110000101111010010111000111111010100010000001111110010000001010001110001000100100110101110101110110111010010011011101010011111000010000110111111101100100100010100110001001100011010101100100000100101001100001011000110011000111011110010000001001100000011000100110100100010011010001010100010100000000001001110111000111101100001001000011011110000100010110001100011000001101001010000100000010011011100010110011011110100111100010001101111001100111110101100100110110111111111000'
			break
		else:
			#No valid input.
			print("\nError: that was not a number from 1-3, please try again.")

	fps = 150
	num_inputs = 9
	num_hidden_layer_nodes = 10
	bits_per_weight = 8
	num_outputs = 4
	game = SnakeGameGATest(fps, chrom, bits_per_weight, num_inputs, num_hidden_layer_nodes, num_outputs)
	pygame.font.init()
	

	while game.play:

		game.clock.tick(game.fps)
		
		game.move_snake()
		game.check_collisions()

		#check if snake is killed for not eating a fruit in a while
		game.update_frames_since_last_fruit()

		if game.restart == True:
			game.restart = False
			continue
		
		game.redraw_window()
		game.event_handler()

if __name__ == "__main__":	
	main()