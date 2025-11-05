import global_utilities
import sunflower
import pumpkin

def isHarvestable(loc = (get_pos_x(),get_pos_y())):
	curCrop = global_utilities.getCropTypeAtPosition(loc)
	#data validation
	if curCrop == None:
		return False
	elif not can_harvest():
		return False
	elif curCrop == Entities.Pumpkin:
		if pumpkin.canHarvest():
			return True
		else:
			return False
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
			elif curCrop == Entities.Pumpkin:
				pumpkin.harvestedNotify()
				return harvest()
			else:
				return False
		return harvest()
	else:
		return False

def autonomousHarvesting():
	#don't automatically harvest sunflowers
	#if get_entity_type() == Entities.Sunflower:
		#return
	return performHarvest()
