#navigation/movement
currentTileCount = 0
fullPassCt = 0
directions = [North,South,East,West]

#available resource values
hayNum = num_items(Items.Hay)
woodNum = num_items(Items.Wood)
carrotNum = num_items(Items.Carrot)
pumpkinNum = num_items(Items.Pumpkin)
energyNum = num_items(Items.Power)

#constants
resourceValueFloor = 10000000
mostInDemandCrop = Entities.Carrot

def getTileCount():
	global currentTileCount
	return currentTileCount

def incrementTileCount():
	global currentTileCount
	currentTileCount += 1

def resetTileCount():
	global currentTileCount
	currentTileCount = 0

def getFullPassCount():
	global fullPassCt
	return fullPassCt

def incrementFullPassCount():
	global fullPassCt
	fullPassCt += 1

def resetFullPassCount():
	global fullPassCt
	fullPassCt = 0

def updateResourceValues():
	global hayNum
	global woodNum
	global carrotNum
	global pumpkinNum
	global energyNum
	global resourceValueFloor

	hayNum = num_items(Items.Hay)
	woodNum = num_items(Items.Wood)
	carrotNum = num_items(Items.Carrot)
	pumpkinNum = num_items(Items.Pumpkin)
	energyNum = num_items(Items.Power)

	#update resource floor dynamically based on lowest quantity resource
	resources = [hayNum, woodNum, carrotNum, pumpkinNum]
	lowestResourceAmt = resourceValueFloor
	for r in resources:
		if r < lowestResourceAmt:
			lowestResourceAmt = r
	resourceValueFloor = lowestResourceAmt