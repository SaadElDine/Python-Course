def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def square_move():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move() 
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()  
def hurdle2():
    while not at_goal() :
        jump()
def hurdle3():
        while not at_goal():
            if wall_in_front():
                jump()
            else:
                move()
def maze_escape():
    while front_is_clear():
        move()
    turn_left()
    while not at_goal():
        if right_is_clear():
            turn_right
            move()
            
        elif front_is_clear():   
            move()
        else:
            turn_left()
maze_escape()            
                
            
    
        
        
    
    

   
    
    

    