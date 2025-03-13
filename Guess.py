import random

secret_number = random.randint(1,100)
guesses = 0

while True:
 try:
 number = int(input("Guess the number between 1 and 100: "))
 guesses += 1
 if number == secret_number:
 print(f"You guessed the correct number in {guesses} guesses!")
 break
 elif number > secret_number:
 print("Try guessing a lower number.")
 else:
 print("Try guessing a higher number.")
 except ValueError:
 print("Please enter a valid integer.")
