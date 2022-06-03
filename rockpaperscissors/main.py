import random

instruction = '\nThis is Rock Paper Scissors game.\n'
instruction += 'Input:\n\t"R" for Rock,\n\t"P" for Paper\n\t"S" for Scissors.\n'
print(instruction)

def wrong_input():
    print('Wrong Input')
    print('Input:\n\t"R" for Rock,\n\t"P" for Paper\n\t"S" for Scissors.\n')

options = ['R', 'P', 'S']
options_mapper = {
    'R': 'ROCK',
    'P': 'PAPER',
    'S': 'SCISSORS'
}

quit_options = ['q', 'Q' 'quit']

def play_game():
    quit = ''
    while quit not in quit_options:
        player_choice = input('What do you choose: ').upper()
        cpu_choice = random.choice(options)

        while player_choice not in options:
            wrong_input()
            player_choice = input('What do you choose: ').upper()
        if player_choice == cpu_choice:
            decison = 'TIE'
        else:
            if player_choice == 'R':
                if cpu_choice == 'P':
                    decison = 'CPU won'
                else:
                    decison = 'You won'
            
            if player_choice == 'P':
                if cpu_choice == 'S':
                    decison = 'CPU won'
                else:
                    decison = 'You won'
            
            if player_choice == 'S':
                if cpu_choice == 'R':
                    decison = 'CPU won'
                else:
                    decison = 'You won'

        print(f"Moves:\n\tPlayer: {options_mapper[player_choice]}\n\tCPU: {options_mapper[cpu_choice]}\n\t{decison}")
        quit = input('Enter q to quit or any letter to play again: ')

play_game()
