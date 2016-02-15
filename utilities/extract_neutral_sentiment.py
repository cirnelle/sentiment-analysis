#!/usr/local/bin/python3

__author__ = 'yi-linghwong'

###############
# 1) extract neutral tweets from results of a sentiment lexicon (emoticon, BLiu, etc)
# 2) create file from labelled tweets with only the noneutral ones from lexicon (for performance comparison)
###############

import sys
import os
import time

class ExtractNeutralSentiment():

    def get_neutral_and_noneutral_tweets(self):

    ################
    # returns a list of the noneutral tweets (tweets only)
    # create a file with the neutral tweets for pipeline
    ################

        lines = open(path_to_sentiment_result_file,'r').readlines()

        results = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            results.append(spline)

        print ("Length of original sentiment is "+str(len(results)))

        noneutral = [] #only tweets
        noneutral_full = [] #tweets and sentiment
        neutral = [] #only tweets

        for r in results:
            if r[0] != 'neutral':
                noneutral.append(r[1])
                noneutral_full.append(r)

            elif r[0] == 'neutral':
                # remove blank space from front and end of tweet
                r[1] = r[1][1:-1]
                neutral.append(r[1])

            else:
                print ("error")

        print ("Length of noneutral list is "+str(len(noneutral)))
        print ("Length of neutral list is "+str(len(neutral)))

        f = open(path_to_store_noneutral_file_lexicon,'w')

        for nnf in noneutral_full:
            f.write(','.join(nnf)+'\n')

        f.close()

        f = open(path_to_store_only_neutral_file_lexicon,'w')

        for n in neutral:
            f.write(n+'\n')

        f.close()

        return noneutral,noneutral_full

    def get_labelled_preprocessed_tweets(self):

    ################
    # create list of labelled tweets with the tweets preprocessed
    # tweets of the labelled tweets are not preprocessed, can't compare directly, need to zip two files
    ################

        lines = open(path_to_unprocessed_labelled_tweets,'r').readlines()

        polarity = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            polarity.append(spline[0])

        print ("Length of polarity list is "+str(len(polarity)))

        lines = open(path_to_preprocessed_tweets,'r').readlines()

        preprocessed = []

        for line in lines:
            spline = line.replace('\n','')
            preprocessed.append(spline)

        print ("Length of preprocessed tweets is "+str(len(preprocessed)))

        combined = zip(polarity,preprocessed)

        labelled_preprocessed = []

        for c in combined:
            c = list(c)
            labelled_preprocessed.append(c)

        print ("Length of labelled preprocessed list is "+str(len(labelled_preprocessed)))

        # overwrite the original unprocessed labelled tweets with labelled preprocessed tweets

        f = open(path_to_unprocessed_labelled_tweets,'w')

        for lp in labelled_preprocessed:
            f.write(','.join(lp)+'\n')

        f.close()

        return labelled_preprocessed

    def get_labelled_noneutral_tweets(self):

    ###############
    # get the labelled tweets which overlap with the noneutral list from lexicon (for performance comparison)
    ###############

        labelled = self.get_labelled_preprocessed_tweets() # [['neg','this is a tweet'],['pos,'this is a second tweet']]
        noneutral = self.get_neutral_and_noneutral_tweets()[0] # [' this is a tweet ', ' this is another tweet ']
        noneutral_full = self.get_neutral_and_noneutral_tweets()[1]

        labelled_noneutral = []
        labelled_neutral = []
        labelled_noneutral_tweet = []

        # remove neutral from labelled list

        print (labelled[:1])
        print (noneutral[:1])
        print (noneutral_full[:1])

        print ("Extracting neutral and noneutral overlap...")

        t1 = time.time()

        for l in labelled:
            # need to add space to front and back because we added space to the tweets in lexicon analysis
            l[1] = ' '+l[1]+' '

            if l[1] in noneutral:
                labelled_noneutral.append(l)
                labelled_noneutral_tweet.append(l[1])
            else:
                labelled_neutral.append(l)

        t2 = time.time()

        total_time = round(((t2 - t1) / 60),2)

        print ("Computing time was "+str(total_time)+" minutes.")

        print ("Length of labelled noneutral list is "+str(len(labelled_noneutral)))
        print ("Length of labelled neutral list is "+str(len(labelled_neutral)))

        ##############
        # Check if length of two lists are equal and print the missing tweet
        ##############


        if len(labelled_noneutral) != len(noneutral_full):
            print ("Length not equal")

            temp = []

            for nf in noneutral_full:
                if nf[1] not in labelled_noneutral_tweet:
                    temp.append(nf[1])

            print (len(temp))
            print ("Missing tweets are "+str(temp))

        f = open(path_to_store_labelled_noneutral_list,'w')

        for ln in labelled_noneutral:
            f.write(','.join(ln)+'\n')

        f.close()

        f = open(path_to_store_labelled_neutral_list,'w')

        for ln in labelled_neutral:
            f.write(','.join(ln)+'\n')

        f.close()

        return labelled_noneutral


#################
# variables
#################

# command line
path_to_sentiment_result_file = sys.argv[1]
path_to_store_only_neutral_file_lexicon = sys.argv[2]
path_to_store_noneutral_file_lexicon = sys.argv[3]
# 2 stage
#path_to_sentiment_result_file = '../_BLiu/results/sts_gold_tweets_senti_polarity.txt'
#path_to_store_only_neutral_file_lexicon = '../_BLiu/results/neutral/sts_gold_neutral.txt'
#path_to_store_noneutral_file_lexicon = '../_BLiu/results/neutral/sts_gold_noneutral.txt'
# 3 stage
#path_to_sentiment_result_file = '../_emoticon/results/SA_tweets_senti_polarity.txt'
#path_to_store_only_neutral_file_lexicon = '../_emoticon/results/neutral/SA_neutral.txt'
#path_to_store_noneutral_file_lexicon = '../_emoticon/results/neutral/SA_noneutral.txt'
#path_to_sentiment_result_file = '../_BLiu/results/neutral/emoticon_SA_senti_polarity.txt'
#path_to_store_only_neutral_file_lexicon = '../_BLiu/results/neutral/SA_neutral.txt'
#path_to_store_noneutral_file_lexicon = '../_BLiu/results/neutral/SA_noneutral.txt'
# big file
#path_to_sentiment_result_file = '../../data_files/labelled_tweets/SA/BLiu_results/SA_tweets_senti_polarity.txt'
#path_to_store_only_neutral_file_lexicon = '../../data_files/labelled_tweets/SA/BLiu_results/neutral/SA_neutral.txt'
#path_to_store_noneutral_file_lexicon = '../../data_files/labelled_tweets/SA/BLiu_results/neutral/SA_noneutral.txt'

# command line
path_to_unprocessed_labelled_tweets = sys.argv[4]
path_to_preprocessed_tweets = sys.argv[5]
# 2 stage
#path_to_unprocessed_labelled_tweets = '../tweets/labelled_tweets_sts_gold.txt'
#path_to_preprocessed_tweets = '../tweets/preprocessed_tweets_sts_gold.txt'
# 3 stage
#path_to_unprocessed_labelled_tweets = '../tweets/labelled_tweets_SA.txt'
#path_to_preprocessed_tweets = '../tweets/preprocessed_tweets_SA.txt'
#path_to_unprocessed_labelled_tweets = '../tweets/neutral/emoticon_labelled_neutral_SA.txt'
#path_to_preprocessed_tweets = '../_emoticon/results/neutral/SA_neutral.txt'
# big file
#path_to_unprocessed_labelled_tweets = '../../data_files/labelled_tweets/SA/labelled_tweets_SA.txt'
#path_to_preprocessed_tweets = '../../data_files/labelled_tweets/SA/preprocessed_tweets_SA.txt'

# command line
path_to_store_labelled_noneutral_list = sys.argv[6]
path_to_store_labelled_neutral_list = sys.argv[7]
# 2 stage
#path_to_store_labelled_noneutral_list = '../tweets/neutral/bliu_labelled_noneutral_sts_gold.txt'
#path_to_store_labelled_neutral_list = '../tweets/neutral/bliu_labelled_neutral_sts_gold.txt'
# 3 stage
#path_to_store_labelled_noneutral_list = '../tweets/neutral/emoticon_labelled_noneutral_SA.txt'
#path_to_store_labelled_neutral_list = '../tweets/neutral/emoticon_labelled_neutral_SA.txt'
#path_to_store_labelled_noneutral_list = '../tweets/neutral/bliu_labelled_noneutral_SA.txt'
#path_to_store_labelled_neutral_list = '../tweets/neutral/bliu_labelled_neutral_SA.txt'
# big file
#path_to_store_labelled_noneutral_list = '../../data_files/labelled_tweets/SA/neutral/labelled_noneutral_SA.txt'
#path_to_store_labelled_neutral_list = '../../data_files/labelled_tweets/SA/neutral/labelled_neutral_SA.txt'


if __name__ == '__main__':

    en = ExtractNeutralSentiment()

    #en.get_neutral_and_noneutral_tweets()
    #en.get_labelled_preprocessed_tweets()
    en.get_labelled_noneutral_tweets()