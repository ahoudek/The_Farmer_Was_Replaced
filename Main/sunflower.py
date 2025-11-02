#plantedSfCt = 0
sfHighPetalCount = 0
sfHighPetalCountLoc = None
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

#def prepForPlantingSunflower():
	#plantedSunflowers[(get_pos_x(), get_pos_y())] = measure()
	#checkPetals(highestNumPetals)

def okToPlantSunflower():
	if get_pos_x() % 2 == 0: #and get_pos_x() % (get_world_size() / 2) == 0:
		return True
	return False

def checkPetals(highestNumPetals):
	if highestNumPetals == None:
		print('Error')
		return None
	if measure() == None:
		print('Failed to Measure')
		return None
	if highestNumPetals < measure():
		return (get_pos_x(), get_pos_y())
	else:
		return None

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

def harvestBestSunflower(): #TODO
	flowerPos = getHighestPetalsFlower()
	if flowerPos != None:
		#goToPosition(flowerPos)
		#harvestCrop()
		#replant
		#TODO can remove this once the planting function is better
		#sunflower.preparePlantSunflower()
		#planting.plantCropHere(Entities.Sunflower, True)
		return True
	return False	