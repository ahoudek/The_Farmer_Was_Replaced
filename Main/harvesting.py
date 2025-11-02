import sunflower
import pumpkin

def isHarvestable():
	curCrop = get_entity_type()
	if not can_harvest():
		return False
	#data validation
	if curCrop == None or curCrop == Entities.Dead_Pumpkin:
		return False
	#if crop is pumpkin, check if pumpkin fully grown
	elif curCrop == Entities.Pumpkin:
		if pumpkin.isPumpkinReadyForHarvest():
			return True
	#if crop is sunflower, check if flower has the highest number of petals
	elif curCrop == Entities.Sunflower:
		if sunflower.isBestSunflower():
			return True
	else:
		return True
	return False

def performHarvest():
	if isHarvestable():
		curLoc = (get_pos_x(), get_pos_y())
		curCrop = get_entity_type()
		if curCrop == Entities.Sunflower:
			#special sunflower harvesting process
			if curLoc in sunflower.plantedSunflowers:
				sunflower.plantedSunflowers.pop(curLoc)
		#elif curCrop == Entities.Pumpkin:
		return harvest()
	return False

def autonomousHarvesting():
	#don't automatically harvest sunflowers
	if get_entity_type() == Entities.Sunflower:
		return
	success = performHarvest()
