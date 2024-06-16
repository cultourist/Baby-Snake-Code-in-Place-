from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    dx = 0
    dy = 0
    
    #Create player and set position 
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, 'blue')

    #Create goal and set position
    goal_x = 360
    goal_y = 360
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE, 'salmon')

    direction = 'Right'
    score = 0 

#Animation loop
    #Set Key Press
    while True:
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            direction = 'Left'
        if key == 'ArrowRight':
            direction = 'Right'
        if key == 'ArrowUp':
            direction = 'Up'
        if key == 'ArrowDown':
            direction = 'Down'

        #Updating position of player
        if direction == 'Left':
            dx -= SIZE
        if direction == 'Right':
            dx += SIZE
        if direction == 'Up':
            dy -= SIZE
        if direction == 'Down':
            dy += SIZE

        #Continuous moving of player
        canvas.moveto(player, dx, dy)

        #Detecting collisions with the walls
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        if player_x < 0 or player_x > CANVAS_WIDTH or player_y < 0 or player_y > CANVAS_HEIGHT:
            break
            
        #Moving goal randomly when hit by player
        if player_x == goal_x and player_y == goal_y:
            goal_x = random.randint(0, CANVAS_WIDTH // SIZE - 1) * SIZE
            goal_y = random.randint(0, CANVAS_WIDTH // SIZE - 1) * SIZE
            canvas.moveto(goal, goal_x, goal_y)
            score += 1

        #Show current score in lower left corner
        score_text = canvas.create_text(2, CANVAS_HEIGHT-12, str(score) + " points")

        #Sleep between animation steps
        time.sleep(DELAY)

        #Delete score text when game ends
        canvas.delete(score_text)

    #Display text in middle when game ends
    end_result = "Your score was " + str(score) + "!"
    canvas.create_text(CANVAS_WIDTH/2 - 0.085*CANVAS_WIDTH, CANVAS_HEIGHT/2, "Game Over!", color = 'red')
    canvas.create_text(CANVAS_WIDTH/2 - 0.1*CANVAS_WIDTH, CANVAS_HEIGHT/2+SIZE, end_result, color = 'red')

if __name__ == '__main__':
    main()