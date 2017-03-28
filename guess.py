# Nicole Kyriakopoulos
# nkyriako@ucsc.edu
# programming assignment 1
# Player has 3 chances to guess a randomly generated number from 1 to 10

def _startgame():
  print("I'm thinking of an integer, you have three guesses.")
  import random
  rnumber = random.randint(1, 10)
  #first_guess first guessed number
  first_guess = eval(input("Guess 1: Please enter an integer between 1 and 10: "))  
  # guess 1 correct
  if rnumber == first_guess:
    print("You got it!") 
  # guess 1 too high
  if rnumber < first_guess:
    print("Your guess is too big.")
    sec_guess = eval(input("Guess 2: Please enter an integer between 1 and 10: "))
  #guess 2, variable sec_guess correct
    if rnumber == sec_guess:
      print("You got it!") 
  #guess 2 too high  
    if rnumber < sec_guess:
      print("Your guess is too big.")
      third_guess = eval(input("Guess 3: Please enter an integer between 1 and 10: "))
  #guess 3 correct     
      if rnumber == third_guess:
        print("You got it!") 
  #guess 3 incorrect   
      if rnumber != third_guess:
        print("Too bad. The number is: ", rnumber)	
  # guess 2 too low 
    if rnumber > sec_guess:
      print("Your guess is too small.")
      third_guess = eval(input("Guess 3: Please enter an integer between 1 and 10: "))
      if rnumber == third_guess:
        print("You got it!") 
      if rnumber != third_guess:
        print("Too bad. The number is: ", rnumber)
  #guess 1 too low
  if rnumber > first_guess:
    print("Your guess is too small.")  
    sec_guess = eval(input("Guess 2: Please enter an integer between 1 and 10: "))
  #guess 2 correct 
    if rnumber == sec_guess:
      print("You got it!") 
  #guess 2 too high
    if rnumber < sec_guess:
      print("Your guess is too big.")
      third_guess = eval(input("Guess 3: Please enter an integer between 1 and 10: "))
  #guess 3 correct
      if rnumber == third_guess:
        print("You got it!") 
  #guess 3 incorrect
      if rnumber != third_guess:
        print("Too bad. The number is: ", rnumber)	
  #guess 2 too small
    if rnumber > sec_guess:
      print("Your guess is too small.")	
      third_guess = eval(input("Guess 3: Please enter an integer between 1 and 10: "))
  #guess 3 correct
      if rnumber == third_guess:
        print("You got it!")  
  #guess 3 incorrect 
      if rnumber != third_guess:
        print("Too bad. The number is: ", rnumber)

_startgame()
