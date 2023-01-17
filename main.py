import random
#gameStart=False

# if input="rock" 
choose = input ("Choose one: "  "rock " " paper" " or scissors: ").lower()
print("You choosed:", choose)
list = [("rock"), ("paper"), ("scissors")]
computer = random.choice(list)
print("Computer choosed:", computer)

# def rock(): 
if choose == "rock" and computer == "scissors":
  print ("You win")
elif choose == "rock" and computer == "paper":
  print ("You loose")
elif choose == "rock" and computer == "rock":
  print ("Try again")

if choose == "scissors" and computer == "paper":
  print("You win")
elif choose == "scissors" and computer == "rock":
  print ("You loose")
elif choose == "scissors" and computer == "scissors":
  print ("Try again")
  
  
  

# # if player picks rock, paper, or scissors the computer picks a different variable to play against to see who wins. 
# Rock bets scissors
# scissors bets paper
# paper bets rock

# if choice = rock 

# if choice not in list:
  # print ("Not a valid answer. Choose rock, paper, or scissors")



# while choice not in list:
  # choice = input("Choose from the list").lower()



  
  
  # choice = input("Choose from list: " + str(choose) + "").lower()
   # if choice != ("rock" or "paper" or "scissors")


