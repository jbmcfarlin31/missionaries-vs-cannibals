from GameLogic import GameLogic
import sys
from datetime import datetime, date, time

# Our global variables
west_bank = {"missionaries": 0, "cannibals": 0}
east_bank = {"missionaries": 3, "cannibals": 3}
canoe = {"location": "east"}


def display_story():
	""" This method handles the display of the story at the begining of the game """

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
	""" This method handles the display of the winning screen """

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
	""" This method handles the display of the losing screen """

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

	# We check to see if the user wants to see the solution...
	# TODO: Make user lose 5 times before showing?
	response = input("Would you like to see the solution? Type 'y' for yes or 'n' for no: ")
	response = str(response)

	if response == "y":
		show_solution()

# --------------------------------------

def show_solution():
	""" This method handles the display of the solution to beat the game """

    print("||------------------------------------------------------------------||")
    print("||                                                                  ||")
    print("||  Missionaries vs. Cannibals solution                             ||")
    print("||                                                                  ||")
    print("||  1) Send two cannibals to the west bank                          ||")
    print("||  2) Send one cannibal back to the east bank                      ||")
    print("||  3) Send two cannibals back to the west bank                     ||")
    print("||  4) Send one cannibal back to the east bank                      ||")
    print("||  5) Send two missionaries back to the west bank                  ||")
    print("||  6) Send one missionary and one cannibal back to the east bank   ||")
    print("||  7) Send two missionaries to the west bank                       ||")
    print("||  8) Send one cannibal back to the east bank                      ||")
    print("||  9) Send two cannibals to the west bank                          ||")
    print("||  10) Send one cannibal back to the east bank                     ||")
    print("||  11) Send two cannibals back to the west bank                    ||")
    print("||                                                                  ||")
    print("||------------------------------------------------------------------||")

    print('\n')

def run():
	""" The main method for running our game """

	# Keep track of when the game was started... 
	# this is so that if you win, we can display how long it took you
	start_time = datetime.now()

	# Class instantiation
	obj = GameLogic()

	# Initialize variables
	WinLoseCheck = 'continue to play'
	global west_bank
	global east_bank
	global canoe

	# Display the story so use knows what to do
	display_story()

	#Begin game
	while WinLoseCheck == 'continue to play':
	    # Display the locations
	    obj.display_locations(east_bank, west_bank, canoe)

	    # Ask for user prompt of who to send
	    val_ask = obj.user_prompt(east_bank, west_bank, canoe)
	    if val_ask[0] == "q" or val_ask[1] == "q":
	        print("Thank you for playing!")
	        sys.exit(1)
	    else:
	        # Update location dictionaries and reset values
	        result = obj.update_locations(val_ask, east_bank, west_bank, canoe)
	        east_bank = result[0]
	        west_bank = result[1]
	        canoe = result[2]

	        # Check for a win/loss
	        WinLoseCheck = obj.check_for_win(east_bank, west_bank)

	# If there is a win, get the ending time so we can compare start_time to see how long it took
	# We also display the winning screen, otherwise show the losing screen
	if WinLoseCheck == "Winner":
		end_time = datetime.now()
		date_diff = end_time - start_time
		print("You completed the game in: ", date_diff)

		display_win()
	elif WinLoseCheck == "Loser":
		display_lost()
	else:
		pass

# Run the main program and start the game
run()
