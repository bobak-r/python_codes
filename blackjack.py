
from  random import choice

cards = [11,11,11,11, 2,2,2,2,3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10,10,10,10,10,10,10,10, 10,10,10,10,10]

user_cards = []
computer_cards = []

#give computer and user two cards
def deal_card():
    """Returns a random card from the deck."""
    card=choice(cards)
    cards.remove(card)
    return card
    
def start_game():
    
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    
def calculate_score(getcards):
    total=0
    total=sum(getcards)
    if total>22:
        for i in range(len(getcards)):
          if  getcards[i]==11:
              getcards[i]=1
              total=sum(getcards)
              break      
    return total
def computerdecide():
    state=0
    while state==0:
        if calculate_score(computer_cards)>17:
            state=1
            return calculate_score(computer_cards)
        else:
            
            computer_cards.append(deal_card())
                 
def compare():
    print (user_cards)
    
    state=0
    while state==0:
        
        user_action=input("to get another card type hint or want stay type stand  ")
        if user_action=="hint":
            
            user_cards.append(deal_card())
            print(user_cards)
        else:
            state=1
    dec=computerdecide()
    if calculate_score(user_cards)>22:
        print (computer_cards)
        print (user_cards)
        print ("lose")
    elif dec>22:
        print (computer_cards)
        print (user_cards)
        print("win")
    elif dec==21:
        print (computer_cards)
        print (user_cards)
        print("lose")
    elif calculate_score(user_cards)>dec:
        print (computer_cards)
        print (user_cards)
        print("win")
    elif  calculate_score(user_cards)<dec:
        print (computer_cards)
        print (user_cards)
        print("lose")
    if input("do you wnat continue plese Enter y :")=="y":
        user_cards.clear()
        computer_cards.clear()
        start_game()
        compare()
start_game()
compare()
            
    
        
        
        
        
        
        