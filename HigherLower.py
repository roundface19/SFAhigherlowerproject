import time, os, random
# Imports are the modules needed for this program
ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"] #The lists of are cards from Ace=1 to King=13
suits = ["Clubs","Hearts","Diamonds","Spades"] #The 4 decks of cards
deck = []
#fisrt loop "for rank in ranks: and than an inner loop of for suits in suits:
value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1
#the code for the Scoreboard
random.shuffle(deck)
score = 0
card1 = deck.pop(0)

while True:
    os.system("cls")#if running on Linux it needs to be set to the command clear
    print("You've Guessed Coreectly", score) #you guessed the right answer
    print("\n\nThe Flipped Card is", card1[0]) #identify the card that is flipped
    while True:
        choice = input("Will the card be Higher or Lower?") 
        if len(choice) > 0:
            if choice[0].lower() in ["h","l"]:
                break
        

    card2 = deck.pop(0)
    print("The Next card turned over is", card2[0])
    time.sleep(1)

    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print("You Chose Wisely it was Higher!") #you chose the correct answer
        score +=1
        time.sleep(1)
    if choice[0].lower() == "h" and card2[1] < card1[1]:
        print("Bad hand I'm afraid") #you choose the incorrect answer
        time.sleep(1)
        break
    if choice[0].lower() == "l" and card2[1] < card1[1]:
        print("Great choice, it was indeed Lower!") #you choose lower and were correct
        score +=1
        time.sleep(1)
    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print("I would've chosen Higher that round") #you choose lower and were incorrect 
        time.sleep(1)
        break
    else:
        print("It twas a draw!") #The else is for any other scenario other than Higher or Lower

    card1 = card2

os.system("cls")
print("The Game is Over")
print("The Highest you Guessed was", score)
time.sleep(4)
os.system("cls")
