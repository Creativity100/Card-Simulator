'''
1 - 13   spades
14 - 26  hearts
27 - 39  clovers
40 - 52  diamonds
'''
DECK = []

def card_simulator(num_of_trials):
    # validate param
    if num_of_trials <= 0:
        print(f'invalid number of trials {num_of_trials}')
        return




if __name__ == "__main__":
    num_of_trials = int(input("How many trials do you want to run?\n"))

    # fill up deck
    for i in range(52):
        DECK.append(i + 1)

    card_simulator(num_of_trials)