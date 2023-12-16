"""
this game of rock paper scissors only gives you 3 trys even if you played wrong ,there was a tie etc...
what i want to do with this code is to make sure that  who gets the most of  3 rounds wins win the game 
so i need to make the game to keep runnig until that happens ...THERE IS A SOLUTION I JUST WANT TO FIND IT...
"""
import random


i =0
while i<3:
    def get_choice():
        player_choice = input("enter ur choice (rock, paper, scissors): ")
        options =["rock","paper","scissors"]
        computer_choice = random.choice(options)
        choices={"player":player_choice,"computer":computer_choice}
        print(f"player chose {player_choice} and computer chose {computer_choice}")


        return choices
    
    def check_win(player,computer):
        if player==computer:
             return "tie"  
        elif player == "rock":
            if computer == "paper":
                return "computer win"
            else:
                return "player win"
        elif player== "paper":
            if computer == "rock":
                return "player win"
            else:
                return "computer win"
        elif player == "scissors":
            if computer =="rock":
                return "computer win"
            else:
                return "player win"
        else:
        
            return "invalid choice"
        
    def final():
        ch=get_choice()
        result=check_win(ch["player"],ch["computer"])
        return result

    x=final()
    print(x)

    i +=1
    

   



    
