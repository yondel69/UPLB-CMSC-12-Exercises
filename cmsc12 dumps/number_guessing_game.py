import random
import time

i = random.randint(1, 100)
print("Welcome to the CMSC 12 Class G Guessing Game!")
print("Guess the number (1-100): ")

guesses = 10
correct_guess = False

while guesses > 0:
    print("You have", guesses, "guesses left.")
    answer = int(input("Your guess: "))

    if answer > i:
        print("Guess lower!: ")
        time.sleep(0.4)
    elif answer < i:
        print("Guess higher!: ")
        time.sleep(0.4)
    else: 
        correct_guess = True
        break
        
    guesses -= 1

if correct_guess:
    print("CONGRATULATIONS!")
    print ("You got the right answer! ")

else: 
    print("The answer is", i,", try again")
