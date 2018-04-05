#rectangle runner game
#author Steve Titus
#note playing around with pygame dont judge my lazy coding

import pygame
import time

#constants
grey=(200,200,200)
black=(0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
darkgrey = (100,100,100)

#Parameters
playerSpeed = 5
worldSpeed = 75
wallColor = darkgrey
playerColor = white
playerHealthColor = black
playerHealth = 5
worldColor=blue
worldBrightness=10


killCount=1
pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_blue = True
x = 100
y = 130
color = (0,128,255)
color2 = (255, 0 , 0)
clock = pygame.time.Clock()
offset=150

Sstate =0
range = 3
counter = 0
speedx = 0.2
speedy = 0.2
staticx = x
staticy = y
y=500
x=100
movementx = 0
movementy = 0

startTime = time.time()
while not done:

	#obstacles
	r2 = pygame.Rect(movementx+staticx+offset*0, movementy+staticy, 60, 500)
	r3 = pygame.Rect(movementy*0.5+staticx+offset*1, staticy-200, 80-movementx*0.7, 500)
	r4 = pygame.Rect(2*movementy+staticx+offset*2, staticy+movementx, 60+movementy*0.2, 500)
	r5 = pygame.Rect(movementy+staticx+offset*3, staticy-400, 80+movementy*0.4,(movementy+movementy)*1.5+720)
	r6 = pygame.Rect(staticx+offset*4-movementy*0.4, staticy, 60, 500)

	Goal = pygame.Rect(staticx+600,staticy-80,60,60)
	
	#make world
	screen.fill((abs(movementx)*4+worldBrightness,abs(movementy)*4+worldBrightness,abs(movementx+movementy)*2+worldBrightness))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				done = True
	#get user input
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: y -= playerSpeed
	if pressed[pygame.K_DOWN]: y += playerSpeed
	if pressed[pygame.K_LEFT]: x -= playerSpeed
	if pressed[pygame.K_RIGHT]: x += playerSpeed 

	#move Player
	playerOutline = pygame.Rect(x-80, y, 60, 60)
	playerCentre = pygame.Rect(x-80+15, y+15, 30, 30)

	#obstacle collision
	if playerOutline.colliderect(r2) or playerOutline.colliderect(r3) or playerOutline.colliderect(r4) or playerOutline.colliderect(r5) or playerOutline.colliderect(r6): 
		color = red
		y=500
		x=100
		killCount +=1
		print("You were hurt, Damage: " + str(playerHealth) + "/250")
		playerHealth += 5
		playerHealthColor = (playerHealth,0,0) 
		playerColor = (255-playerHealth,255-playerHealth,250-playerHealth)
	#out of bounds
	elif x > 800 or x < 40 or y > 560 or y < -20:
		y=500
		x=100
		killCount+=1
		playerHealth += 5
		print("You were hurt, Damage: " + str(playerHealth) + "/250")		
		playerHealthColor = (playerHealth,0,0)
		playerColor = (255-playerHealth,255-playerHealth,250-playerHealth)
	else: 
		color = wallColor	
	if playerHealth >= 250:
		print("You're bad. Get Better.")
		done = True
	#game win
	if playerOutline.colliderect(Goal):
		done = True
		color = green
		screen.fill(black)
		print("You Finally Didnt Die")

	#draw screen
	pygame.draw.rect(screen, playerColor, playerOutline)
	pygame.draw.rect(screen, playerHealthColor, playerCentre)
	pygame.draw.rect(screen, color, r2)
	pygame.draw.rect(screen, color, r3)
	pygame.draw.rect(screen, color, r4)
	pygame.draw.rect(screen, color, r5)
	pygame.draw.rect(screen, color, r6)
	pygame.draw.rect(screen, green, Goal)
	pygame.display.flip()

	#update Time
	clock.tick(100)
	
	#psudo random movement parameters
	if movementx >= 35 or movementx <= -5:
		speedx = speedx * -1
	movementx = movementx + speedx
	if movementy >= 30 or movementy <= -30:
		speedy = speedy * -1
	movementy = movementy + speedy

print("You Died " + str(killCount) + " Times")
print("Time Taken: " + str(time.time()-startTime) + " seconds")
time.sleep(0.5)



