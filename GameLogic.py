class GameLogic(object):
    
    def __init__(self):
        # Initialize various variables
        self.prompt_choices = {
        "m": "missionary",
        "c": "cannibal",
        "q": "quit"
        }

        self.response = ""
        self.response2 = ""
        self.response3 = ""


    def display_locations(self, east_bank, west_bank, canoe):
        """ Handles the logic for displaying the locations """

        output = """
        West Bank Contains                       East Bank contains
        Missionaries: %s                          Missionaries: %s
        Cannibals:    %s                          Cannibals:    %s
        """ % (west_bank['missionaries'], east_bank['missionaries'], west_bank['cannibals'], east_bank['cannibals'])

        print(output)

        if canoe['location'] == "west":
            print("Canoe is on the west bank")
        else:
            print("                                                 Canoe is on the east bank")

        print('\n')

        return

    def update_locations(self, user_choice, east_bank, west_bank, canoe):
        """ Handles the logic for updating each location """

        print("Variables before manipulation$$$$$$")
        print(user_choice)
        print("EAST", east_bank)
        print("WEST", west_bank)
        print(canoe)

        for i in user_choice:
            if i is not None and i is not "":
                if canoe['location'] == "east":

                    if i == "m":
                        east_bank['missionaries'] = east_bank['missionaries'] - 1
                        west_bank['missionaries'] = west_bank['missionaries'] + 1
                    else:
                        east_bank['cannibals'] = east_bank['cannibals'] - 1
                        west_bank['cannibals'] = west_bank['cannibals'] + 1

                    print("Variables east manipulation$$$$$$")
                    print(user_choice)
                    print("EAST", east_bank)
                    print("WEST", west_bank)
                    print(canoe)

                elif canoe['location'] == "west":
                    if i == "m":
                        east_bank['missionaries'] = east_bank['missionaries'] + 1
                        west_bank['missionaries'] = west_bank['missionaries'] - 1
                    else:
                        east_bank['cannibals'] = east_bank['cannibals'] + 1
                        west_bank['cannibals'] = west_bank['cannibals'] - 1

                    print("Variables west manipulation$$$$$$")
                    print(user_choice)
                    print("EAST", east_bank)
                    print("WEST", west_bank)
                    print(canoe)

                else:
                    print("Nothing")

        if canoe['location'] == "east":
            canoe['location'] = "west"
        else:
            canoe['location'] = "east"


        return (east_bank, west_bank, canoe)

    def check_for_win(self, east_bank, west_bank):
        """ Handles the logic needed for checking to see if there has been a win """
        #print("West bank MSN = {}".format(west_bank['missionaries']))
        #print("West bank CNB = {}".format(west_bank['cannibals']))
        #print("East bank MSN = {}".format(west_bank['missionaries']))
        #print("East bank CNB = {}".format(west_bank['cannibals']))

        if west_bank['missionaries'] == 3 and west_bank['cannibals'] == 3:
            return 'Winner'
        elif west_bank['cannibals'] > west_bank['missionaries'] and west_bank['missionaries'] > 0:
            return 'Loser'
        elif east_bank['cannibals'] > east_bank['missionaries'] and east_bank['missionaries'] > 0:
            return 'Loser'
        else:
            return 'continue to play'

    def user_prompt(self, east_bank, west_bank, canoe):
        """ Handles the logic needed for asking a user for information """
        global response
        global response2
        global response3

        response = ""
        response2 = ""
        response3 = ""

        #print("BEGIN: Response3 = ", response3)

        if canoe['location'] == "east":
            response = input("Who would you like to send to the west bank? Type 'm' for missionary or 'c' for cannibal or 'q' to quit:")
            response = str(response)

            response2 = input("Who would you like to send next to the west bank? Type 'm' for missionary or 'c' for cannibal or 'q' to quit:")
            response2 = str(response2)

            try:
                value = self.prompt_choices[response]
                value2 = self.prompt_choices[response2]
            except Exception as error:
                print("That is not a valid choice. Please try again.")
                self.user_prompt(east_bank, west_bank, canoe)

            if value != "quit" and value2 != "quit":
                validate_move = self.ValidateMove(response, east_bank, west_bank, canoe, response2)
                if validate_move is True:
                    print("\nSending a {} and a {}... good luck!".format(value, value2))
                    return (response, response2, response3)
                else:
                    print("Your selection is invalid - move will not work.")
                    self.user_prompt(east_bank, west_bank, canoe)
            else:
                print("Thank you for playing!")

        if canoe['location'] == "west":
            response3 = input("Who would you like to take the boat back to the east bank? Type 'm' for missionary or 'c' for cannibal or 'q' to quit:")
            response3 = str(response3)
            #print("Response3 = ", response3)

            try:
                value = self.prompt_choices[response3]
            except Exception as error:
                print("That is not a valid choice. Please try again.")
                self.user_prompt(east_bank, west_bank, canoe)

            if value != "quit":
                validate_move = self.ValidateMove(response3, east_bank, west_bank, canoe, None)
                if validate_move is True:
                    #print(response, response2, response3)

                    print("\nReturning a {}... good luck!".format(value))
                else:
                    print("Your selection is invalid - move will not work.")
                    #print(response, response2, response3)

                    self.user_prompt(east_bank, west_bank, canoe)
            else:
                print("Thank you for playing!")

            #print("END: Response3 = ", response3)

        return (response, response2, response3)

    def ValidateMove(self, user_choice, east_bank, west_bank, canoe, user_choice2=None):
        """ Handles the logic for validating a move """

        #print("USERCHOICE = ", user_choice)

        if canoe['location'] == 'west':
            if user_choice == 'm':
                if west_bank['missionaries'] > 0:
                    return True
                else:
                    return False
            if user_choice  == 'c':
                if west_bank['cannibals'] > 0:
                    return True
                else:
                    return False
        ##########################################

        if canoe['location'] == 'east':
            # If the user chooses both missionaries to send...
            if user_choice == 'm' and user_choice2 == "m":
                if east_bank['missionaries'] > 1:
                    return True
                else:
                    return False

            # If the user chooses both cannibals to send...
            if user_choice == 'c' and user_choice2 == "c":
                if east_bank['cannibals'] > 1:
                    return True
                else:
                    return False

            # If the user chooses one missionary and one cannibal...
            if user_choice == 'm' and user_choice2 == "c":
                if east_bank['cannibals'] > 0 and east_bank['missionaries'] > 0:
                    return True
                else:
                    return False

            # Same as above, just with reversed logic choice
            if user_choice == 'c' and user_choice2 == "m":
                if east_bank['cannibals'] > 0 and east_bank['missionaries'] > 0:
                    return True
                else:
                    return False
