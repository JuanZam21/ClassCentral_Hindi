# Imports and logo
import random
from replit import clear 
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# FUCTIONS
# Cards picker 
def dealCards(cards):
    return random.choices(cards, k=2)

# Calculate score
def calculateScore(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    if score > 21 and 11 in cards:
       cards.remove(11)
       cards.append(1)
    return score

# Compare fuction
def compare(userScore, computerScore):
  if userScore > 21 and computerScore > 21:
    return "You went over. You lose 😤"
  if userScore == computerScore:
    return "Draw"
  elif computerScore == 0:
    return "Lose, opponent has blackjack"
  elif userScore == 0:
    return "Win with a blackjack"
  elif userScore > 21:
    return "You went over. You lose"
  elif computerScore > 21:
    return "Opponent went over. You win"
  elif userScore > computerScore:
    return "You win"
  else:
    return "Computer wins"
    
# Game fuction
def blackjack():
  print(logo)
  endGame = False
  userCards = dealCards(cards)
  computerCards = dealCards(cards)
  
  while not endGame: 
    userScore = calculateScore(userCards)
    computerScore = calculateScore(computerCards)
        
  # Game start  
    print(f"{userCards} Your current score is: {userScore}")
    print(f"Computer first card: {computerCards[0]}")
    if userScore == 0 or computerScore == 0 or userScore > 21:
      endGame = True
    else:
      if input("Type 'y' to get another card, type 'n' to end game: ").lower() == "y":
        userCards.append(random.choices(cards, k=1)[0])
      else:
        endGame = True
  while computerScore != 0 and computerScore < 17:
    computerCards.append(random.choices(cards, k=1)[0])
    computerScore = calculateScore(computerCards)
  
  print(f" Your final hand: {userCards}, final score {userScore}")
  print(f" Computer's final hand: {computerCards}, final score {computerScore}")
  print(compare(userScore, computerScore))

# Start
while input("Do you want to play blackjack game, type 'y' or 'n': ").lower() == "y":
  clear()
  blackjack()
