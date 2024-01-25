import copy
import random

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
    global count, total_trials

    # validate param
    if num_of_trials <= 0:
        print(f'invalid number of trials {num_of_trials}')
        return

    # run trials
    for i in range(num_of_trials):
        deck = copy.deepcopy(DECK)

        # draw 13 cards without replacement
        ace_count = 0
        for j in range(13):
            random_index = random.randint(1, len(deck))
            draw = deck.pop(random_index - 1)

            if draw % 13 == 1:
                ace_count += 1

            if ace_count > 1:
                break

        # increment
        count = count + 1 if ace_count == 1 else count
        total_trials += 1


def print_results():
    print("RESULTS:")
    print(f'Total trials run:         {total_trials}')
    print(f'Number of counts:         {count}')
    print(f'Theoretical probability:  {count / total_trials}')


if __name__ == "__main__":
    n = int(input("How many trials do you want to run?\n"))

    # fill up deck
    for i in range(52):
        DECK.append(i + 1)

    card_simulator(n)
    print_results()