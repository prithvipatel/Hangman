import random

global_dictionary = {}
global_positions = []


def readfile():
    filename = 'words.txt'
    words = open(filename, "r").readlines()
    return words


def welcome():
    print("Hello! Welcome to HangMan by Prithvi Patel")
    print("If you know how to play the Classic hangman type 'y', if not type 'n':")
    answer = input()

    if answer == 'n' or answer == 'N':
        print("Hangman is a game for 2 or more players but in this case it would be player against computer."
              "Player will guess one word, which the computer has chose with 7 guesses.")

    else:
        pass


def wordassign(word):
    temp = random.randint(0, 3)
    print("The word has been chosen by the computer.")
    return word[temp]


def character_check(fun_char, word):
    if fun_char in word:
        return True
    else:
        return False


def position_checker(character, word):
    positions = []
    for x in range(0, len(word)):
        if character == word[x]:
            positions.append(x)

    return positions


def game(word):
    try_counter = 0
    print_dictionary(global_dictionary, global_positions, word)
    while try_counter < 7:
        character = input(print('\ninput a character'))

        if character_check(character, word):
            positions = position_checker(character, word)

            for x in range(0, len(positions)):
                game_dictionary = {positions[x]: character}
                global_dictionary.update(game_dictionary)
                global_positions.append(positions[x])
            print_dictionary(global_dictionary, global_positions, word)
            if check_win(global_positions, word):
                print("\nCongrats you guessed the word!")
                break
        elif check_win(global_positions, word):
            print("\nCongrats you guessed the word!")
            break

        else:
            print_dictionary(global_dictionary, global_positions, word)
            try_counter += 1
            print('\nIncorrect!' + str(try_counter))


def print_dictionary(gd, pos, word):
    for x in range(0, len(word) - 1):
        if x in pos:
            res = gd.get(x, "")
            print(res, end=" ")
        else:
            print("_", end=" ")


def check_win(pos, word):
    if len(pos) == len(word)-1:
        return True
    else:
        return False


if __name__ == "__main__":
    words = readfile()
    welcome()
    chosenword = wordassign(words)
    game(chosenword)
