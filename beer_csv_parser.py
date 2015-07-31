import nltk
from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import numpy as np

import cPickle
import os

from random import shuffle
# class Beer(object):
# 	def __init__(self, brewId, beer, category, style, abv, description, adjectives, iden):
# 		self.name = beer
# 		self.category = category
# 		self.style = style
# 		self.abv = abv
# 		self.description = description
# 		self.id = iden
# 		self.brewId = brewId
# 		self.adjectives = adjectives

# class BeerManager(object):
# 	def __init__(self):
# 		self.nextAvailableIndex = 0
# 		self.beers = []

# 	def sortByIndex(self):
# 		return sorted(self.beers,key = lambda beer: beer.id)

# 	def getNextId(self):
# 		self.nextAvailableIndex = self.nextAvailableIndex + 1
# 		return self.nextAvailableIndex

# 	def addBeer(self, brewId, beer, category, style, abv, description, adjectives):
# 		self.beers.append(Beer(brewId, beer, category, style, abv, description, adjectives, self.getNextId()))



# beerManager = BeerManager()
# count = 0

# styles = []

# categories = ['British Ale',
# 'Irish Ale',
# 'North American Ale',
# 'German Ale',
# 'Belgian and French Ale',
# 'International Ale',
# 'German Lager',
# 'North American Lager',
# 'Other Lager',
# 'International Lager',
# 'Other Style']


# with open('./styles.csv', 'r') as f:
# 	styleData = map(lambda x: x.replace('"',''), f.readlines())
# 	styles = map(lambda x: x.split(',')[2], styleData[1:])

# with open('./beers.csv', 'r') as f:
# 	inputData = map(lambda x: x.replace('"',''), f.readlines())
# 	beerData = map(lambda x: x.split(',')[1:], inputData[1:])
# 	for line in beerData:
# 			try:
# 				if line[9] != '' and line[1] != '':
# 					count += 1
# 					if count % 100 == 0:
# 						print "PROGRESS:", count, "OUT OF 2036"
# 					tokens = nltk.word_tokenize(line[9])

# 					beerManager.addBeer(int(line[0]), line[1], categories[int(line[2])-1] if int(line[2]) != -1 else '', styles[int(line[3])-1] if int(line[3]) != -1 else '', float(line[4]),line[9], map(lambda y: y[0], filter(lambda x: x[1] == 'JJ', nltk.pos_tag(tokens))))
# 			except:
# 				1

corpus = ''
# Set the directory you want to start from
rootDir = '/Users/Kevin/Downloads/1-billion-word-language-modeling-benchmark-r13output/training-monolingual.tokenized.shuffled'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
  		with open('/Users/Kevin/Downloads/1-billion-word-language-modeling-benchmark-r13output/training-monolingual.tokenized.shuffled/' + fname, 'r') as f:
				corpus = corpus + f.read()

corp_list = corpus.split('\n')
length = len(corp_list)/10

shuffle(corp_list)

corpus = '\n'.join(corp_list[:length])


print "starting to run model"
model = word2vec.Word2Vec(corpus, workers=4,
            size=300, min_count = 5,
            window = 10, sample = 1e-3)
        #self.model.init_sims(replace=True)

f = open('./model.pickle', 'w')
cPickle.dump(model, f, cPickle.HIGHEST_PROTOCOL)
f.close()