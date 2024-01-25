'''
1 - 13   spades
14 - 26  hearts
27 - 39  clovers
40 - 52  diamonds
'''
DECK = []
count = 0
total_trials = 0


def card_simulator(num_of_trials):
    # validate param
    if num_of_trials <= 0:
        print(f'invalid number of trials {num_of_trials}')
        return

    # run n trials
    count = 0
    total = 0
    for i in range(num_of_trials):
        pass


def print_results():
    print("RESULTS:")
    print(f'Total trials run:         {total_trials}')
    print(f'Number of counts:         {count}')
    print(f'Theoretical probabilitY:  {count / total_trials}')


if __name__ == "__main__":
    num_of_trials = int(input("How many trials do you want to run?\n"))

    # fill up deck
    for i in range(52):
        DECK.append(i + 1)

    card_simulator(num_of_trials)