import random
secretnumber=random.randint(1, 20)
print("i'm thinking of a number between 1 and 20")
for guessestaken in range(1,6):
    print('take a guess: ')
    guess=float(input())

    if guess<secretnumber:
        print('your guess is too low')
    elif guess>secretnumber:
        print('your guess is too high')
    else:
        break
if guess == secretnumber:
    print('good job! you guess my number right in ' + str(guessestaken) +' guesses')
else:
    print('nope the number i was thinking of was ' +str(secretnumber))
