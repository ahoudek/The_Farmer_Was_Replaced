import global_utilities

sfHighPetalCount = 0
sfHighPetalCountLoc = None
sfFloorForPlanting = 10
plantedSunflowers = {}

def getNumOfPlantedFlowers():
	global plantedSunflowers
	return len(plantedSunflowers)

#TODO
#def shouldFlowerBeHarvested():
	#global sfHighPetalCount
	#global sfHighPetalCountLoc

	#plant new crops if able and measure if needed
	#newHighPetalCtLoc = chooseWhatToPlant(movement.getTotalSquareCount(), sfHighPetalCount)
	#if newHighPetalCtLoc != None:
	#    sfHighPetalCountLoc = newHighPetalCtLoc
	#    sfHighPetalCount = measure()

def canPlant():
	return

def canHarvest():
	return

def isBestSunflower():
	flower = getHighestPetalsFlower()
	if flower == (get_pos_x(), get_pos_y()):
		return True
	return False

def getHighestPetalsFlower():
	highestIndex = 0
	highestCt = 0

	if plantedSunflowers != None and len(plantedSunflowers) > 0:
		for i in plantedSunflowers:
			if plantedSunflowers[i] != None:
				if plantedSunflowers[i] > highestCt:
					highestCt = plantedSunflowers[i]
					highestIndex = i
	return highestIndex

def isHarvested():
	if global_utilities.fullPassCt % global_utilities.plantSunflowersEvery == 0: #and global_utilities.fullPassCt > 0:
		return False
	elif global_utilities.howManyOfCropPlanted(Entities.Sunflower) > global_utilities.getMaxTileCount() / 4:
		return False
	return True