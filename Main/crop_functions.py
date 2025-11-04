#controller
import global_utilities
import planting
import harvesting
import movement
import sunflower
import pumpkin

__distantCropsToPlant = []

def tryHarvestCrop():
	if harvesting.performHarvest():
		return True
	return False

def tryPlantCrop(crop):
	if planting.performPlant(crop):
		return True
	return False

def replaceCrop(newCrop):
	if tryHarvestCrop():
		if tryPlantCrop(newCrop):
			return True
	return False

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

def checkForQueuedPlants():
	#check for nearby companion plants in queue and plant those if possible
	originalLoc = (get_pos_x(), get_pos_y())
	for i in __distantCropsToPlant:
		plannedPlanting = i
		if isDistanceTooFar(plannedPlanting[0]) == False:
			plantAtLocation(plannedPlanting[1],plannedPlanting[0])
			__distantCropsToPlant.remove(plannedPlanting)

	if originalLoc != ((get_pos_x(), get_pos_y())):
		movement.goToPosition(originalLoc)
	
def tryGoPlantCompanion():
	goNext = False
	originalLoc = (get_pos_x(), get_pos_y())
	checkForQueuedPlants()
	#if companion exists, check if position is valid for the crop it wants
	while goNext == False and get_companion() != None:
		type, pos = get_companion()
		if planting.isPlantable(type, pos):
			#if valid for planting and not too far away, go to it
			if isDistanceTooFar(pos) == False:
				#plant companion if possible
				goNext = plantAtLocation(type, pos)
				#check for others in queue nearby and plant them while there if possible
				checkForQueuedPlants()
			else:
				#if valid but too far away, add to queue and move on
				__distantCropsToPlant.append((pos, type))
				goNext = True
	#if invalid location or if planting failed, move on
	if originalLoc != ((get_pos_x(), get_pos_y())):
		movement.goToPosition(originalLoc)

def findSunflowerIfPowerCritical():
	originalLoc = (get_pos_x(), get_pos_y())
	global_utilities.updateResourceValues()
	if global_utilities.powerNum < global_utilities.criticalPowerLevel:
		#harvest until level is higher than minimum so we don't keep coming back to this as it barely rises and barely drops below threshold
		#must also check if sunflowers are actually planted before trying to find and harvest them
		while global_utilities.powerNum <= global_utilities.criticalPowerLevel * 2 and sunflower.getNumOfPlantedFlowers() > sunflower.sfFloorForPlanting:
			bestFlowerIndex = sunflower.getHighestPetalsFlower()
			if bestFlowerIndex != 0:
				movement.goToPosition(bestFlowerIndex)
				replaceCrop(Entities.Sunflower)
				global_utilities.updateResourceValues()
		if originalLoc != (get_pos_x(),get_pos_y()):
			movement.goToPosition(originalLoc)

def autoCropProcess():
	#harvest current tile if possible (call needed because of pumpkins, sunflowers,
	#which are not included in plant method's harvesting when plant is detected)
	harvesting.autonomousHarvesting()

	#plant best crop for this position in the current tile, if possible
	planting.autonomousPlanting()

def mainLoop():
	#if energy is critical and there are enough sunflowers planted, harvest the best one(s) to raise power level
	#if at a different position than original, return to original position after
	findSunflowerIfPowerCritical()

	#if the current position plant wants a companion, go plant it if possible, then come back to this location to harvest and re-plant
	#if too far away, add to queue for when drone is close to position next
	#continues until planted crop does not have a companion or planting the companion at its desired location is invalid or too far away
	tryGoPlantCompanion()

	#the harvest/plant process
	autoCropProcess()

	#continue to next tile
	movement.moveNextAsSnakePattern()