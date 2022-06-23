
import math
import random
import re

PlayerDeckSize = int(40)
PlayerHandSize = int(5)
CPUDeckSize = int(40)
CPUHandSize = int(5)

Element = ["Fire", "Water", "Snow"]

PlayerCard1Element = random.choice(Element) 
PlayerCard2Element = random.choice(Element)
PlayerCard3Element = random.choice(Element)
PlayerCard4Element = random.choice(Element)
PlayerCard5Element = random.choice(Element)
PlayerCard6Element = random.choice(Element)
PlayerCard7Element = random.choice(Element)

PlayerCard1Strength = random.randint(4,10)
PlayerCard2Strength = random.randint(4,10)
PlayerCard3Strength = random.randint(4,10)
PlayerCard4Strength = random.randint(4,10)
PlayerCard5Strength = random.randint(4,10)
PlayerCard6Strength = random.randint(4,10)
PlayerCard7Strength = random.randint(4,10)

#PlayerCard1 = PlayerCard1Element, + PlayerCard1Strength
#first hand
ViewOrPlay = input("Press H to view your hand or a number to play that card from within your hand.")

if ViewOrPlay.upper() == "H":
    print('Card 1 is : ' +  PlayerCard1Element, +"+" + PlayerCard1Strength)

