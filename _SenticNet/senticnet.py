__author__ = 'yi-linghwong'

import rdflib
import os
import sys
import time
from rdflib import URIRef


class SenticNet():

	def create_concept_url_list(self):

	#############
	# create a list of concept URL, e.g. http://sentic.net/api/en/concept/a_little
	# this function is not really needed if we have the concept list
	#############

		lines = open('test.txt', 'r').readlines()

		concept_url_list = []

		for line in lines:
			spline = line.replace('\n','')

			concept_url_list.append(spline)

		print ("Length of concept URL list is "+str(len(concept_url_list)))

		return concept_url_list

	def create_concept_list(self):

	#############
	# Create a list of concepts, e.g. ['32_teeth', 'a_lot_of_space']
	#############

		lines = open('test1.txt','r').readlines()

		concept_list = []

		for line in lines:
			spline = line.replace('\n','')

			concept_list.append(spline)

		print ("Length of concept list is "+str(len(concept_list)))

		return (concept_list)

	def create_ngram_list(self):

	#############
	# Create a list of ngram, with no underscore between words, and in descending order
	# longer-gram first, e.g. ['a lot of people', 'abandoned person', 'person']
	#############

		concept_list = self.create_concept_list()

		ngram_list = []

		for cl in concept_list:
			cl = cl.replace('\n','')
			cl = cl.replace('_',' ')

			ngram_list.append(cl)

		# sort ngram_list by the number of words, so that longer-grams come first
		ngram_list.sort(key=lambda x: len(x.split()), reverse=True)

		return (ngram_list)


	def get_sentiment_polarity(self):

	################
	# Create a polarity list, i.e. [['zone', '0.056'], ['zone out', '0.619'],...]
	# write result to a file
	################

		concept_list = self.create_concept_list()

		graph = rdflib.Graph()
		graph.parse(location='dictionary/senticnet3.rdf.xml')

		polarity_list = []

		t1 = time.time()

		print ("creating sentiment polarity list ...")

		for cl in concept_list:

			polarity = []

			objects = graph.objects(subject=URIRef("http://sentic.net/api/en/concept/"+cl), predicate=URIRef("http://sentic.net/apipolarity"))

			for o in objects:

				polarity.append(cl)

				# toPython() method converts rdf object to python format
				polarity.append(str(o.toPython()))

				polarity_list.append(polarity)

		t2 = time.time()

		total_time = (t2 - t1)/60

		print ("Computing time was "+str(total_time)+" minutes.")

		print ("Length of polarity list is "+str(len(polarity_list)))

		f = open('dictionary/polarity_list.txt','w')

		for pl in polarity_list:

			f.write('\t'.join(pl)+'\n')

		f.close()

		return (polarity_list)


	def create_polarity_dict(self):

	#############
	# Create a polarity dictionary using the polarity_list.txt as input file
	# result: {' a little ': -0.125, ' a lot of books ': '0.047', ...}
	#############

		lines = open('dictionary/polarity_list.txt','r').readlines()

		polarity_dict = {}

		for line in lines:

			spline = line.replace('\n','').split('\t')

			spline[0] = spline[0].replace('_',' ')

			# add blank space before and after term
            # so that later we can match whole words to terms in the dictionary
            # instead of substring (e.g. 'go' will be matched to 'going' if no blank space added before and after 'go')

			spline[0] = ' '+spline[0]+' '

			polarity_dict[spline[0]] = spline[1]

		print ("Length of polarity dict is "+str(len(polarity_dict))

		return polarity_dict

	






'''
graph = rdflib.Graph()
graph.parse(location='test.rdf.xml')


objects = graph.objects(subject=URIRef("http://sentic.net/api/en/concept/32_teeth"),predicate = URIRef("http://sentic.net/apipolarity"))

for o in objects:
	print (o)

for s,p,o in graph:

	print (s)

'''

if __name__ == "__main__":

	path_to_concept_url_list = 'dictionary/concept_url.txt'
	path_to_concept_list = 'dictionary/concents.txt'

	sn = SenticNet()
	#sn.create_concept_list()
	#sn.create_ngram_list()
	#sn.get_sentiment_polarity()
	sn.create_polarity_dict()

