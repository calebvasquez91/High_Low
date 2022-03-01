#Display art
from art import logo
from game_data import data
import random
from replit import clear


def format_data(account):
  """takes the account data and returns th printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
  """takes the users guess to see if true and compares how many followers each account has"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

"""This is the starting point of the whole code restarting the random picks"""
while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  """This will print the layout of the 2 chosen accounts in a VS standoff"""
  print(f"Compare A: {format_data(account_a)}.")
  print("vs")
  print(f"Compare B: {format_data(account_b)}.")
  #Format the account data into printable form.
  #Ask user for a guess 
  guess = input("who has more followers? type 'a' or 'b': ").lower()
  #Check if user is correct
  ##Ger follower count of each account
  a_follower_account = account_a["follower_count"]
  b_follower_account = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_account, b_follower_account)
  #Give user feedback on their guess
  ##Use if statement to check if user is correct
  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"you are correct, current score {score}")
  else:
    game_should_continue = False
    print(f"you are wrong, final score {score}")


#Score keeping
#Make the game repeatable
#Making account at postiton B become the next account at position A