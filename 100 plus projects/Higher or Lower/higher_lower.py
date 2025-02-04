import art
import data

replay = True
first_limit = 1
second_limit = 2
score = 0
while replay == True:
    print(art.logo)
    if score > 0:
        print(f"You are right. Your current Score is {score}")
    first_statement = data.data[first_limit]
    print(f"{first_statement['name']} is a {first_statement['description']}")
    print(art.vs)
    second_statement = data.data[second_limit]
    print(f"{second_statement['name']} is a {second_statement['description']}")
    higher_or_lower = input(f"Who has more followers? Press A for {first_statement['name']} or Press B for {second_statement['name']}\n").lower()
    if higher_or_lower == 'a':
       if second_statement['follower_count'] > first_statement['follower_count']:  
           print("You are right")
           score = +1
           first_limit +=1                                                         
           second_limit +=1                                                        
           replay = True                                                          
           print("\n"*40)
       elif second_statement['follower_count'] < first_statement['follower_count']: 
           print("Wrong Guess")                                                    
           replay = False  
           print(art.lose)
           break           
    if higher_or_lower == 'b':
         if second_statement['follower_count'] < first_statement['follower_count']:
             score = +1
             first_limit +=1
             second_limit +=1
             replay = True
             print("\n"*40)  
         elif second_statement['follower_count'] > first_statement['follower_count']:
             print("Wrong Guess")
             replay = False
             print(art.lose)
             break
