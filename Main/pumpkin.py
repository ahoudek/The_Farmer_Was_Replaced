#key pumpkins for measuring size (Column#:ID#)
keyPumpkinsIds = {}
worldSz = get_world_size()
__botPumY = 0
__botPum2Y = worldSz / 2 - 2
__topPum2Y = worldSz / 2 + 1
__topPumY = worldSz - 1

def isInPumpkinPatch(position = (get_pos_x(), get_pos_y())):
	if get_entity_type() == Entities.Dead_Pumpkin:
		return True
	#patch is right side of map only, excluding the two middle rows that would make the patch not square
	if position[0] > (get_world_size() / 2) and position[1] != get_world_size() / 2 - 1 and position[1] != get_world_size() / 2:
		return True
	return False

def updateMeasuringPumpkinIds():
	global worldSz
	if len(keyPumpkinsIds) <= 0: #init
		keyPumpkinsIds[__botPumY] = None
		keyPumpkinsIds[__botPum2Y] = None
		keyPumpkinsIds[__topPum2Y] = None
		keyPumpkinsIds[__topPumY] = None

	column = get_pos_y()
	if column in keyPumpkinsIds:
		keyPumpkinsIds[column] = measure()

def isPumpkinReadyForHarvest():
	global worldSz
	col = get_pos_y()
	if isInPumpkinPatch():
		updateMeasuringPumpkinIds()
		if col < (get_world_size() / 2):
			if keyPumpkinsIds[__botPumY] != None and keyPumpkinsIds[__botPum2Y] != None:
				if keyPumpkinsIds[__botPumY] == keyPumpkinsIds[__botPum2Y]:
					return True
		if keyPumpkinsIds[__topPumY] != None and keyPumpkinsIds[__topPum2Y] != None:
			if col >= (get_world_size() / 2):
				if keyPumpkinsIds[__topPumY] == keyPumpkinsIds[__topPum2Y]:
					return True
	return False