# This is a programming project prepared by Yap Wei Xiang (21067939) for Dr Matthew Teow.
# In this project, I will be coding a playable game of Mastermind.

# Put the game under one function
def game():
    # Import random library
    import random

    # Create a list of all possible colours
    colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']

    # For Code Maker
    answer = random.choices(colours, k=4)  # To randomise the selection of colours.

    # To Compare Lists
    # Function to check number of correct colours in the correct places
    def black_peg():
        x = 0
        for i in range(len(answer)):
            if answer[i] == guess[i]:
                x += 1
        return x

    # Function to check number of correct colours in total
    def white_peg():
        s = 0
        for p in colours:
            q = answer.count(p)
            r = guess.count(p)
            if q <= r:
                s += q
            else:
                s += r
        return s

    # For Player
    guess = []  # List to compare user's guess with answer
    counter = 0  # Variable that increases until user's guess is correct

    while guess != answer:
        giveup = 0
        guess = []  # Start with an empty list everytime the user's guess is wrong
        for x in range(len(answer)):
            userGuess = 0
            while userGuess == 0:
                userGuess = input("\nWhat colour do you think is in slot " + str(x + 1) + "?\n")
                userGuess = userGuess.lower()
                if userGuess == 'red' or userGuess == 'r':
                    userGuess = 'Red'
                elif userGuess == 'orange' or userGuess == 'o':
                    userGuess = 'Orange'
                elif userGuess == 'yellow' or userGuess == 'y':
                    userGuess = 'Yellow'
                elif userGuess == 'green' or userGuess == 'g':
                    userGuess = 'Green'
                elif userGuess == 'blue' or userGuess == 'b':
                    userGuess = 'Blue'
                elif userGuess == 'purple' or userGuess == 'p':
                    userGuess = 'Purple'
                elif userGuess == 'quit' or userGuess == 'q':  # Giving the user the option to quit the game if they give up.
                    giveup = 1
                    break
                else:
                    userGuess = 0
                    print("I do not recognise that input. Let's try this again.")

            if giveup == 1:
                break
            else:
                guess.append(userGuess)
        if giveup == 1:
            break

        print("\nYour input was: " + str(guess)[1:-1] + ".")
        counter += 1
        if guess != answer:
            print("\nYou got it wrong!")
            slotsCorrect = black_peg()
            print("Correct colour(s) in the correct place(s):" + str(slotsCorrect))
            coloursCorrect = white_peg()
            # since coloursCorrect accounts for all colours, we take the difference between coloursCorrect and slotsCorrect
            rightColourWrongSlot = coloursCorrect - slotsCorrect
            print("Correct colour(s) in the wrong place(s): " + str(rightColourWrongSlot))

    # Congratulatory message for when the user eventually gets to the answer
    if giveup == 0:
        print("Congratulations! You broke my code! It took you " + str(counter) + " attempt(s)!")
    # Message for when the user quits halfway through the game
    elif giveup == 1:
        print("Looks like you couldn't break my code! The code was " + str(answer)[1:-1] + ". Better luck next time!")



# Writing a Main Menu for the game

# Writing Instructions
gameInstructions = "The objective of the game is to guess a sequence of four colours that I have selected. There\n" \
                   "are six total colours to choose from: RED, ORANGE, YELLOW, GREEN, BLUE and PURPLE. You can input\n" \
                   "the colours using their full names, or if you choose to, you can also just use the first letter \n" \
                   "of the respective colours, e.g. R for RED and B for BLUE. \n" \
                   "I will ask you for ONE colour at a time, each turn, you will need to decide\n" \
                   "on FOUR. At the end of each turn, I will let you know how many colours you have chosen are correct " \
                   "and in the\n" \
                   "right places, and how many are correct but in the wrong places. You will need to use your own\n" \
                   "thinking to beat me!\n" \
                   "\nP.S. Don't forget that the order of the colours matter! Also capitalisation does not matter."\
                   "\nP.P.S You can quit the game any time by inputting 'quit' or 'q'."


mainMenu = 1

while mainMenu == 1:
    menu = input("=========================== M A S T E R M I N D ===========================\n"
                 "Input 'P' to start playing, 'I' for instructions and 'Q' to quit the game.\n")
    menu = menu.lower()
    print()
    if menu == 'p' or menu == 'play':
        print("=========================== M A S T E R M I N D ===========================\n")
        game()
    elif menu == 'i' or menu == 'instructions':
        print("======================== I N S T R U C T I O N S =========================\n")
        print(gameInstructions)
    elif menu == 'q' or menu == 'quit':
        mainMenu = 0
    else:
        print("I do not recognise that input. Let's try this again.")
    print()
