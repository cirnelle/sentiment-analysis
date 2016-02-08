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

		lines = open(path_to_concept_url_list, 'r').readlines()

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

		lines = open(path_to_concept_list,'r').readlines()

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

		print ("Length of ngram list is "+str(len(ngram_list)))

		return (ngram_list)


	def create_tweet_list(self):

		# create a list of tweets, e.g. ['This is the first tweet', 'This is another tweet', ...]
		# splitlines method to remove '\n' from end of line
		lines = open(path_to_processed_tweets).read().splitlines()

		# add blank space to front and end of line for each tweet, in case the ngram is the first or last word in the sentence
		# e.g. ngram = ' the end ', and the tweet is 'that is the end', if we don't add space the ngram won't be detected

		lines=[' '+x+' ' for x in lines]

		return lines

	def get_sentiment_polarity(self):

	################
	# Create a polarity list, i.e. [['zone', '0.056'], ['zone out', '0.619'],...]
	# write result to a file
	################

		concept_list = self.create_concept_list()

		graph = rdflib.Graph()
		graph.parse(location='dictionary/senticnet3.rdf.xml')

		polarity_list = []

		print ("creating sentiment polarity list ...")

		t1 = time.time()

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

	###############
	# Create a polarity dictionary using the polarity_list.txt as input file
	# result: {' a little ': -0.125, ' a lot of books ': '0.047', ...}
	###############

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

		print ("Length of polarity dict is "+str(len(polarity_dict)))

		return polarity_dict

	def calculate_senti_score(self):

		senti_dict = self.create_polarity_dict()
		tweet_list = self.create_tweet_list()
		ngram_list = self.create_ngram_list()

		# add white space to front and end of terms so whole words can be matched

		ngram_list = [' '+nl+' ' for nl in ngram_list]

		tweet_score_list = []

		print ("Calculating sentiment score ...")

		t1 = time.time()

		for tl in tweet_list:

			tl = tl.lower()

			tweet_score = []

			string = tl

			senti_score = 0

			for nl in ngram_list:

				substring = nl

				if substring in string:

					senti_score += float(senti_dict[substring])

					# remove the substring (which are ngrams) from the tweet and replace with space
					# so that if two adjacent sentiment terms are found they can be detected
					string = string.replace(substring,' ')


			tweet_score.append(str(round((senti_score),3)))
			tweet_score.append(tl)

			tweet_score_list.append(tweet_score)

		t2 = time.time()

		total_time = (t2 - t1)/60

		print ("Computing time was "+str(total_time)+" minutes.")

		f = open('results/tweets_senti_score.txt', 'w')

		for tsl in tweet_score_list:
			f.write(', '.join(tsl)+'\n')

		f.close()

		return tweet_score_list



if __name__ == "__main__":

	path_to_concept_url_list = 'dictionary/concept_url.txt'
	path_to_concept_list = 'dictionary/concepts.txt'
	path_to_processed_tweets = '../tweets/preprocessed_tweets.txt'

	sn = SenticNet()
	#sn.create_concept_list()
	#sn.create_ngram_list()
	#sn.get_sentiment_polarity()
	#sn.create_polarity_dict()
	sn.calculate_senti_score()

