import random
#gameStart=False

# if input="rock" 
choice = input ("rock " " paper" " or scissors: ").lower()
print("You choosed:", choice)
list = ["rock" "paper" "scissors"]

# if choice not in list:
  # print ("Not a valid answer. Choose rock, paper, or scissors")



while choice not in list:
  choice = input("Choose from the list").lower()
  
  # choice = input("Choose from list: " + str(options) + "").lower()
   # if choice != ("rock" or "paper" or "scissors")


