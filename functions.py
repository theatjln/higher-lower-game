from random import choice

def pick_2_random_entities(data):
  for _ in range(2):
    if _ == 0:
      CURRENT_WINNER = choice(data)
    if _ == 1:
      CHALLENGER = choice(data)

  return CURRENT_WINNER, CHALLENGER 


def game_opening(CURRENT_WINNER, CHALLENGER, vs):  
  print(f"Compare A: {CURRENT_WINNER['name']}, a {CURRENT_WINNER['description']}, from {CURRENT_WINNER['country']}\n{vs}\nCompare B: {CHALLENGER['name']}, a {CHALLENGER['description']}, from {CHALLENGER['country']}")
  
  choice = ""
  while(choice != 'A' or choice != 'B'):
    choice = input("\nWho has more followers? Type 'A' or 'B':  ").upper()
    if choice == 'A':
      return CURRENT_WINNER
    elif choice == 'B':
      return CHALLENGER
    else: print("You entered an invalid input. Pick again.")

  
def compare_entities(CURRENT_WINNER, CHALLENGER): 
  if CURRENT_WINNER["follower_count"] < CHALLENGER["follower_count"]:
    CURRENT_WINNER = CHALLENGER
  elif CURRENT_WINNER["follower_count"] == CHALLENGER["follower_count"]:
    print("\nequal followers!") 

  return CURRENT_WINNER, CHALLENGER
