from random import randint
import time

WIDTH = 800
HEIGHT = 600
CENTER = (400,300)
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
FONT_COLOR = (127, 255, 0)
game_over = False
movement = False

blue_ball = Actor("blue-ball")
blue_ball.pos = CENTER


score1 = 0
score2 = 0

hi = Actor("hi")
hi.pos = 20, 300
hi2 = Actor("hi2")
hi2.pos = 780, 300

ball_list = []
blue_ball_vy = 5
blue_ball_vx = 5


def draw():
    screen.clear()
    screen.blit("background", (-700,-300))
   
    
    blue_ball.draw()
    
    screen.draw.text("PINGPONG", fontsize = 70, color = FONT_COLOR, center = (400,30))
    
    hi.draw()
    hi2.draw()

    screen.draw.text(
            "RED SCORE: " +
            str(score1),
            topleft = (10, 10), color = FONT_COLOR)
    screen.draw.text(
            "BLUE SCORE: " +
            str(score2),
            topleft = (650, 10), color = FONT_COLOR)
    
    if score1 == 3:
        screen.clear()
        screen.draw.text("RED PLAYER WINS!", center = (400,300), color = FONT_COLOR,fontsize = 80)
        time.sleep(2)
        
    if score2 == 3:
        screen.clear()
        screen.draw.text("BLUE PLAYER WINS!", center = (400,300), color = FONT_COLOR, fontsize = 80)
        time.sleep(2)
        



def update_ball():
   
    global blue_ball_vy, blue_ball_vx
    global score1, score2
    
    
    blue_ball.x = blue_ball.x + blue_ball_vx
    blue_ball.y = blue_ball.y + blue_ball_vy

    if blue_ball.left < 0:
        score2 = score2 + 1
        blue_ball.x = 400
        blue_ball.y = 300
        time.sleep(2)
        blue_ball_vy = 5
        blue_ball_vx = 5
    if blue_ball.right > WIDTH:
        score1 = score1 + 1
        blue_ball.x = 400
        blue_ball.y = 300
        time.sleep(2)
        blue_ball_vy = 5
        blue_ball_vx = 5
    if blue_ball.top < 0:
        blue_ball_vy = -blue_ball_vy
    if blue_ball.bottom > HEIGHT:
        blue_ball_vy = -blue_ball_vy
        
    if blue_ball.colliderect(hi):
        blue_ball_vx = -blue_ball_vx
    if blue_ball.colliderect(hi2):
        blue_ball_vx = -blue_ball_vx
    
    
         

    return


def velocity():
    global blue_ball_vx, blue_ball_vy
    if blue_ball.colliderect(hi) or blue_ball.colliderect(hi2):
       blue_ball_vy = blue_ball_vy + 0.6
       blue_ball_vx = blue_ball_vx + 0.6
    




def update():
    global game_over
    if not game_over:
        if keyboard.up:
            hi.y -= 4
        elif keyboard.down:
            hi.y += 4
        elif keyboard.w:
            hi2.y -= 4
        elif keyboard.s:
            hi2.y += 4

    update_ball()
    velocity()




        
