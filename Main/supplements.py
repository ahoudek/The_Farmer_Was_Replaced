defaultWaterLvl = 0.01
pumpkinWaterLvl = 0.1
flowerWaterLvl = 0.55

def useSupplements():
	useWater()
	#useFertilizer()

def useWater():
	global defaultWaterLvl
	global pumpkinWaterLvl
	global flowerWaterLvl
	lvl = 0
	
	if get_entity_type() == Entities.Pumpkin:
		lvl = pumpkinWaterLvl
	elif get_entity_type() == Entities.Sunflower:
		useFertilizer()
		lvl = flowerWaterLvl
	else:
		lvl = defaultWaterLvl
		
	while get_water() < lvl:
		use_item(Items.Water)
		
def useFertilizer():
	use_item(Items.Fertilizer)
	#use_item(Items.Weird_Substance)
