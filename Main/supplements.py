defaultWaterLvl = 0.0
pumpkinWaterLvl = 0.0
flowerWaterLvl = 0.6

def useSupplements():
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
