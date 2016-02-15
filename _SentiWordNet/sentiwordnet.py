__author__ = 'yi-linghwong'

import os
import sys
import time


class SentiWordNet():

    def create_senti_dict(self):

        lines = open(path_to_sentiment_dictionary, 'r').readlines()

        senti_dict = {}

        print ("Creating sentiment dictionary ...")

        for line in lines:
            spline = line.replace("\n","").split(', ')

            # add blank space before and after term
            # so that later we can match whole words to terms in the dictionary
            # instead of substring (e.g. 'go' will be matched to 'going' if no blank space added before and after 'go')

            spline[0] = ' '+spline[0]+' '

            senti_dict[spline[0]] = {'pos':spline[1],'neg':spline[2]}


        #print ("Length of sentiment dictionary is "+str(len(senti_dict)))

        return senti_dict


    def create_tweet_list(self):

        # create a list of tweets, e.g. ['This is the first tweet', 'This is another tweet', ...]
        # splitlines method to remove '\n' from end of line
        lines = open(path_to_processed_tweet_file).read().splitlines()

        # add blank space to front and end of line for each tweet, in case the ngram is the first or last word in the sentence
        # e.g. ngram = ' the end ', and the tweet is 'that is the end', if we don't add space the ngram won't be detected

        lines=[' '+x+' ' for x in lines]

        return lines


    def create_ngram_list(self):

        ################
        # create a list of the ngrams from sentiment dictionary (only the terms, without their score)
        # i.e. ['go off the mark', 'going away', 'laughing', ...]
        ################

        ngram_list = []

        lines = open(path_to_sentiment_dictionary, 'r').readlines()

        print ("Creating ngram list ...")

        for line in lines:
            spline = line.replace('\n', '').split(', ')
            ngram_list.append(spline[0])

        # sort ngram_list by the number of words, so that longer-grams come first
        ngram_list.sort(key=lambda x: len(x.split()), reverse=True)

        return ngram_list


    def calculate_senti_score(self):

        senti_dict = self.create_senti_dict()
        tweet_list = self.create_tweet_list()
        ngram_list = self.create_ngram_list()

        print ("Length of tweet list is "+str(len(tweet_list)))

        # add white space to front and end of terms so whole words can be matched

        ngram_list = [' '+nl+' ' for nl in ngram_list]

        tweet_score_list = []
        tweet_score_list_polarity = []

        print ("Calculating sentiment score ...")

        t1 = time.time()

        for tl in tweet_list:

            tl = tl.lower()

            tweet_score = []
            tweet_score_c = []

            string = tl

            pos_score = 0
            neg_score = 0


            for nl in ngram_list:

                substring = nl

                if substring in string:

                    #print (str(substring)+" pos: "+str(senti_dict[substring]['pos'])+" neg: "+str(senti_dict[substring]['neg']))
                    pos_score += float(senti_dict[substring]['pos'])
                    neg_score += float(senti_dict[substring]['neg'])

                    # remove the substring (which are ngrams) from the tweet and replace with space
                    # so that if two adjacent sentiment terms are found they can be detected
                    string = string.replace(substring,' ')

                    #print ("Pos score is "+str(pos_score))
                    #print ("Neg score is "+str(neg_score))

            tweet_score.append(str(pos_score))
            tweet_score.append(str(neg_score))
            tweet_score.append(tl)

            tweet_score_list.append(tweet_score)

            # calculate the polarity (i.e. 'pos', 'neg' or 'neutral')

            sentiment = pos_score - neg_score

            if sentiment > 0:
                tweet_score_c.append('pos')

            elif sentiment < 0:

                tweet_score_c.append('neg')

            # if tweet has neutral score classify it as negative (only for datasets that do not have neutral!)
            elif sentiment == 0:
                tweet_score_c.append('neg')

            else:
                print ("error")

            tweet_score_c.append(tl)
            tweet_score_list_polarity.append(tweet_score_c)

        t2 = time.time()

        total_time = round(((t2 - t1) / 60),2)

        print ("Computing time was "+str(total_time)+" minutes.")

        f = open(path_to_store_results_score, 'w')

        for tsl in tweet_score_list:
            f.write(','.join(tsl)+'\n')

        f.close()

        f = open(path_to_store_results_polarity, 'w')

        for tslp in tweet_score_list_polarity:
            f.write(','.join(tslp)+'\n')

        f.close()

        return tweet_score_list


###############
# variables
###############

path_to_sentiment_dictionary = 'dictionary/avg_no_neutral.txt'

path_to_processed_tweet_file = '../_BLiu/results/neutral/SA_neutral.txt'
path_to_store_results_score = 'results/neutral/SA_neutral_senti_score.txt'
path_to_store_results_polarity = 'results/neutral/SA_neutral_senti_polarity.txt'


if __name__ == "__main__":


    swn = SentiWordNet()
    #swn.create_senti_dict()
    #swn.create_tweet_list()
    #swn.create_ngram_list()
    swn.calculate_senti_score()
