import global_utilities

lastHarvestOnLap = -1

def canPlant():
	global lastHarvestOnLap
	#prevent pumpkins from being planted again after harvest so that other crops can be planted
	#don't replace existing alive pumpkins with more pumpkins
	if lastHarvestOnLap != global_utilities.getFullPassCount() and not get_entity_type() == Entities.Pumpkin:
		#iterate when to plant a pumpkin patch and make sure it's not already harvested
		if global_utilities.fullPassCt % global_utilities.plantPumpkinsEvery == 0 or not isPumpkinHarvested():
			return True
	return False

def canHarvest():
	#Check if any two tiles on opposite sides of the map have the same ID
	for i in global_utilities.farm[0]:
		for j in global_utilities.farm[global_utilities.mapSize - 1]:
			quick_print(str(i[2]) + ', ' + str(j[2]))
			if i[2] != None and i[2] == j[2]: #and j[2] != None
				quick_print('*** ' + str(i[2]) + ', ' + str(j[2]))
				return True
	return False

def isPumpkinHarvested():
	global lastHarvestOnLap
	if lastHarvestOnLap == global_utilities.getFullPassCount():
		return True
	if global_utilities.howManyOfCropPlanted(Entities.Pumpkin) > global_utilities.getMaxTileCount() / 4:
		return False
	if global_utilities.fullPassCt % global_utilities.plantPumpkinsEvery == 0:
		return False
	return True

def harvestedNotify():
	global lastHarvestOnLap
	lastHarvestOnLap = global_utilities.getFullPassCount()
