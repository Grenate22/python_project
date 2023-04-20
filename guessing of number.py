# guessing of number i want my user to guess a number between 1-20 with just a limit of 5 guess
guess_number = 13
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
while guess != guess_number:
    if guess_count < guess_limit:
        guess = int(input("Guess a number between 1 to 20: "))
        if guess < guess_number:
            print("your guess is lesser than the number \nTry a higher number ")
        elif guess > guess_number:
            print("your guess is higher than the number \nTry a lower number ")
        guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("You loose the game")
else:
    print("You win the game")
