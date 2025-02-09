import random
rock='🪨'
paper='📃'
scissors='✂️'
game_image=[rock,paper,scissors]

user=int(input("Please choose your fighter 0 for Rock 1 for Paper 2 For Scissors: \n"))

computer= random.randint(0,2)
if user>=3 or user<0:
    print("invalid choice you loose.")
else:
    img=game_image[computer]
    user_img=game_image[user]
    print(f"The computer Chose{img}")
    print(f"The User Chose{user_img}")

    if computer==user:
        print("It's a Draw")
    elif computer==0 and user==2:
        print("computer won")
    elif computer==2 and user==0:
        print("user won")    
    elif computer>user:
        print("Computer Won")
    elif user>computer:
        print("User Won")    
    elif computer==0 and user==1:
        print("User won")



# if computer==0 and user==1:
#     print("User Won")
# elif computer==0 and user==2:
#     print("Computer Won")    
# elif computer==1 and user==0:
#     print("Computer Won")   
# elif computer==1 and user==2:
#     print("User Won") 
# elif computer==2 and user==0:
#     print("User Won")   
# elif computer==2 and user==1:
#     print("Computer Won")   
# elif computer==user:
#     print("Draw")    