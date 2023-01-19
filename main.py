import random
#gameStart=False

# if input="rock" 
# choose = input ("Choose one: "  "rock " " paper" " or scissors: ").lower()
# print("You choosed:", choose)
# input_validation = False
# list = [("rock"), ("paper"), ("scissors")]
# computer = random.choice(list)
# print("Computer choosed:", computer)
# user_input_int = int(user_input)
number = input ("How many times do you want to play? ").lower()
number_input_int = ''
try:
    number_input_int = int(number)
    print(f"your input has the datatype'{type(number_input_int)}'")
# except ValueError:
    # print(f"You didn't enter Rock, Paper, or Scissors, the input data type is '{type(number_input_int)}'")



# def rock():
    for loop in range(number_input_int):
      choose = input ("Choose one: "  "rock " " paper" " or scissors: ").lower()
    print("You choosed:", choose)
    #input_validation = False
    list = [("rock"), ("paper"), ("scissors")]
    computer = random.choice(list)
    print("Computer choosed:", computer)
    
  
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
    
    if choose == "paper" and computer == "rock":
      print ("You win")
    elif choose == "paper" and computer == "scissors":
      print ("You loose")
    elif choose == "paper" and computer == "paper":
      print ("Try again")
    
except ValueError:
    print(f"You didn't enter Rock, Paper, or Scissors, the input data type is '{type(number_input_int)}'")  
  

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


