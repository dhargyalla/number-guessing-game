#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
print(logo)

""" return the actual answer """
def secret_number():
  number = random.randint(1,100)
  return number

def guess_number():
  guess = int(input("Make a guess: "))
  return guess

def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return 10
  elif level == "hard":
    return 5
  else:
    print("Invalid input")
    
def check_guess(guess, number):
  if guess == number:
    return "You got it! The answer was {number}."
  elif guess > number:
    return "Too high."
  elif guess < number:
    return "Too low."

def game():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = secret_number()
  print(f"Pssst, the correct answer is {number}")
  attempts = difficulty()
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = guess_number()
  while attempts > 0:
    if guess == number:
      print(f"You got it! The answer was {number}.")
      break
    else:
      attempts -= 1
      print(check_guess(guess, number))
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess = guess_number()
      if attempts == 0:
        print("You've run out of guesses, you lose.")

game()



