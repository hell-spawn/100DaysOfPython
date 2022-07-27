from art import logo
import os
import random 

clear = lambda: os.system('cls||clear')

"""
Do you want to play a game of Blackjack? Type 'y' or 'n':

  Logo

 Your cards: [8, 10], current score: 18
   Computer's first card: 8


Type 'y' to get another card, type 'n' to pass:

Computer's final hand: [8, 8, 10], final score: 26
Opponent went over. You win 😁
Do you want to play a game of Blackjack? Type 'y' or 'n': 


Your cards: [3, 10, 7], current score: 20
   Computer's first card: 8
Type 'y' to get another card, type 'n' to pass: 

 Your final hand: [4, 10, 3, 6], final score: 23
 Computer's final hand: [5, 4, 10], final score: 19
"""


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card



def calculate_score(cards):
  result = 0
  if sum(cards) == 21 and len(cards) == 2:
    return result 
  
  for value in cards:
    result += value
  return result


def play_game():
  clear()
  print(logo)
  player_cards = [deal_card(), deal_card()]
  computer_cards = [deal_card(), deal_card()]
  if calculate_score(player_cards) == 0 or calculate_score(computer_cards) == 0:
    print(f"  Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
    print(f"  Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    result = compare(calculate_score(player_cards), calculate_score(computer_cards))
    print(result)
  else:
    player_cards = deal_player(player_cards, computer_cards) 
    computer_cards = deal_computer(computer_cards, player_cards)
    result = compare(calculate_score(player_cards), calculate_score(computer_cards))
    print(result)


def deal_player(player_cards, computer_cards):
  player_score = calculate_score(player_cards) 
  print(f"  Your cards: {player_cards}, current score: {player_score}")
  print(f"  Computer's first card: {computer_cards[0]}")
  another_card = input(f"Type 'y' to get another card, type 'n' to pass:")
  if another_card == 'y':
    player_cards.append(deal_card())
    if calculate_score(player_cards) < 21:
      deal_player(player_cards, computer_cards)
    else:
      return player_cards
  else:
    return player_cards



def deal_computer(computer_cards, player_cards):
  computer_score = calculate_score(computer_cards)
  player_score = calculate_score(player_cards)
  while player_score < 22 and  computer_score < 21 and computer_score < player_score:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards) 
  print(f"  Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
  print(f"  Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
  return computer_cards
 
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


run_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if run_game.lower() == 'n':
  exit()
else:
  while run_game == 'y':
    play_game()
    run_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  exit()
