logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
from replit import clear
mazaddd = {}
print(logo)
def get_maxbid(dic):
  max = 0
  for bids in dic:
    amount = dic[bids]
    if amount > max:
      max = amount
      winner = bids
  print(f"{winner} is the highest bid of {max}$")
continue_mazad = True
while(continue_mazad):
  name = input("Enter Your Name:\n")
  bid = int(input ("Enter Your Bid:\n"))
  mazaddd[name] = bid
  cond = input ("Do You Want To Add More Bidders? (y/n)\n")
  if cond.lower() == "n": 
    continue_mazad = False
  else:
    clear()
get_maxbid(mazaddd)