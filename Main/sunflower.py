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
