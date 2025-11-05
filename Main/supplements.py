defaultWaterLvl = 0.2
pumpkinWaterLvl = 0.0
flowerWaterLvl = 0.6

def useSupplements():
	global defaultWaterLvl
	global pumpkinWaterLvl
	global flowerWaterLvl
	lvl = 0
	
	crop = get_entity_type()
	if crop == Entities.Pumpkin:
		lvl = pumpkinWaterLvl
	elif crop == Entities.Sunflower:
		use_item(Items.Fertilizer)
		lvl = flowerWaterLvl
	elif crop == Entities.Tree:
		useFertilizer()
		lvl = flowerWaterLvl
	elif crop == Entities.Bush:
		use_item(Items.Fertilizer)
		lvl = flowerWaterLvl
	else:
		lvl = defaultWaterLvl
		
	if crop != Entities.Pumpkin:
		while get_water() < lvl:
			use_item(Items.Water)
		
def useFertilizer():
	use_item(Items.Fertilizer)
	use_item(Items.Weird_Substance)
