import copy

#Next world iteration function
def nextIter(world):
	#Create mutable world
	newWorld = copy.deepcopy(world)


	for y in range(len(world)):
		for x in range(len(world[y])):
			#If current cell went beyond boundaries
			if x < 1 or y < 1 or x > len(world[0]) - 2 or y > len(world) - 2:
				#Next cell
				continue

			neighbors = 0
			#Get all neighbors of the current cell
			if world[y - 1][x] == 1:
				neighbors += 1

			if world[y][x - 1] == 1:
				neighbors += 1

			if world[y - 1][x - 1] == 1:
				neighbors += 1

			if world[y + 1][x] == 1:
				neighbors += 1
			
			if world[y][x + 1] == 1:
				neighbors += 1

			if world[y + 1][x + 1] == 1:
				neighbors += 1

			if world[y - 1][x + 1] == 1:
				neighbors += 1

			if world[y + 1][x - 1] == 1:
				neighbors += 1
			

			#If current cell is living
			if world[y][x] == 1:
				#If overpopulation or underpopulation, current cell is died
				if neighbors > 3 or neighbors < 2:
					newWorld[y][x] = 0

			#If current cell is dead
			if world[y][x] == 0:
				#If num of neighbors equal 3, current cell is comes alive (Rules Conway's game of life)
				if neighbors == 3:
					newWorld[y][x] = 1

	return newWorld