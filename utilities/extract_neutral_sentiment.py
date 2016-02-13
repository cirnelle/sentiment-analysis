__author__ = 'yi-linghwong'

###############
# 1) extract neutral tweets from results of a sentiment lexicon (emoticon, BLiu, etc)
# 2) create file from labelled tweets with only the noneutral ones from lexicon (for performance comparison)
###############

import sys
import os

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
                neutral.append(r[1])

            else:
                print ("error")

        print ("Length of neutral list is "+str(len(neutral)))
        print ("Length of noneutral list is "+str(len(noneutral)))

        f = open(path_to_store_noneutral_file_lexicon,'w')

        for nnf in noneutral_full:
            f.write(','.join(nnf)+'\n')

        f.close()

        f = open(path_to_store_only_neutral_file_lexicon,'w')

        for n in neutral:
            f.write(n+'\n')

        f.close()

        return noneutral

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
        noneutral = self.get_neutral_and_noneutral_tweets() # [' this is a tweet ', ' this is another tweet ']

        labelled_noneutral = []

        # remove neutral from labelled list

        for l in labelled:
            # need to add space to front and back because we added space to the tweets in lexicon analysis
            l[1] = ' '+l[1]+' '

            if l[1] in noneutral:
                labelled_noneutral.append(l)

        print ("Length of labelled noneutral list is "+str(len(labelled_noneutral)))

        f = open(path_to_store_labelled_noneutral_list,'w')

        for ln in labelled_noneutral:
            f.write(','.join(ln)+'\n')

        f.close()

        return labelled_noneutral

if __name__ == '__main__':

    path_to_sentiment_result_file = '../_BLiu/results/sts_gold_tweets_senti_polarity.txt'
    path_to_store_only_neutral_file_lexicon = '../_BLiu/results/neutral/sts_gold_neutral_polarity.txt'
    path_to_store_noneutral_file_lexicon = '../_BLiu/results/neutral/sts_gold_noneutral_polarity.txt'

    path_to_unprocessed_labelled_tweets = '../tweets/labelled_tweets_sts_gold.txt'
    path_to_preprocessed_tweets = '../tweets/preprocessed_tweets_sts_gold.txt'

    path_to_store_labelled_noneutral_list = '../tweets/neutral/labelled_noneutral_sts_gold.txt'

    en = ExtractNeutralSentiment()

    #en.get_neutral_and_noneutral_tweets()
    #en.get_labelled_preprocessed_tweets()
    en.get_labelled_noneutral_tweets()