from random import randint
EASY = 10
DIFFICULT = 5
def check_answer(guess,answer,turns):
  if guess < answer:
    print("Olayel y ba5el")
    return turns - 1
  elif guess > answer:
    print("3aly y basha llasaf")
    return turns - 1 
  else:
    print(f"Shater y sahby... got it! The answer was {answer}.")
def check_diff():
  level = input("Enter 'e' to easy level or 'd' to difficult level : ")
  if level == 'e':
    return EASY
  else:
    return DIFFICULT
def el3ab():
  print("********** Welcome To GUESS THE NUMBER Game **********")
  print("HYKOON LIK/Y 10 ATTEMPTS LAW E5TART/Y EASY W 10 LAW E5TART/Y DIFFICULT : ")
  turns = check_diff()
  answer = randint(1,100)
  guess = 0
  while guess != answer:
    print(f"Rakez Lessa 3andk {turns} attempts remaining to guess the number.")
    guess = int(input("Make a Guess:"))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("5lst mo7awlatak y 7aloof e5la3...")
      return
    elif guess != answer:
      print("Guess again.")
el3ab() 
  

                