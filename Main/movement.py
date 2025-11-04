import global_utilities

def moveDroneByOneTile(direction):
	#update original position
	global_utilities.updateFarmGridWithCurrentPosition()
	#do the move
	move(direction)
	#update new position
	global_utilities.updateFarmGridWithCurrentPosition()

def moveNextAsSnakePattern():
	maxPosValue = global_utilities.mapSize - 1
	x = get_pos_x()
	y = get_pos_y()
	#start over if at end of grid
	if (0, maxPosValue) == (x, y):
		goToPosition((0,0))
		rowInvert = False
		global_utilities.incrementFullPassCount()
	#move if not at last tile
	else:
		rowInvert = False
		if y % 2 == 0:
			rowInvert = False
		else:
			rowInvert = True
		#End of row, right
		if x == maxPosValue and not rowInvert:
			moveDroneByOneTile(North)
		#End of row, left
		elif x == 0 and rowInvert:
			moveDroneByOneTile(North)
		#Moving right	
		elif x < maxPosValue and not rowInvert:
			moveDroneByOneTile(East)
		#Moving left
		elif x > 0 and rowInvert:
			moveDroneByOneTile(West)

def goToPosition(position):
	if position != None: #and position != 0: #TODO remove 0 check once bug is gone
		x, y = position
		while x > get_pos_x():
			moveDroneByOneTile(East)
		while x < get_pos_x():
			moveDroneByOneTile(West)
		while y > get_pos_y():
			moveDroneByOneTile(North)
		while y < get_pos_y():
			moveDroneByOneTile(South)

def moveToCheckSurroundingTilesForCrop(cropType):
	originalPos = (get_pos_x(), get_pos_y())
	existsFlag = False
	if not existsFlag and moveDroneByOneTile(North):
		if get_entity_type() == cropType:
			existsFlag = True
		moveDroneByOneTile(South) #move back
	if not existsFlag and moveDroneByOneTile(East):
		if get_entity_type() == cropType:
			existsFlag = True
		moveDroneByOneTile(West) #move back
	if not existsFlag and moveDroneByOneTile(South):
		if get_entity_type() == cropType:
			existsFlag = True
		moveDroneByOneTile(North) #move back
	if not existsFlag and moveDroneByOneTile(West):
		if get_entity_type() == cropType:
			existsFlag = True
		moveDroneByOneTile(East) #move back
	if (get_pos_x(), get_pos_y() != originalPos):	
		goToPosition(originalPos)
	return existsFlag
