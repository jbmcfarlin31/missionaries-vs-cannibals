from GameLogic import GameLogic
import sys

west_bank = {"missionaries": 0, "cannibals": 0}
east_bank = {"missionaries": 3, "cannibals": 3}
canoe = {"location": "east"}


def display_story():
	print("||------------------------------------------------------------------||")
	print("||                                                                  ||")
	print("||  Welcome to the Missonaries and Cannibals Logic Puzzle!!         ||")
	print("||                                                                  ||")
	print("||  In the missionaries and cannibals puzzle, three missionaries    ||")
	print("||  and three cannibals must cross a river using a canoe which can  ||")
	print("||  carry no more than two people, under the constraint that, if    ||")
	print("||  there are missionaries present on a bank, they cannot be        ||")
	print("||  outbumbered by cannibals, otherwise the cannibals would eat     ||")
	print("||  them.  The boat cannot cross the river by itself with no people ||")
	print("||  on board.                                                       ||")
	print("||                                                                  ||")
	print("||------------------------------------------------------------------||")

	print('\n')
# --------------------------------------

def display_win():
	print("||------------------------------------------------------------------||")
	print("||                                                                  ||")
	print("||  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                                 ||")
	print("||  !!!!!   You WON   !!!!!!!!!!!!!                                 ||")
	print("||  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!                                 ||")
	print("||                                                                  ||")
	print("||  You have helped the missionaries cross the river with the       ||")
	print("||  cannibals in tow.  The cannibals are sure to be rehabilitated.  ||")
	print("||  Just think of all the lives you just saved.  You sir or ma'am   ||")
	print("||  are a true hero!                                                ||")
	print("||                                                                  ||")
	print("||  Three cheers for you:                                           ||")
	print("||       YAY you!                                                   ||")
	print("||            YAY you!                                              ||")
	print("||                 YAY you!                                         ||")
	print("||                                                                  ||")
	print("||------------------------------------------------------------------||")

	print('\n')
# --------------------------------------

def display_lost():
	print("||------------------------------------------------------------------||")
	print("||  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                           ||")
	print("||  XXXXX   You have LOST   XXXXXXXXXXXXX                           ||")
	print("||  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                           ||")
	print("||                                                                  ||")
	print("||  The missionaries have been eaten by the cannibals!  Your poor   ||")
	print("||  decisions have led to the downfall of this expeditation.        ||")
	print("||  If only you were better at logic puzzles....                    ||")
	print("||                                                                  ||")
	print("||------------------------------------------------------------------||")

	print('\n')

# --------------------------------------

def run():
	""" The main method for running our game """

	# Class instantiation
	obj = GameLogic()

	# Initialize variables
	WinLoseCheck = 'continue to play'
	global west_bank
	global east_bank
	global canoe

	# Call print story
	display_story()

	#Begin game
	while WinLoseCheck == 'continue to play':
	    #Call display locations
	    obj.display_locations(east_bank, west_bank, canoe)

	    #call ask
	    val_ask = obj.user_prompt(east_bank, west_bank, canoe)
	    if val_ask[0] == "q" or val_ask[1] == "q" or val_ask[2] == "q":
	        sys.exit(1)
	    else:
	        # Update locations
	        #print("Hello world ######", val_ask)
	        result = obj.update_locations(val_ask, east_bank, west_bank, canoe)
	        east_bank = result[0]
	        west_bank = result[1]
	        canoe = result[2]

	        WinLoseCheck = obj.check_for_win(east_bank, west_bank)


	if WinLoseCheck == "Winner":
		display_win()
	elif WinLoseCheck == "Loser":
		display_lost()
	else:
		pass

run()
