
import math
import random

PlayerDeckSize = int(40)
PlayerHandSize = int(5)
CPUDeckSize = int(40)
CPUHandSize = int(5)
TurnCount = int(0)
WinsCount = int(0)
LoseCount = int(0)

Element = ["Fire", "Water", "Snow"]

CPUCard1Element = random.choice(Element) 
CPUCard2Element = random.choice(Element)
CPUCard3Element = random.choice(Element)
CPUCard4Element = random.choice(Element)
CPUCard5Element = random.choice(Element)
CPUCard6Element = random.choice(Element)
CPUCard7Element = random.choice(Element)

CPUCard1Strength = random.randint(4,10)
CPUCard2Strength = random.randint(4,10)
CPUCard3Strength = random.randint(4,10)
CPUCard4Strength = random.randint(4,10)
CPUCard5Strength = random.randint(4,10)
CPUCard6Strength = random.randint(4,10)
CPUCard7Strength = random.randint(4,10)

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
  
def CheckHand():
    print('Card 1 is : ' +  PlayerCard1Element, + PlayerCard1Strength)
    print('Card 2 is : ' +  PlayerCard2Element, + PlayerCard2Strength)
    print('Card 3 is : ' +  PlayerCard3Element, + PlayerCard3Strength)
    print('Card 4 is : ' +  PlayerCard4Element, + PlayerCard4Strength)
    print('Card 5 is : ' +  PlayerCard5Element, + PlayerCard5Strength)
    if PlayerHandSize >= 6:
        print('Card 6 is : ' +  PlayerCard6Element, + PlayerCard6Strength)
        if PlayerHandSize == 7:
            print('Card 7 is : ' +  PlayerCard7Element, + PlayerCard7Strength)

ViewOrPlay = input("Press H to view your hand or a number to play that card from within your hand.")

if ViewOrPlay.upper() == "H":
    CheckHand()

if ViewOrPlay() == "1":
     print('You play : ' +  PlayerCard1Element, + PlayerCard1Strength)
     print('Opponent plays : ' +  CpuCard1Element, + CPUCard1Strength)
     if PlayerCard1Element == "Fire" and CPUCard1Element == "Water":
         LoseHand()
     elif PlayerCard1Element == "Fire" and CPUCard1Element =="Snow":
        Winhand()
     elif PlayerCard1Element == "Fire" and CPUCard1Element =="Fire":
        if PlayerCard1Strength < CPUCard1Strength :
            LoseHand()
        elif PlayerCard1Strength > CPUCard1Strength :
            WinHand()
        else:
            DrawHand()