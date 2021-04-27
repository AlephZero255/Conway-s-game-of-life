import pygame
import worldIteration as wi

pygame.init()

#Constants
BACKGROUNDCOLOR = (0, 0, 0)
CELLCOLOR = (0, 225, 0)
WIDTH = 500
HEIGHT = 500
SIZE = 10
CURSORCOLOR = (225, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Generate world
world = [[i*0 for i in range(0, WIDTH//SIZE)] for i in range(0, HEIGHT//SIZE)]

stop = True
mouse = {'column': 0, 'row': 0, 'down': False}

clock = pygame.time.Clock()
while 1:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
		if i.type == pygame.KEYDOWN:
			#PRESS KEY TO PAUSE/RESUME
			stop = not stop

		#Mouse events
		if i.type == pygame.MOUSEMOTION:
			mouse['column'] = round((i.pos[0] - 7)/SIZE)
			mouse['row'] = round((i.pos[1] - 7)/SIZE)
		if i.type == pygame.MOUSEBUTTONDOWN:
			mouse['down'] = True
		if i.type == pygame.MOUSEBUTTONUP:
			mouse['down'] = False

	clock.tick(60)
	#Clear canvas
	screen.fill(BACKGROUNDCOLOR)
	
	#If mouse button is pressed
	if mouse['down']:
		#Create new living cell in mouse coordinates
		world[mouse['row']][mouse['column']] = 1

	#If game not stopped
	if not stop:
		#Next world iteration
		world = wi.nextIter(world)

	#Draw function
	for y in range(len(world)):
		for x in range(len(world[y])):
			if world[y][x] == 1:
				pygame.draw.rect(screen, CELLCOLOR, (x*SIZE, y*SIZE, SIZE, SIZE))

	#Draw rect in mouse coordinates
	pygame.draw.rect(screen, CURSORCOLOR, (mouse['column']*SIZE, mouse['row']*SIZE, SIZE, SIZE), 1)

	pygame.display.update()