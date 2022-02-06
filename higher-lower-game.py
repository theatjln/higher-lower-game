# from replit import clear #uncomment
from random import choice
from game_data import data 
from art import logo, vs
from functions import pick_2_random_entities, game_opening, compare_entities

CURRENT_SCORE = 0

def higher_lower_game(CURRENT_SCORE, CHALLENGER = {}):
  CURRENT_WINNER = {}

  # Pick 2 Entities, pick 1 and store as the CURRENT_WINNER and the other as CHALLENGER    
  CURRENT_WINNER, CHALLENGER = pick_2_random_entities(data)
  # print(f"CURRENT_WINNER: {CURRENT_WINNER}\n\nCHALLENGER: {CHALLENGER}") #comment 


  # Display {Entity 1, Vs, Entity 2}, ask user who's have higher followers and store user's answer in a variable
  user_choice = game_opening(CURRENT_WINNER, CHALLENGER, vs)


  # Find who has more followers and store the persons data into the variable CURRENT_WINNER
  CURRENT_WINNER, CHALLENGER = compare_entities(CURRENT_WINNER, CHALLENGER)


  # compare the followers of CURRENT_WINNER and user_choice if the same
  def check_user_choice(CURRENT_SCORE):    
    # if the same,
    #    accumulate CURRENT_SCORE, 
    #    display confirmation and current score, 
    #    pick another Entity to compare and store as CHALLENGER, 
    #    re-run the game using updated CURRENT_SCORE and CHALLENGER as parameters
    if CURRENT_WINNER["follower_count"] == user_choice["follower_count"]:
      clearConsole() #delete
      # clear() #uncomment
      print(logo)

      # print(f"\nCURRENT_WINNER: {CURRENT_WINNER}") #comment
      CURRENT_SCORE += 1
      print(f"\nYou\'re right! Corrent score: {CURRENT_SCORE}")
      CHALLENGER = choice(data)
      higher_lower_game(CURRENT_SCORE, CHALLENGER)

    # if not the same, 
    #   clear the console screen, 
    #   print logo
    #   display regret and the final score
    #   clear the player's current score stop game
    else:  
      # clear() #uncomment
      clearConsole() #delete
      print(logo)
      # print(f"\nCURRENT_WINNER: {CURRENT_WINNER}") #comment
      print(f"\nSorry, that's wrong. Final score: {CURRENT_SCORE}")
      CURRENT_SCORE = 0

  CURRENT_SCORE = check_user_choice(CURRENT_SCORE)

# clear console 
# clear() #uncomment

import os
def clearConsole(): #delete
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
      command = 'cls'
  os.system(command)  

clearConsole() #delete
print(logo)
higher_lower_game(CURRENT_SCORE)