import card
import player

# derp
def setupCards():
   copper = card.Card("Copper", "Treasure")
   estate = card.Card("Estate", "Victory")
   cards = {'Copper' : copper, 'Estate' : estate}

# this is junk for fun   
def playerTurn(plyr):
   print(plyr.player_name,"'s turn!", sep='')
   
   action = input('What do you do? (BE = Buy Estate, P = Pass Turn, Q = Quit Game): ')
   if (action == "BE"):
      print("You buy an estate!")
   elif (action == "BC"):
      print("You buy a copper!")
   elif (action == "P"):
      print("you chose P!")
   elif (action == "Q"):
      return False
   else:
      print("Invalid Input")
   return True

# more junk
def gameloop():
   loop = True
   cards = setupCards()
   # Only allows one player
   userInput = input('Let\'s play PyDom! Enter your name: ')
   # Does no checking on input
   plyr1 = player.Player(userInput)
   
   while loop:
      loop = playerTurn(plyr1)
   
   print("Game Over!")
      

if __name__ == "__main__":
   gameloop()

