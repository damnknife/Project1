import random

def get_word(src = 'hangman_words.txt'):
    '''take a txt source file with a list of words, separated in lines
    and return a random word
    Input: src(defaulted to a list of 50 most commom english nouns)'''
    with open(src) as file:
        data = file.read()
        word_list = data.split('\n')
    return str(word_list[random.randint(0, len(word_list))])


def generate_board(word):
    '''Generate a string with the same # of _ as letters in the word'''
    board = ''
    for letter in word:
        board = board + '_'
    return board


def guess_letter(guessed, board, word):
    '''Take a user input and return if guess is correct
    input: guessed: Guessed letter
            board: current state of the board'''
    board = list(board)
    flag_guess = 0
    for letters in range(len(word)):
        if list(word)[letters] == guessed:
            board[letters] = guessed
            flag_guess += 1
    #print(word)
    return ''.join(board), flag_guess != 0


def hangman():
    current_word = get_word()
    game_board = generate_board(current_word)
    lifes = 15;
    while (current_word != game_board) and (lifes !=0):

        print(game_board, '\n You have ', str(lifes), ' lifes. Guess a letter:\n')
        guess = input()
        while len(guess) != 1:
            print('Invalid input, guess a SINGLE letter:\n')
            guess = input()
        game_board, life_check = guess_letter(guess, game_board, current_word)

        if life_check == False:
            lifes -= 1
    if lifes == 0:
        print('You lost, try again?(y/n)\n')
    else:
        print('You won, Another round?(y/n)\n')

round = True

while round:
    hangman()
    round = input()
    if round.lower() == 'y':
        round = True
    elif round.lower() == 'n':
        round = False
    else:
        print('Invalid Input')
        round = False
