rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
name = input("Enter Your Name :\n")
inp = int(input("Pick A Number: 0 for Rock , 1 for Paper OR 2 for Scissors \n"))
if inp<0 or inp>2:
  print("INVALID INPUT YOU LOSE")
else:
  print("Your Choice :")
  if inp==0:
    print("ROCK")
    print(rock)
  elif inp==1:
    print("PAPER")
    print(paper)
  else:
    print("SCISSORS")
    print(scissors)  
  computer=random.randint(0, 2)
  print("Your Enemy Choice :")
  if computer==0:
    print("ROCK")
    print(rock)
  elif computer==1:
    print("PAPER")
    print(paper)
  else:
    print("SCISSORS")
    print(scissors)  
  if inp==computer:
    print("You Are Both EQUAL , Press Run To Play Agin")
  elif inp==0 and computer==2 :
    print("Congratulations "+name+" You Won")
  elif inp==2 and computer==1 :
    print("Congratulations "+name+" You Won")
  elif inp==1 and computer==0 :
    print("Congratulations "+name+" You Won")
  else:
    print(name+" is looser!!")
    


