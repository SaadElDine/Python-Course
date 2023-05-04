from  data import data
import random 
from art import vs
from art import logo

def randomdata():
  return random.choice(data)

def formulate(haga):
  name = haga["name"]
  description = haga["description"]
  country = haga["country"]
  return f"{name},a {description}, from {country}."

def check(answer,chooseA,chooseB):
  if chooseA > chooseB:
    return answer == 'a'
  else:
    return answer == 'b'
    
def kasban(a,b):
  if a["follower_count"] > b["follower_count"]:
    return a
  else:
    return b
    
def game():
  print(logo)
  randomA = randomdata()
  randomB = randomdata()
  continuegame = True
  score = 0
  while continuegame:
    print(formulate(randomA))
    print(vs)
    print(formulate(randomB))
    answer = input("Choose 'a' OR 'b': ")
    if not check(answer,randomA["follower_count"],randomB["follower_count"]):
      print(f"Your SCORE Is {score}")
      print("GAME OVER !")
      continuegame = False
    else:
      score = score + 1
      randomA = kasban(randomA,randomB)
      randomB = randomdata()
      print(" ")
      print("___________________________________________________________________________________________________________________")
      print(" ")
game()  
  