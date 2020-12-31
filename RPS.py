# Rock paper scissors game against the computer
# Can you beat random chance?
# Play and find out!
import random

def RPS():
    print("Welcome to Rock Paper Scissors\nPlease enter your name")
    playername = ""
    while playername=="":
        usr_input = input("Name: ")
        if usr_input=="":
            print("Looks like Nobody is playing my game, but Polyphemus won't be tricked!\nPlease enter your name")
        else:
            playername = usr_input
    player_choice = ""
    outcome = ""
    winner = ""

    # Dictionary of what beats what (key beats value)
    hier = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}

    def computer_choice():
        comp_choice = ""
        options = ['Rock', 'Paper', 'Scissors']
        rndm_num = random.randint(0,2)
        comp_choice = options[rndm_num]
        return comp_choice

    def play(player, computer, hier):
        outcome = ""
        if player==computer:
            outcome = "Tie"
        else:
            if hier[player] == computer:
                outcome = 'Player'
            else:
                outcome = "Computer"
        return outcome

    def print_hand(player, computer):
    # Make sure inputs are in form 'Rock', 'Paper', or 'Scissors' or alter dictionary
        # Rock
        rock = ['     _____    ',
                '   /       \  ',
                '  /  #      \\ ',
                ' /  ##       |',
                ' \          / ',
                '  \________/  ']

        # Paper
        paper = ['  ________    ',
                 ' | ~~~~~~ |   ',
                 ' | ~~~~~~ |   ',
                 ' | ~~~~~~ |   ',
                 ' | ~~~~~~ |   ',
                 ' |________|   ']

               # Scissors
        scissors = ['   (_)  / )   ',
                    '     | (_/    ',
                    '    _./       ',
                    '   //|\\      ',
                    '  // | )      ',
                    ' (/  |/       ']

        images = {'Rock': rock, 'Paper': paper, 'Scissors': scissors}
        player_image = images[player]
        comp_image = images[computer]

        print()
        print(' You                 Computer')
        print()
        for i in range(len(player_image)):
            if i == 2:
                print(player_image[i], ' VS ', comp_image[i])
            else:
                print(player_image[i], '    ', comp_image[i])
        print()

    while winner == "":
        player_choice = ""
        while player_choice=="":
            player_input = input("Make your choice (Rock/Paper/Scissors): ").capitalize()
            if player_input not in hier:
                print("Sorry, I couldn't read that. Please omit any spaces or\nspelling errors and try again.")
            else:
                print("Rock...Paper...Scissors...Shoot!")
                player_choice = player_input
        comp_choice = computer_choice()
        #print('You chose:', player_choice)
        #print('Computer chose:', comp_choice)
        print_hand(player_choice, comp_choice)

        outcome = play(player_choice, comp_choice, hier)

        if outcome == "Tie":
            print("It's a tie! Please try again.")
        elif outcome == 'Player':
            winner = 'You win!'
        else:
            winner = 'Computer wins!'

    print(winner, ' Thanks for playing!')

RPS()
