import global_utilities

rowInvert = False

farm = []

grid = [
	[Entities.Tree, Entities.Carrot, Entities.Bush],
	[Entities.Pumpkin, Entities.Tree, Entities.Grass],
	[Entities.Cactus, Entities.Carrot, Entities.Grass]
]

def continueToNext():
	global rowInvert
	#start over if at end of grid
	if (get_world_size() * get_world_size()) <= global_utilities.getTileCount():
		while get_pos_x() != 0:
			move(East)
		while get_pos_y() != 0:
			move(North)
		#reset
		rowInvert = False
		global_utilities.resetTileCount()
		global_utilities.incrementFullPassCount()
	else:
		#default movement
		global_utilities.incrementTileCount()
		if (get_pos_x() + 1) < get_world_size() and not rowInvert:
			move(East)
		elif rowInvert and get_pos_x() == 0:
			move(North)
			rowInvert = False
		else:
			if not rowInvert:
				move(North)
				rowInvert = True
			else:
				move(West)

def zigZagThroughFarm():
	continueToNext()

def goToPosition(position):
	if position != None and position != 0:
		x, y = position
		while x > get_pos_x():
			move(East)
		while x < get_pos_x():
			move(West)
		while y > get_pos_y():
			move(North)
		while y < get_pos_y():
			move(South)

def checkSurroundingTilesForCrop(cropType):
	originalPos = (get_pos_x(), get_pos_y())
	existsFlag = False
	if not existsFlag and move(North):
		if get_entity_type() == Entities.Tree:
			existsFlag = True
		move(South) #move back
	if not existsFlag and move(East):
		if get_entity_type() == Entities.Tree:
			existsFlag = True
		move(West) #move back
	if not existsFlag and move(South):
		if get_entity_type() == Entities.Tree:
			existsFlag = True
		move(North) #move back
	if not existsFlag and move(West):
		if get_entity_type() == Entities.Tree:
			existsFlag = True
		move(East) #move back
	if (get_pos_x(), get_pos_y() != originalPos):	
		goToPosition(originalPos)
	return existsFlag
