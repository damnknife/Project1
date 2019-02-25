import random

def roll_dice(n_dices = 1, n_sides = 6):
    ''''Roll a given number of n-sided dices and return the output as a list
    Input: n_dices(default = 1)
           n_sides(default = 6)'''
    results = []
    if n_sides <= 0:
        print('Invalid input')
        return None
    else:
        for x in range(n_dices):
            results.append(random.randint(0,n_sides))
    return results
