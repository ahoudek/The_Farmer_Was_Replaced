import global_utilities
import supplements
import pumpkin
import sunflower

__cropsPreferredGround = {Entities.Grass:Grounds.Grassland, Entities.Bush:Grounds.Grassland, Entities.Tree:Grounds.Grassland, Entities.Carrot:Grounds.Soil, Entities.Cactus:Grounds.Soil, Entities.Sunflower:Grounds.Soil, Entities.Pumpkin:Grounds.Soil}

def isPlantable(crop, loc = (get_pos_x(),get_pos_y())):
	if crop != None:
		x,y = loc
		alreadyPlanted = global_utilities.farm[x][y]
		#check if it's trying to plant something that isn't a pumpkin in the pumpkin patch
		if crop != Entities.Pumpkin and global_utilities.fullPassCt % global_utilities.plantPumpkinsEvery == 0 and global_utilities.fullPassCt > 0 and crop != Entities.Sunflower:
			return False
		#harvest any grown crop if it's there instead of wasting it by planting over, except for special harvest cases
		if alreadyPlanted != None and alreadyPlanted != Entities.Pumpkin:
			if can_harvest():
				harvest()
		#don't plant a tree next to another tree
		if crop == Entities.Tree and global_utilities.isPositionSurroundedByCrop(crop, loc):
			return False
		return True
	return False

def performPlant(crop):
	if crop != None:
		if isPlantable(crop):
			#check if the ground needs to be tilled. if so, till it
			if __cropsPreferredGround[crop] != get_ground_type():
				till()
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
	currentlyPlanted = get_entity_type()
	#always replace dead pumpkins
	if currentlyPlanted == Entities.Dead_Pumpkin:
		return Entities.Pumpkin
	#determine what to plant based on current resources and previous crop	
	global_utilities.updateResourceValues()
	#plant pumpkins if on a pumpkin lap OR if we haven't harvested the pumpkin yet (majority of grid is pumpkins)
	if global_utilities.howManyOfCropPlanted(Entities.Pumpkin) > global_utilities.getMaxTileCount() / 2 or (global_utilities.fullPassCt % global_utilities.plantPumpkinsEvery == 0 and global_utilities.fullPassCt > 0):
		return Entities.Pumpkin
	elif global_utilities.powerNum <= global_utilities.criticalPowerLevel * 5 or sunflower.sfFloorForPlanting > sunflower.getNumOfPlantedFlowers():
		return Entities.Sunflower
	elif currentlyPlanted == Entities.Tree or get_pos_x() == get_pos_y() or get_pos_x() + get_pos_y() == get_world_size() - 1:
		return Entities.Tree
	elif global_utilities.hayNum <= global_utilities.resourceValueFloor:
		return Entities.Grass
	elif global_utilities.carrotNum <= global_utilities.resourceValueFloor:
		return Entities.Carrot
	elif global_utilities.mostInDemandCrop != None:
		return global_utilities.mostInDemandCrop
	else:
		return Entities.Grass

def autonomousPlanting():
	cropSelected = defaultChooseCrop()
	if cropSelected != None and performPlant(cropSelected) == False:
		#try again with another crop
		if performPlant(global_utilities.mostInDemandCrop) == False:
			#prevent empty square of nothing growing
			#if cropSelected != None and get_ground_type() == Grounds.Soil:
			#	till()
			return