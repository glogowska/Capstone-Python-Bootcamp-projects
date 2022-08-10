
## There are 2 decks
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.

#This dictionary is used for counting the points for the player and the dealer
cards_points = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K":10,}

#This dictionary is used for 
cards_dictionaries= [ {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K":10,} , {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,} ]
              

## The cards in the list have equal probability of being drawn.
## Cards are removed from the deck as they are drawn.
## The computer is the dealer

##################### Hints #####################

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.



def pick_a_card_throw_it_away(players_or_dealers_cards):
  """This function chooses a random card from two decks of cards, adds the picked card to the players_or_dealers_cards list and removes this card from the two decks, so it cannot be chosen again."""
  random_stack = random.randint(0,1)
    
  random_card = random.choice(list(cards_dictionaries[random_stack]))
  players_or_dealers_cards.append(random_card)
          
  del cards_dictionaries[random_stack][random_card]

def calculate_points(players_or_dealers_cards):
  """This function calculates the points of players_or_dealers_cards - it goes one by one through the cards of said player or dealer - checks the points for a certain card, sums them up and returns the value."""
  players_or_dealers_points = 0
  for card in players_or_dealers_cards:
    if card =="A":
      if players_or_dealers_points + 11 <= 21:
        cards_points[card] = 11
      else:
        cards_points[card] = 1
    players_or_dealers_points += cards_points[card]
  return players_or_dealers_points

def compare_points(points1, points2):
  """Function that compares points and announces(prints) whether player with points1 won, lost or draw with player with points2."""
  if(points2 == points1):
    print("It's a draw.")
  elif(points2 == 21):
    print("You lost.")
  elif(points1>points2):
    print("You won. Yay!")
  elif(points1<points2 and points2 < 21):
    print("You lost.")
  elif(points1<points2 and points2 > 21):
    print("You won. Yay!")


from art import logo
import random
from replit import clear

while True:
  response1 = input("Type 'y' to play BlackJack or 'n' to pass :>\n")
  
  if(response1=='n'):
    print("Goodbye!")
    break
  elif(response1 == 'y'):
    clear()
    print("You are playing with two decks.\n")
    print(logo)
  
    players_cards = []
    players_points = 0
    dealers_cards = []
    dealers_points = 0
  
    #Picking first two cards for the player
    for picks_player in range(2):
      pick_a_card_throw_it_away(players_cards)
      players_points = calculate_points(players_cards)
    print(f"Player's cards: {players_cards}")
    print(f"Player's points: {players_points}")
    
    #Picking first two cards for the dealer
    for picks_dealer in range(2):
      pick_a_card_throw_it_away(dealers_cards)
      dealers_points = calculate_points(dealers_cards)
    dealers_points_preview = cards_points[dealers_cards[0]]  
      
    #print(f"Dealers cards: {dealers_cards}") ##just for testing - to delete later
      
    print(f"Dealer has two cards and the first one is: {dealers_cards[0]}, which is {dealers_points_preview} points.")
    
  
    #print(cards_dictionaries) ##for testing - to delete later
    #loop for the player
    while True:
      if(players_points >= 21):
        break
      next_card = input("Type 'hit' to pick another card and 'stand' to stop.\n")
      if(next_card == 'stand'):
        break
      elif(next_card == "hit"):
        pick_a_card_throw_it_away(players_cards)
        players_points = calculate_points(players_cards) 
        print(f"Player's cards: {players_cards}")
        print(f"Player's points: {players_points}")
      else:
        print("Invalid response.\n")
          
    
    if(players_points >21):
      print("You lost. You have over 21 points.")
    else:
      print("Dealer is playing...")
      random_num_picks = random.randint(0,10)
      for i in range(random_num_picks):
        if(dealers_points >=21):
          break
        pick_a_card_throw_it_away(dealers_cards)
        dealers_points = calculate_points(dealers_cards)
      print(f"Dealers cards: {dealers_cards}")
      print(f"Dealer's points: {dealers_points}")
      
      compare_points(players_points,dealers_points)
  else:
    print("Invalid response. Try again.\n")