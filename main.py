import pygame
import random
import math
import numpy
# inittilize the pygame
pygame.init() 
screen=pygame.display.set_mode((800,533))
##background image
background=pygame.image.load('space_background.jpg')

#Title and icon
pygame.display.set_caption("Space Invader Game by Saquib Anjum")

icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
# player image
playerImg=pygame.image.load('player.png')
playerX = 370
playerY = 455
playerX_change =0

#for the enemy
enemyImg=[]
enemyX=[]
enemyY = []
num_of_enemy=15
enemyX_change=[]
enemyY_change=[]
for i in range(num_of_enemy):

    enemyImg=pygame.image.load('enemy.png')
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append((0.3))
    enemyY_change.append((40))
#for bullet

bulletImg=pygame.image.load('bullet.png')
bulletX =0
bulletY =450
bulletX_change =0
bulletY_change=  .9
#ready state means we can not see the bullet
#fire state means bullet is moving know
bullet_state="ready"
score=0

#score
score_value= 0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
testY=10
def show_score(x,y):
    score = font.render("score :" + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


def player(x,y):
    screen.blit(playerImg,(x,y))


def enemy(x,y,i):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16, y+10))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    
    distance=math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance <27:
        return True
    else:
        return False
# it is something that will stay continue
running = True
while running:
    #this is for rgb color ke liye
    screen.fill((0,0, 0))
    #here is background
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
        #if keystroke is prassed check wether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
                
            if event.key == pygame.K_RIGHT:
                playerX_change =1
            #logic for bullet when we press space bar bullet will fire
            if event.key == pygame.K_SPACE:
                bulletX= playerX
                fire_bullet(playerX,bulletY)

                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                playerX_change = 0
                
    #checking for boundaries  of spaceship so it does go outside the bounds 
    playerX += playerX_change
    #boundary for the spaceship
    if playerX <=0:
        playerX=0
    elif playerX>=736:
        playerX=736

    #checking for boundaries  of enemy so it does go outside the bounds 
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        #boundary for the enemy
        if enemyX[i] <=0:
            enemyX_change[i]=0.3
            enemyY[i] +=enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i]= -0.3
            enemyY[i] +=enemyY_change[i]
        #collision 
        collision= isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=450
            bullet_state="ready"
            score_value+=1
             
            
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
    #bullet status
    if bulletY<=0:
        bulletY=450
        bullet_state="ready"
    #bullet state
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY-= bulletY_change
     

    player(playerX,playerY)
    show_score(textX,testY)
    pygame.display.update() 