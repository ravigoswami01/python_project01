"""
case 
A - rock
rock - rock = tid
rock - paper = paper is win
rock - scissor = rock is  win 
case -B
paper - paper= tid
paper - rock = paper win 
paper - scissor = scissor win 

Case - c
scissor - scissor = tid
scissor - rock =  rock win 
scissor - paper = scissor win 

input taken by User 

"""
import random
item_list = ["rock","paper", "scissor"]

User_chosse = input("enter your move Rock , Paper , scissor =")
Computer_chosse = random.choice(item_list)

print(f"your chosse is ={User_chosse}, Computer chosse is ={Computer_chosse}")


if User_chosse == Computer_chosse:
    print("both choose Same : match Tid")

elif  User_chosse == "Rock":
    if Computer_chosse == "Paper":
        print("paper cover rock = Computer Win!")
    else:
        print("Rock Smashes Scissor = You Win!")

elif User_chosse == "Paper":
    if Computer_chosse == "Scissor":
        print("scissor cut Paper = Compute Win!")
    else:
        print("paper cover Rock = You Win!")
elif User_chosse == "Scissor":
    if Computer_chosse == "Paper":
        print("Scissor cut the paper = You Win!")
    else:
        print("rock brock the Scissor = Computer Win!")        
        