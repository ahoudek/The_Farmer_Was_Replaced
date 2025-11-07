#constants
mapSize = get_world_size()
resourceValueFloor = 10000000
criticalPowerLevel = mapSize
plantSunflowersEvery = 4
plantPumpkinsEvery = 5
mostInDemandCrop = Entities.Carrot
directions = [North,South,East,West]

#navigation/movement
currentTileCount = 0
fullPassCt = 0

#available resource values
hayNum = num_items(Items.Hay)
woodNum = num_items(Items.Wood)
carrotNum = num_items(Items.Carrot)
pumpkinNum = num_items(Items.Pumpkin)
powerNum = num_items(Items.Power)

#farm/map grid
farm = []
i = 0
while i < mapSize:
	row = []
	j = 0
	while j < mapSize:
		tile = []
		x = 0
		while x < 3:
			tile.append(None)
			x += 1
		row.append(tile)
		j += 1
	farm.append(row)
	i += 1

def init():
	if fullPassCt == 0 and get_pos_x() == 0 and get_pos_y() == 0:
		updateFarmGridWithCurrentPosition()

def updateFarmGridWithCurrentPosition():
	global farm
	x = get_pos_x()
	y = get_pos_y()
	farm[x][y] = [get_entity_type(),get_ground_type(),measure()]

def getCropTypeAtPosition(position = (get_pos_x(), get_pos_y())):
	global farm
	x, y = position
	return farm[x][y][0]

def getGroundTypeAtPosition(position = (get_pos_x(), get_pos_y())):
	global farm
	x, y = position
	return farm[x][y][1]

def isPositionSurroundedByCrop(cropType, position):
	global farm
	x,y = position
	if x < mapSize - 1 and farm[x+1][y][0] == cropType:
		return True
	if x > 0 and farm[x-1][y][0] == cropType:
		return True
	if y < mapSize - 1 and farm[x][y+1][0] == cropType:
		return True
	if y > 0 and  farm[x][y-1][0] == cropType:
		return True
	return False

def howManyOfCropPlanted(cropType):
	global farm
	count = 0
	for i in farm:
		for x in i:
			if x[0] == cropType:
				count += 1
	return count

def getTileCount():
	global currentTileCount
	return currentTileCount

def incrementTileCount():
	global currentTileCount
	currentTileCount += 1

def resetTileCount():
	global currentTileCount
	currentTileCount = 0

def getMaxTileCount():
	return mapSize * mapSize

def getFullPassCount():
	global fullPassCt
	return fullPassCt

def incrementFullPassCount():
	global fullPassCt
	fullPassCt += 1
	print(fullPassCt)

def updateResourceValues():
	global hayNum
	global woodNum
	global carrotNum
	global pumpkinNum
	global powerNum
	global resourceValueFloor
	global criticalPowerLevel

	hayNum = num_items(Items.Hay)
	woodNum = num_items(Items.Wood)
	carrotNum = num_items(Items.Carrot)
	pumpkinNum = num_items(Items.Pumpkin)
	powerNum = num_items(Items.Power)

	#update resource floor dynamically based on lowest quantity resource
	resources = [hayNum, woodNum, carrotNum, pumpkinNum]
	lowestResourceAmt = resourceValueFloor
	for r in resources:
		if r < lowestResourceAmt:
			lowestResourceAmt = r
	resourceValueFloor = lowestResourceAmt
