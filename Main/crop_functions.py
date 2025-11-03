#controls order, behavior, and interaction of modules
import planting
import harvesting
import movement
import sunflower
import pumpkin

__skipHarvestFlag = False
__distantCropsToPlant = []

def tryHarvestCrop():
	if harvesting.performHarvest():
		return True
	return False

def tryPlantCrop(crop):
	if planting.performPlant(crop):
		return True
	return False

#def replaceCrop(newCrop):
#	if tryHarvestCrop():
#		if tryPlantCrop(newCrop):
#			return True
#	return False

#def tryFindCropType():
	#only harvest big sunflowers
	#if curCrop == Entities.Sunflower and (sunflower.sfHighPetalCountLoc == get_pos_x(), get_pos_y() or sunflower.getNumOfPlantedFlowers() > 10): #and curTileCt % 2 == 0
	#if sunflower.plantedSunflowers != None and len(sunflower.plantedSunflowers) > 0 and (get_pos_x(), get_pos_y()) in sunflower.plantedSunflowers:
	#sunflower.plantedSunflowers.pop((get_pos_x(), get_pos_y()))

def plantAtLocation(crop, location):
	if crop != None and location != None:
		movement.goToPosition(location)
		return tryPlantCrop(crop)
	return False

def isDistanceTooFar(desiredLoc):
	currentPos = (get_pos_x(), get_pos_y())
	maxDistance = get_world_size() / 2
	#data validation
	if desiredLoc == None or currentPos == None:
		return True
	#check if distance is too far (before moving)
	if (desiredLoc[0] - currentPos[0] > maxDistance or desiredLoc[0] - currentPos[0] < -maxDistance) or (desiredLoc[1] - currentPos[1] > maxDistance or desiredLoc[1] - currentPos[1] < -maxDistance):
		return True
	return False
	
def tryGoPlantCompanion():
	global __skipHarvestFlag
	originalLoc = (get_pos_x(), get_pos_y())

	#check for nearby companion plants in queue
	for i in __distantCropsToPlant:
		plannedPlanting = i
		if isDistanceTooFar(plannedPlanting[0]) == False:
			plantAtLocation(plannedPlanting[1],plannedPlanting[0])
			__distantCropsToPlant.remove(plannedPlanting)

	if originalLoc != ((get_pos_x(), get_pos_y())):
		movement.goToPosition(originalLoc) #reset

	#plant companion plant if available
	if get_companion() != None:
		type, pos = get_companion()
		if not pumpkin.isInPumpkinPatch(pos):
			if isDistanceTooFar(pos) == False:
				plantAtLocation(type, pos)
				movement.goToPosition(originalLoc) #reset
			else:
				__distantCropsToPlant.append((pos, type))
				__skipHarvestFlag = True

def tryEnergyManagement():
	if planting.isEnergyLow() and movement.checkSurroundingTilesForCrop(Entities.Sunflower) == False:
		bestFlowerIndex = sunflower.getHighestPetalsFlower()
		if bestFlowerIndex != 0:
			movement.goToPosition(bestFlowerIndex)
			tryHarvestCrop()
			tryPlantCrop(Entities.Sunflower)

def mainLoop():
	global __skipHarvestFlag
	if not pumpkin.isInPumpkinPatch():
		tryGoPlantCompanion()
	if __skipHarvestFlag == False:
		harvesting.autonomousHarvesting()
	planting.autonomousPlanting()
	movement.zigZagThroughFarm()
	tryEnergyManagement()
	__skipHarvestFlag = False