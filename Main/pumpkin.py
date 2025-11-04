import global_utilities

def isPumpkinReadyForHarvest():
	#Check if any two tiles on opposite sides of the map have the same ID
	for i in global_utilities.farm[0]:
		for j in global_utilities.farm[global_utilities.mapSize - 1]:
			print(i[2])
			print(j[2])
			if i[2] == j[2]:
				return True
	return False

	#col = get_pos_y()
	#if col < (global_utilities.mapSize / 2):
	#	if keyPumpkinsIds[__botPumY] != None and keyPumpkinsIds[__botPum2Y] != None:
	#		if keyPumpkinsIds[__botPumY] == keyPumpkinsIds[__botPum2Y]:
	#			return True
	#if keyPumpkinsIds[__topPumY] != None and keyPumpkinsIds[__topPum2Y] != None:
	#	if col >= (global_utilities.mapSize / 2):
	#		if keyPumpkinsIds[__topPumY] == keyPumpkinsIds[__topPum2Y]:
	#			return True
	#return False