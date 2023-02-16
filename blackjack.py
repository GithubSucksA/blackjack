import random



# Blackjack class game
class Blackjack:
  def __init__(self, dealer_name, player_name, chips):
    self.dealer_name = dealer_name
    self.player_cards = []
    self.player_total = 0
    self.dealer_cards = []
    self.dealer_total = 0
    self.chips = chips
    self.bet = 0

# Draw the initial 2 cards for dealer and player
  def start_game(self):
    print("You have " + str(self.chips) + " chips.")
    self.bet = int(input("How much do you want to bet? "))
    self.player_cards = []
    self.dealer_cards = []
    for i in range(4):
      num = random.randint(2, 14)
      if (num == 12):
        num = 'J'
      elif (num == 13):
        num = 'Q'
      elif (num == 14):
        num = 'K'
      #elif (num == 11):
       # num = input("You drew an ace, please choose between 1 or 11: ")
       # num = int(num)
      if (i % 2 == 0):
        self.player_cards.append(num)
      else: 
        self.dealer_cards.append(num)
    self.get_player_total()
    if (self.player_total == 21):
      self.chips += (int(self.bet * 2.5))
      print("Wow BLACKJACK!! You won " + (str(self.bet * 2.5)))
      return
    self.get_cards()
    self.player_turn()
    self.dealer_turn()

# Get total score of player
  def get_player_total(self):
    self.player_total = 0
    for i in self.player_cards:
      if (i == 'J' or i == 'Q' or i == 'K'):
        self.player_total += 10
      else:
        self.player_total += i

# Get total score of dealer
  def get_dealer_total(self):
    self.dealer_total = 0
    for i in self.dealer_cards:
      if (i == 'J' or i == 'Q' or i == 'K'):
        self.dealer_total += 10
      else:
        self.dealer_total += i

# Display the current cards on table for dealer and player
  def get_cards(self):
    print("Player has: " + str(self.player_cards) + "(score: " + str(self.player_total) + ")")
    print("Dealer has: " + str(self.dealer_cards[1]))

  def get_player_cards(self):
    print("Player has: " + str(self.player_cards) + "(score: " + str(self.player_total) + ")")

  def get_dealer_cards(self):
    print("Dealer has: " + str(self.dealer_cards) + "(score: " + str(self.dealer_total) + ")")

# Player draw a card
  def player_hit(self):
    num = random.randint(2, 14)
    if (num == 12):
        num = 'J'
    elif (num == 13):
      num = 'Q'
    elif (num == 14):
      num = 'K'
    self.player_cards.append(num)
    self.get_player_total()
    self.get_player_cards()

# Dealer draw a card
  def dealer_hit(self):
    num = random.randint(2, 14)
    if (num == 12):
        num = 'J'
    elif (num == 13):
      num = 'Q'
    elif (num == 14):
      num = 'K'
    self.dealer_cards.append(num)
    self.get_dealer_total()
    self.get_dealer_cards()

# Checking if there's an ace that can count for 1 when busted
  def player_busted(self):
    if (11 in self.player_cards):
      index = self.player_cards.index(11)
      game_one.player_cards[index] = 1
      self.get_player_total()
      self.get_player_cards()

  def dealer_busted(self):
    if (11 in self.dealer_cards):
      index = self.dealer_cards.index(11)
      game_one.dealer_cards[index] = 1
      self.get_dealer_total()
      self.get_dealer_cards()

# Ask player if they want to draw
  def player_turn(self):
    additional_card = input("Player, do you want to hit? Enter y or n: ")
    while (additional_card == 'y'):
      self.player_hit()
      if (self.player_total > 21 and 11 not in self.player_cards):
        print("Busted! Dealer won")
        self.chips -= self.bet
        break
      elif(self.player_total > 21 and 11 in self.player_cards):
        self.player_busted() 
      additional_card = input("Player, do you want to hit? Enter y or n: ")

# Dealer draw turn
  def dealer_turn(self):
    self.get_dealer_total()
    self.get_dealer_cards()
    if (self.player_total < 22):
      while (self.dealer_total <= 16):
        self.dealer_hit()
        if (self.dealer_total > 21 and 11 not in self.dealer_cards):
          print("Busted!")
          break
        elif (self.dealer_total > 21 and 11 in self.dealer_cards):
          self.dealer_busted()
      if (self.player_total > self.dealer_total or self.dealer_total > 21 and self.player_total <= 21):
        print("Congratulations! You won!")
        self.chips += self.bet
      elif (self.dealer_total > self.player_total):
        print("The house won.")
        self.chips -= self.bet
      else:
        print("Draw")

game_one = Blackjack("dealer", "player", 100)
game_one.start_game()

continue_playing = True
resume = input("Do you want to play another game? y/n ")
if (resume == 'y'):
  continue_playing = True
else:
  continue_playing = False

while continue_playing:
  if (game_one.chips <= 0):
    print("The fuck you trying to do?")
    break
  game_one.start_game()
  resume = input("Do you want to play another game? y/n ")
  if (resume == 'y'):
    continue_playing = True
  else:
    print("You have " + str(game_one.chips) + " left. Have a nice day.")
    break