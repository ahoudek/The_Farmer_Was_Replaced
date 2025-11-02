import global_utilities
import supplements
import pumpkin
import sunflower
import movement

__cropsPreferredGround = {Entities.Grass:Grounds.Grassland, Entities.Bush:Grounds.Grassland, Entities.Tree:Grounds.Grassland, Entities.Carrot:Grounds.Soil, Entities.Cactus:Grounds.Soil, Entities.Sunflower:Grounds.Soil, Entities.Pumpkin:Grounds.Soil}

def isEnergyLow():
	global_utilities.updateResourceValues()
	if global_utilities.energyNum < 1: #.1
		return True
	return False

def isPlantable(crop):
	plantType = get_entity_type()
	if crop != None:
		#check if it's trying to plant something that isn't a pumpkin in the pumpkin patch
		if crop != Entities.Pumpkin and pumpkin.isInPumpkinPatch():
			return False
		#check if there is already something planted there besides grass
		if plantType != Entities.Grass and plantType != None and plantType != Entities.Dead_Pumpkin:
			return False
		#if crop == Entities.Sunflower and not sunflower.okToPlantSunflower():
		#	return False
		#don't plant a tree next to another tree
		if crop == Entities.Tree and movement.checkSurroundingTilesForCrop(crop):
			return False
		#harvest any grown crop if it's there instead of wasting it by planting over, except for special harvest cases
		if plantType != Entities.Pumpkin and plantType != Entities.Sunflower: #plantType == Entities.Grass:
			if can_harvest():
				harvest()
		#check if the ground needs to be tilled. if so, till it
		if __cropsPreferredGround[crop] != get_ground_type():
			till()
		return True
	return False

def performPlant(crop):
	if crop != None:
		if isPlantable(crop):
			if crop == Entities.Sunflower:
				#sunflower planting process
				plant(crop)
				supplements.useSupplements()
				sunflower.plantedSunflowers[(get_pos_x(), get_pos_y())] = measure()
				return True
			else:
				#general planting process
				if plant(crop):
					supplements.useSupplements()
					return True
				return False
	return False

def defaultChooseCrop():
	#replace dead pumpkins
	if get_entity_type() == Entities.Dead_Pumpkin:
		return Entities.Pumpkin
	
	#determine what to plant based on current resources and previous crop	
	global_utilities.updateResourceValues()
	if get_entity_type() == None or get_entity_type() == Entities.Grass:
		if pumpkin.isInPumpkinPatch():
			return Entities.Pumpkin
		elif isEnergyLow() and sunflower.getNumOfPlantedFlowers() <= 10: #and (get_pos_x() % 2 == 0 or get_pos_y() % 2 == 0): #TODO spread out flowers
			return Entities.Sunflower
		elif get_entity_type() == Entities.Tree or get_pos_x() == get_pos_y() or get_pos_x() + get_pos_y() == get_world_size() - 1:
			return Entities.Tree
		elif global_utilities.hayNum <= global_utilities.resourceValueFloor: #or global_utilities.hayNum < global_utilities.carrotNum:
			return Entities.Grass
		elif global_utilities.carrotNum <= global_utilities.resourceValueFloor:
			return Entities.Carrot
		elif global_utilities.mostInDemandCrop != None:
			return global_utilities.mostInDemandCrop
		else:
			return Entities.Grass
	return None

def autonomousPlanting():
	cropSelected = defaultChooseCrop()
	if performPlant(cropSelected) == False:
		#prevent empty square of nothing growing
		if cropSelected != None and get_ground_type() == Grounds.Soil: #TODO check this
			till()