# 1A2B Game Desgin
from random import shuffle

def pick_target(SIZE):
    digits = [str(x) for x in range(10)]
    shuffle(digits)
    target = digits[:4]
    return target

def take_user_ip(SIZE):
    guess_str = input("Enter a", SIZE, "digit number: ")
    guess = list(guess_str)
    return guess

def check_guess(target, guess, SIZE):
    x = y = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if target[i] == guess[j]:
                if i == j:
                    x += 1
                else:
                    y += 1
    return x, y

def player_won(x, y, SIZE):
    if x == SIZE:
        return True
    else:
        return False

def game(SIZE):
    ''' Main game logic
    '''
    target = pick_target(SIZE)
    while True:
        guess = take_user_ip(SIZE)
        x, y = check_guess(target, guess)
        print(x, "A", y, "B")
        if player_won(x, y, SIZE):
            print("You WON!")
            break

if __name__ == "__main__":
    SIZE = 4
    game()
