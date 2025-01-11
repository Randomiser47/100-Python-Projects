def turn_right():
    turn_left()
    turn_left()
    turn_left()


def new_wall_logic():
    if wall_in_front() == True:
        turn_left()
    elif wall_in_front() ==False:
        move()
        turn_right()
    
    
while not at_goal():   
    new_wall_logic()

    
