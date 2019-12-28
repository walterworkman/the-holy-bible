#Imports
import random
from random import seed
from random import randint

#Welcome text
print("Welcome to Rock, Paper, Scissors against your computer! Best 2 out of 3.")
print("To play, type Rock, Paper, or Scissors.")

#Defining functions
def base_1():
    i = 0
    sum = 0
    while (i >= 0):
        i = i + 1
        rounds = i
        t = ["Rock", "Paper", "Scissors"]
        computer_hand = t[randint(0,2)]
        their_hand = str(input())
        if their_hand == "Rock":
            if computer_hand == "Rock":
                print("You both said Rock. Tie!")
                base_1()
            elif computer_hand == "Paper":
                print("You said Rock, They said Paper. You lose round 1!)
                base_lose()
            elif computer_hand == "Scissors":
                print("You said Rock, They said Scissors. You win round 1")
                base_win()
            else:
                print("Bad input, check spelling and try again")
                base_1()
        elif their_hand == "Paper":
            if computer_hand == "Rock":
                print("You said Paper, They said Rock. You win round 1")
                base_win()
            elif computer_hand == "Paper":
                print("You both said Paper. Tie!")
                base_1()
            elif computer_hand == "Scissors":
                print("You said Paper, They said Scissors. You lose round 1")
                base_lose()
            else:
                print("Bad input, check spelling and try again")
                base_1()
        elif their_hand == "Scissors":
            if computer_hand == "Rock":
                print("You said scissors, They said Rock. You lose round 1")
                base_lose()
            elif computer_hand == "Paper":
                print("You said Scissors, They said Paper. You win round 1")
                base_win()
            elif computer_hand == "Scissors":
                print("You Both said Scissors. Tie!")
                base_1()
            else:
                print("Bad input, check spelling/capitals and try again")
                base_1()
        else:
                print("Bad input, check spelling/capitals and try again")
                base_1()

#This function runs if the player wins first
def base_win():
    their_hand = str(input())
    t = ["Rock", "Paper", "Scissors"]
    computer_hand = t[randint(0,2)]
    if their_hand == "Rock":
        if computer_hand == "Rock":
            print("You both said Rock. Tie!")
            base_win()
        elif computer_hand == "Paper":
            print("You said Rock, They said Paper. You lose round 2!")
            print("You are now tied with the computer.")
            base_win_loss()
        elif computer_hand == "Scissors":
            print("You said Rock, They said Scissors. You win round 2!")
            print("Congratulations, you win Rock, Paper, Scissors against your computer!")
        else:
            print("Bad input, check spelling and try again")
            base_win()
    elif their_hand == "Paper":
        if computer_hand == "Rock":
            print("You said Paper, They said Rock. You win round 2!")
            print("Congratulations, you win Rock, Paper, Scissors against your computer!")
        elif computer_hand == "Paper":
            print("You both said Paper. Tie!")
            base_win()
        elif computer_hand == "Scissors":
            print("You said Paper, They said Scissors. You lose round 2!")
            print("You are now tied with your computer.")
            base_win_loss()
        else:
            print("Bad input, check spelling and try again")
            base_win()
    elif their_hand == "Scissors":
        if computer_hand == "Rock":
            print("You said scissors, They said Rock. You lose round 2!")
            print("You are now tied with your computer.")
            base_win_loss()
        elif computer_hand == "Paper":
            print("You said Scissors, They said Paper. You win round 2!")
            print("Congratulations, you win Rock, Paper, Scissors against your computer!")
        elif computer_hand == "Scissors":
            print("You Both said Scissors. Tie!")
            base_win()
        else:
            print("Bad input, check spelling/capitals and try again")
            base_win()
    else:
        print("Bad input, check spelling/capitals and try again")
        base_win()

#This function runs if the player loses first
def base_lose():
    their_hand = str(input())
    t = ["Rock", "Paper", "Scissors"]
    computer_hand = t[randint(0,2)]
    if their_hand == "Rock":
        if computer_hand == "Rock":
            print("You both said Rock. Tie!")
            base_lose()
        elif computer_hand == "Paper":
            print("You said Rock, They said Paper. You lose round 2!")
            print("Sorry, you lost Rock, Paper, Scissors agianst your computer. Try Again!")
        elif computer_hand == "Scissors":
            print("You said Rock, They said Scissors. You win round 2!")
            print("You are now tied with your computer.")

            base_win_loss()
        else:
            print("Bad input, check spelling and try again")
            base_lose()
    elif their_hand == "Paper":
        if computer_hand == "Rock":
            print("You said Paper, They said Rock. You win round 2!")
            print("You are now tied with your computer.")
            base_win_loss()
        elif computer_hand == "Paper":
            print("You both said Paper. Tie!")
            base_lose()
        elif computer_hand == "Scissors":
            print("You said Paper, They said Scissors. You lose round 2!")
            print("Sorry, you lost Rock, Paper, Scissors agianst your computer. Try Again!")
        else:
            print("Bad input, check spelling and try again")
            base_lose()
    elif their_hand == "Scissors":
        if computer_hand == "Rock":
            print("You said scissors, They said Rock. You lose round 2!")
            print("Sorry, you lost Rock, Paper, Scissors agianst your computer. Try Again!")
        elif computer_hand == "Paper":
            print("You said Scissors, They said Paper. You win round 2!")
            print("You are now tied with your computer.")
            base_win_loss()
        elif computer_hand == "Scissors":
            print("You Both said Scissors. Tie!")
            base_lose()
        else:
            print("Bad input, check spelling/capitals and try again")
            base_lose()
    else:
        print("Bad input, check spelling/capitals and try again")
        base_lose()


#This function runs if its one to one
def base_win_loss():
    their_hand = str(input())
    t = ["Rock", "Paper", "Scissors"]
    computer_hand = t[randint(0,2)]
    if their_hand == "Rock":
        if computer_hand == "Rock":
            print("You both said Rock. Tie!")
            base_win_loss()
        elif computer_hand == "Paper":
            print("You said Rock, They said Paper. You lose!")
            print("Sorry, you lost Rock, Paper, Scissors agianst your computer. Try Again!")
        elif computer_hand == "Scissors":
            print("You said Rock, They said Scissors. You win!")
            print("Congratulations, you win Rock, Paper, Scissors against your computer!")
        else:
            print("Bad input, check spelling and try again")
            base_win_loss()
    elif their_hand == "Paper":
        if computer_hand == "Rock":
            print("You said Paper, They said Rock. You win!")
            print("Congratulations, you win Rock, Paper, Scissors against your computer!")
        elif computer_hand == "Paper":
            print("You both said Paper. Tie!")
            base_win_loss()
        elif computer_hand == "Scissors":
            print("You said Paper, They said Scissors. You lose!")
            print("Sorry, you lost Rock, Paper, Scissors agianst your computer. Try Again!")
        else:
            print("Bad input, check spelling and try again")
            base_win_loss()
    elif their_hand == "Scissors":
        if computer_hand == "Rock":
            print("You said scissors, They said Rock. You lose!")
            print("Sorry, you lost Rock, Paper, Scissors agianst your computer. Try Again!")
        elif computer_hand == "Paper":
            print("You said Scissors, They said Paper. You win!")
            print("Congratulations, you win Rock, Paper, Scissors against your computer!")
        elif computer_hand == "Scissors":
            print("You Both said Scissors. Tie!")
            base_win_loss()
        else:
            print("Bad input, check spelling/capitals and try again")
            base_win_loss()
    else:
        print("Bad input, check spelling/capitals and try again")
        base_win_loss()



#Running functions
base_1()
