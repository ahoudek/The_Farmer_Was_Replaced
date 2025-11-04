import global_utilities
import sunflower
import pumpkin

def isHarvestable(loc = (get_pos_x(),get_pos_y())):
	curCrop = global_utilities.getCropTypeAtPosition(loc)
	if curCrop == Entities.Dead_Pumpkin or not can_harvest():
		return False
	#data validation
	elif curCrop == None:
		return False
	#if crop is pumpkin, check if pumpkin fully grown
	elif curCrop == Entities.Pumpkin:
		if pumpkin.isPumpkinReadyForHarvest():
			return True
		else:
			return False
	#if crop is sunflower, check if flower has the highest number of petals or if power is low enough to need to harvest
	elif curCrop == Entities.Sunflower and sunflower.getNumOfPlantedFlowers() >= sunflower.sfFloorForPlanting:
		if sunflower.isBestSunflower() or global_utilities.powerNum <= global_utilities.criticalPowerLevel:
			return True
	else:
		return True
	return False

def performHarvest():
	if isHarvestable():
		curLoc = (get_pos_x(),get_pos_y())
		curCrop = get_entity_type()
		if curCrop == Entities.Sunflower:
			#special sunflower harvesting process
			if curLoc in sunflower.plantedSunflowers:
				sunflower.plantedSunflowers.pop(curLoc)
				return harvest()
			else:
				return False
		return True
	else:
		return False

def autonomousHarvesting():
	#don't automatically harvest sunflowers
	if get_entity_type() == Entities.Sunflower:
		return
	return performHarvest()
