#----------- IMPORTING NECESSARY MODULES --------------
import pyray as pr
import random

#---------Initialising a display window with width 750px and height 750px----------------

pr.init_window(750,750,"Snake Game ")

#--------- Setting number of times the game loop should execute per second to create a smooth gameplay ----------------
pr.set_target_fps(20)


# ---------- Function which gets called on when the snake collides with itself or when the snake leaves the boundary -----------
def game_over(score):   
    while (not pr.window_should_close()):
        if pr.is_key_pressed(pr.KEY_R):
            return 
        pr.begin_drawing()
        pr.clear_background(pr.WHITE)

        pr.draw_text("GAME OVER",280,305,30,pr.BLACK)
        pr.draw_text("SCORE : {}".format(score),300,335,25,pr.BLACK)
        pr.draw_text("Press R to Restart ",280,650,25,pr.BLACK)
        pr.draw_text("PRESS ESC TO QUIT ",280,700,25,pr.BLACK)
        pr.end_drawing()
        
    pr.close_window()

#------- Main game ----------------
def game():
    x=20
    y=100

    food_x=random.randrange(20,700,10)
    food_y=random.randrange(20,650,10)

    snake=[(x,y)]

    score=0

    direction='RIGHT'
    
    while (not pr.window_should_close()):
        head=snake[0]
        head_x=head[0]
        head_y=head[1]

        #----------- Checking whether the snake leaves the boundary ---------------
        if head_x < 10 or head_x >740 or head_y < 10 or head_y >650:
            break
        
        #------------ Events handling ----------------------------
        
        ''' Here when a key is pressed , its corresponding direction is stored and according to that
            the snake moves continuously without any futher direction input '''
        
        if pr.is_key_pressed(pr.KEY_RIGHT) and direction!='LEFT':
            direction = "RIGHT"
        elif pr.is_key_pressed(pr.KEY_LEFT) and direction!='RIGHT':
            direction = "LEFT"
        elif pr.is_key_pressed(pr.KEY_UP) and direction!='DOWN':
            direction = "UP"
        elif pr.is_key_pressed(pr.KEY_DOWN) and direction !='UP':
            direction = "DOWN"

        if direction == "RIGHT":
            head_x += 10
        elif direction == "LEFT":
            head_x -= 10
        elif direction == "UP":
            head_y -= 10
        elif direction == "DOWN":
            head_y += 10
        #---------- Checking whether the snake collides with itself or not-----------
            
        ''' If (head_x,head_y) already exists in snake list , it means that the snake's head collides with itself .
            So we execute break statement and come out of game loop and call game_over() to show GAME OVER screen .'''

        ''' If (head_x,head_y) did not exists in snake list , we insert that coordinates to the first and it becomes the new head of the snake
            and pop the tail . As a result the length of the snake remains the same . (ie)(+1 addition and -1 removal )'''
        
        if (head_x, head_y) not in snake:
            snake.insert(0, (head_x, head_y))
            snake.pop()
        else:
            break
        
        pr.begin_drawing()
        
        pr.clear_background(pr.WHITE)
        
        #--------------- DRAWING BOUNDARIES------------------
        pr.draw_line(10,10,740,10,pr.BLACK)
        pr.draw_line(10,10,10,650,pr.BLACK)
        pr.draw_line(740,10,740,650,pr.BLACK)
        pr.draw_line(10,650,740,650,pr.BLACK)

        
        #------- Drawing every part of the snake ----------------
        for i in snake:
            pr.draw_rectangle(i[0],i[1],10,10,pr.RED)

        #---------- Drawing food particle at random coordinates --------
        pr.draw_circle(food_x,food_y,7,pr.GREEN)

        #------ Creating rectangle objects to identify collisions-----------
        snake_rec=pr.Rectangle(head_x,head_y,10,10)
        food_rec=pr.Rectangle(food_x-7,food_y-7,14,14)

        #----- Checking collision between food particle and snake -----------

        ''' Here when the snake collides with food particle we insert a new head into the snake list and do not pop the tail .
            As a result the snake grows...
            When a snake collides with food we incremement the score value by 1 '''
        
        if pr.check_collision_recs(snake_rec,food_rec):
            food_x=random.randrange(20,700,10)
            food_y=random.randrange(20,650,10)
            snake.insert(0,(head_x,head_y))
            score+=1
        #--------- Finally showing the score each frame -------------------
        pr.draw_text("SCORE : {}".format(score),25,700,30,pr.BLACK)
        pr.end_drawing()
        
    return score
    

while not pr.window_should_close():
    score = game()
    game_over(score)

#---- Closing the window -------------
pr.close_window()



