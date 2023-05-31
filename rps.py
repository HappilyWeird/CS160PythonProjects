import random

from colorama import init, Fore, Back, Style

options = ['rock', 'paper', 'scissors', 'spock', 'lizard']
# 0, 1, 2, 3, 4

choices = options[:]

#Which option beats which
def thinker (ply, comp):
    print("player", ply)
    print("computer", comp)
    result = options.index(ply) - options.index(comp)
    result = result % 5
    if result % 2 == 0:
        choices.append(options[options.index(ply) + 1 % 5])
        
        choices.remove(comp)
    else:
#     elif result == 2:
        choices.append(comp)
    return result #1 = player W, 2 = player L, 0 = T

#Play instructions
print(Fore.MAGENTA + "Let's play Rock/Paper/scissors/Lizard/Spock!")
print(Fore.WHITE + "Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has: rock crushes scissors.")
print(Fore.BLUE + 'All hail Sam Kass!')

while True:    #Randomly choose one
    compchoice = random.choice(choices)

    #Get input
    plychoice = ""
    while plychoice not in options:
        plychoice = input(Fore.GREEN + "Pick one (rock, paper, scissors, lizard, or spock): ")
        plychoice = plychoice.lower()

    print(Fore.WHITE + "Computer", compchoice, "Player", plychoice)
    win = thinker(plychoice, compchoice)
    if win % 2 == 0:
        print(Fore.RED + 'Too bad... Try again: ')
    else:
        print(Fore.YELLOW + 'You win! Go again: ')