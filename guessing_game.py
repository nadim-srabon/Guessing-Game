from random import randint

randomNumber = randint(1, 20)

while True:
    guessNumber = int(input("Enter your guess (between 1 and 20): "))

    if guessNumber == randomNumber:
        print("Congratulations! You guessed the right number.")
        break
    elif guessNumber > randomNumber:
        print("You guessed too high. Try again.")
    else:
        print("You guessed too low. Try again.")
