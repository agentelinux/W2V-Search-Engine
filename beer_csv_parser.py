class Beer(object):
	def __init__(self, brewId, beer, category, style, abv, description, iden):
		self.name = beer
		self.category = category
		self.style = style
		self.abv = abv
		self.description = description
		self.id = iden
		self.brewId = brewId

class BeerManager(object):
	def __init__(self):
		self.nextAvailableIndex = 0
		self.beers = []

	def sortByIndex(self):
		return sorted(self.beers,key = lambda beer: beer.id)

	def getNextId(self):
		self.nextAvailableIndex+=1
		return self.nextAvailableIndex

	def addBeer(self, brewId, beer, category, style, abv, description):
		self.beers.append(Beer(brewId, beer, category, style, abv, description, self.getNextId))



beerManager = BeerManager()
count = 0

with open('./beers.csv', 'r') as f:
	inputData = f.readlines()
	beerData = map(lambda x: x.split(',')[1:], inputData[1:])
	for line in beerData:
			try:
				if line[9] != '' and line[1] != '':
					beerManager.addBeer(int(line[0]), line[1], int(line[2]), int(line[3]), float(line[4]),line[9])
			except:
				1

print beerManager.beers[0].name