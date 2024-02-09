import random

cap = input("Type a number: ")

# ensuring the user types an integer and not a string representation of a number ("one" vs "1", "1" -> 1, "one" --> error)
# checking if input is a digit
if cap.isdigit():
    cap = int(cap)
    # the number has to be greater than 0
    if cap <= 0:
        print('Provide a number larger than 0 next time.')
        quit()
# if it's not a digit let the user knwo and quit the game
else:
    print('Not a number, type in a number next time.')
    quit()

random_number = random.randint(0, cap) # (lower bound and upper bound)
# guess tracker
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Type in a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        # stop running once the user guesses correctly
        break
    elif user_guess > random_number:
        print("You were above the number.")
    else:
        print("You were below the number.")

print(f"Took you {guesses} tries.")